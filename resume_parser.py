def extract_skills(text):

    skills_database = [
        "python",
        "java",
        "sql",
        "javascript",
        "react",
        "html",
        "css",
        "machine learning",
        "pandas",
        "numpy",
        "fastapi",
        "git",
        "github"
    ]

    text = text.lower()

    found_skills = []

    for skill in skills_database:
        if skill in text:
            found_skills.append(skill)

    return found_skills