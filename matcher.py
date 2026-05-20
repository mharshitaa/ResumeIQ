from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILLS = [
    "python", "java", "c++", "sql", "mysql",
    "machine learning", "data science",
    "flask", "django", "html", "css", "javascript",
    "react", "node", "git"
]

def extract_skills(text):
    found_skills = []
    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)
    return set(found_skills)

def calculate_match(resume_text, job_text):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    if len(job_skills) == 0:
        return 0

    matched = resume_skills.intersection(job_skills)
    return round((len(matched) / len(job_skills)) * 100, 2)

def final_match_score(resume_text, job_text):
    text_score = calculate_match(resume_text, job_text)
    skill_score = calculate_match(resume_text, job_text)

    return round((0.4 * text_score) + (0.6 * skill_score), 2)