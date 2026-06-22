import requests
import json
import os
import time
import sys
from collections import defaultdict

USERNAME = os.environ.get("LEETCODE_USERNAME")
SESSION = os.environ.get("LEETCODE_SESSION")
CSRF = os.environ.get("LEETCODE_CSRF_TOKEN")

if not all([USERNAME, SESSION, CSRF]):
    print("ERROR: Missing environment variables!")
    print(f"  USERNAME set: {bool(USERNAME)}")
    print(f"  SESSION set:  {bool(SESSION)}")
    print(f"  CSRF set:     {bool(CSRF)}")
    sys.exit(1)

headers = {
    "Cookie": f"LEETCODE_SESSION={SESSION}; csrftoken={CSRF}",
    "x-csrftoken": CSRF,
    "Referer": "https://leetcode.com",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0",
}

def fetch_all_submissions():
    submissions = []
    offset = 0
    limit = 20
    while True:
        url = f"https://leetcode.com/api/submissions/?offset={offset}&limit={limit}&lastkey="
        res = requests.get(url, headers=headers)
        
        if res.status_code != 200:
            print(f"ERROR fetching submissions: HTTP {res.status_code}")
            print(res.text[:500])
            sys.exit(1)

        data = res.json()
        batch = data.get("submissions_dump", [])
        
        if not batch:
            break

        accepted = [s for s in batch if s["status_display"] == "Accepted"]
        submissions.extend(accepted)
        print(f"  Fetched offset {offset}, total accepted so far: {len(submissions)}")

        if not data.get("has_next"):
            break

        offset += limit
        time.sleep(1.5)

    # Deduplicate by title_slug, keep latest
    seen = set()
    unique = []
    for s in submissions:
        if s["title_slug"] not in seen:
            seen.add(s["title_slug"])
            unique.append(s)
    return unique

def fetch_problem_tags(title_slug):
    query = """
    query getTopicTags($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        topicTags { name }
        questionFrontendId
        title
      }
    }
    """
    try:
        res = requests.post(
            "https://leetcode.com/graphql",
            headers=headers,
            json={"query": query, "variables": {"titleSlug": title_slug}},
            timeout=10,
        )
        if res.status_code != 200:
            print(f"  WARNING: GraphQL returned {res.status_code} for {title_slug}")
            return None
        return res.json().get("data", {}).get("question", {})
    except Exception as e:
        print(f"  WARNING: Exception for {title_slug}: {e}")
        return None

def generate_readme(tag_map, slug_to_meta, repo_url):
    lines = [
        "# LeetCode",
        "~Leetcode Solutions\n",
        "<!---LeetCode Topics Start-->",
        "# LeetCode Topics",
    ]
    for tag in sorted(tag_map.keys()):
        lines.append(f"## {tag}")
        lines.append("|  |")
        lines.append("| ------- |")
        for slug in sorted(tag_map[tag]):
            meta = slug_to_meta[slug]
            fid = str(meta["questionFrontendId"]).zfill(4)
            lines.append(f"| [{fid}-{slug}]({repo_url}/tree/master/{fid}-{slug}) |")
        lines.append("")
    lines.append("<!---LeetCode Topics End-->")
    return "\n".join(lines)

def get_repo_url():
    # Try to detect from git remote
    try:
        import subprocess
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True, text=True
        )
        url = result.stdout.strip()
        # Convert SSH to HTTPS if needed
        if url.startswith("git@github.com:"):
            url = url.replace("git@github.com:", "https://github.com/").rstrip(".git")
        return url.rstrip(".git")
    except:
        return f"https://github.com/{USERNAME}/LeetCode"

def main():
    print(f"Starting sync for user: {USERNAME}")
    repo_url = get_repo_url()
    print(f"Repo URL: {repo_url}")

    print("\nFetching submissions...")
    submissions = fetch_all_submissions()
    print(f"\nFound {len(submissions)} unique accepted submissions\n")

    tag_map = defaultdict(list)
    slug_to_meta = {}

    for i, sub in enumerate(submissions):
        slug = sub["title_slug"]
        print(f"[{i+1}/{len(submissions)}] {slug}")
        meta = fetch_problem_tags(slug)
        if not meta or not meta.get("questionFrontendId"):
            print(f"  Skipping {slug} (no data)")
            continue
        slug_to_meta[slug] = meta
        for tag in meta.get("topicTags", []):
            tag_map[tag["name"]].append(slug)
        time.sleep(0.5)

    print(f"\nGenerating README with {len(slug_to_meta)} problems across {len(tag_map)} topics...")
    readme = generate_readme(tag_map, slug_to_meta, repo_url)
    
    with open("README.md", "w") as f:
        f.write(readme)
    print("README.md updated successfully!")

if __name__ == "__main__":
    main()
