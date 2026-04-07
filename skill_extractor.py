SKILLS = [
    "python",
    "java",
    "javascript",
    "react",
    "node",
    "html",
    "css",
    "sql",
    "machine learning",
    "deep learning",
    "tensorflow",
    "aws",
    "docker",
    "kubernetes",
    "linux",
    "git",
    "github",
    "flask",
    "django",
    "data analysis",
    "power bi",
    "pandas",
    "numpy"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills