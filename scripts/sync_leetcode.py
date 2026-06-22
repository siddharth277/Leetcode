import requests
import json
import os
import time
from collections import defaultdict

USERNAME = os.environ.get("LEETCODE_USERNAME")
SESSION = os.environ.get("LEETCODE_SESSION")
CSRF = os.environ.get("LEETCODE_CSRF_TOKEN")

headers = {
    "Cookie": f"LEETCODE_SESSION={SESSION}; csrftoken={CSRF}",
    "x-csrftoken": CSRF,
    "Referer": "https://leetcode.com",
    "Content-Type": "application/json",
}

def fetch_all_submissions():
    submissions = []
    offset = 0
    limit = 20
    while True:
        url = f"https://leetcode.com/api/submissions/?offset={offset}&limit={limit}"
        res = requests.get(url, headers=headers)
        data = res.json()
        batch = data.get("submissions_dump", [])
        if not batch:
            break
        # Only keep accepted
        accepted = [s for s in batch if s["status_display"] == "Accepted"]
        submissions.extend(accepted)
        if not data.get("has_next"):
            break
        offset += limit
        time.sleep(1)  # Be polite to LeetCode's servers
    # Deduplicate by title_slug
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
    res = requests.post(
        "https://leetcode.com/graphql",
        headers=headers,
        json={"query": query, "variables": {"titleSlug": title_slug}},
    )
    data = res.json().get("data", {}).get("question", {})
    return data

def generate_readme(tag_map, slug_to_meta):
    lines = ["# LeetCode\n~Leetcode Solutions\n\n<!---LeetCode Topics Start-->\n# LeetCode Topics"]
    for tag in sorted(tag_map.keys()):
        lines.append(f"## {tag}")
        lines.append("|  |")
        lines.append("| ------- |")
        for slug in sorted(tag_map[tag]):
            meta = slug_to_meta[slug]
            fid = meta["questionFrontendId"].zfill(4)
            title = meta["title"]
            lines.append(f"| [{fid}-{slug}](https://github.com/YOUR_USERNAME/YOUR_REPO/tree/master/{fid}-{slug}) |")
        lines.append("")
    lines.append("<!---LeetCode Topics End-->")
    return "\n".join(lines)

def main():
    print("Fetching submissions...")
    submissions = fetch_all_submissions()
    print(f"Found {len(submissions)} unique accepted submissions")

    tag_map = defaultdict(list)
    slug_to_meta = {}

    for i, sub in enumerate(submissions):
        slug = sub["title_slug"]
        print(f"[{i+1}/{len(submissions)}] Fetching tags for: {slug}")
        meta = fetch_problem_tags(slug)
        if not meta:
            continue
        slug_to_meta[slug] = meta
        for tag in meta.get("topicTags", []):
            tag_map[tag["name"]].append(slug)
        time.sleep(0.5)

    readme = generate_readme(tag_map, slug_to_meta)
    with open("README.md", "w") as f:
        f.write(readme)
    print("README.md updated!")

if __name__ == "__main__":
    main()
