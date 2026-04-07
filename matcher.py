from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def rank_resumes(job_description, resumes):

    jd_embedding = model.encode(job_description)

    scores = []

    for resume in resumes:

        resume_embedding = model.encode(resume["text"])

        similarity = cosine_similarity(
            [jd_embedding],
            [resume_embedding]
        )[0][0]

        scores.append({
            "resume": resume["name"],
            "score": round(float(similarity), 3)
        })

    scores.sort(key=lambda x: x["score"], reverse=True)

    return scores