from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from skill_extractor import extract_skills

model = SentenceTransformer("all-MiniLM-L6-v2")


def rank_resumes(job_description, resumes):

    jd_embedding = model.encode(job_description)

    jd_skills = extract_skills(job_description)

    results = []

    for resume in resumes:

        resume_embedding = model.encode(resume["text"])

        similarity = cosine_similarity(
            [jd_embedding],
            [resume_embedding]
        )[0][0]

        resume_skills = extract_skills(resume["text"])

        matched_skills = list(set(jd_skills) & set(resume_skills))

        results.append({
            "resume": resume["name"],
            "score": round(float(similarity),3),
            "skills": resume_skills,
            "matched": matched_skills
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results