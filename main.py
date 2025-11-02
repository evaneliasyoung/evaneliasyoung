#!/usr/bin/env python3

from shields import Badge

SOCIALS: list[tuple[str, Badge, str]] = [
    (
        "LinkedIn",
        Badge(
            "evaneliasyoung",
            "0A66C2",
            logo="linkedin-white",
            logo_color="fff",
            host="https://custom-icon-badges.demolab.com/badge/",
        ),
        "https://www.linkedin.com/in/evaneliasyoung/",
    ),
    (
        "Instagram",
        Badge("evaneliasyoung", "E4405F", logo="instagram", logo_color="fff"),
        "https://instagram.com/evaneliasyoung",
    ),
    (
        "X",
        Badge("evaneliasyoung", "000", logo="x", logo_color="fff"),
        "https://twitter.com/evaneliasyoung",
    ),
    (
        "Threads",
        Badge("evaneliasyoung", "000", logo="threads", logo_color="fff"),
        "https://www.threads.net/@evaneliasyoung",
    ),
    (
        "Bluesky",
        Badge("eyoung.dev", "0285FF", logo="bluesky", logo_color="fff"),
        "https://bsky.app/profile/eyoung.dev",
    ),
]

LANGS: list[tuple[str, Badge]] = [
    ("Python", Badge("Python", "3776AB", logo="python", logo_color="fff")),
    ("C", Badge("C", "00599C", logo="c", logo_color="fff")),
    ("C++", Badge("C%2b%2b", "00599C", logo="c%2b%2b", logo_color="fff")),
    ("C#", Badge("C%23", "239120", logo="csharp", logo_color="fff")),
    ("JavaScript", Badge("JavaScript", "F7DF1E", logo="javascript", logo_color="000")),
    ("TypeScript", Badge("TypeScript", "3178C6", logo="typescript", logo_color="fff")),
    ("Go", Badge("Go", "00ADD8", logo="go", logo_color="fff")),
    ("Zig", Badge("Zig", "F7A41D", logo="zig", logo_color="fff")),
]

FRAMEWORKS: list[tuple[str, Badge]] = [
    ("HTML", Badge("HTML", "E34F26", logo="html5", logo_color="fff")),
    ("CSS3", Badge("CSS3", "1572B6", logo="css3")),
    ("Bootstrap", Badge("Bootstrap", "4C3E60", logo="bootstrap", logo_color="fff")),
    ("Angular", Badge("Angular", "DD0031", logo="angular")),
    ("Vue", Badge("Vue", "4FC08D", logo="vuedotjs", logo_color="fff")),
    ("Lit", Badge("Lit", "324FFF", logo="lit")),
    ("Svelte", Badge("Svelte", "F1413D", logo="svelte", logo_color="fff")),
]

OTHER = [
    ("MongoDB", Badge("MongoDB", "4EA94B", logo="mongodb", logo_color="fff")),
    ("Redis", Badge("Redis", "DD0031", logo="Redis", logo_color="fff")),
    ("MySQL", Badge("MySQL", "4479A1", logo="mysql", logo_color="fff")),
    ("Git", Badge("Git", "F05032", logo="git", logo_color="fff")),
    ("GitHub", Badge("GitHub", "121011", logo="github", logo_color="fff")),
    ("GitLab", Badge("GitLab", "FC6D26", logo="gitlab", logo_color="fff")),
    ("Bun", Badge("Bun", "14151A", logo="bun", logo_color="fff")),
]


def main() -> None:
    for title, badge, url in SOCIALS:
        print(f"[![{title}]({badge})]({url})")
    print()

    for badge_set in [LANGS, FRAMEWORKS, OTHER]:
        for title, badge in badge_set:
            print(f"![{title}]({badge})")
        print()


if __name__ == "__main__":
    main()
