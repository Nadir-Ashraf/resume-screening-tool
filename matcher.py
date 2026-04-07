from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def rank_resumes(job_description, resumes):

    documents = [job_description]

    for r in resumes:
        documents.append(r["text"])

    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform(documents)

    jd_vector = vectors[0]

    scores = []

    for i in range(1, vectors.shape[0]):   # FIXED HERE

        similarity = cosine_similarity(jd_vector, vectors[i])[0][0]

        scores.append({
            "resume": resumes[i-1]["name"],
            "score": round(float(similarity), 3)
        })

    scores.sort(key=lambda x: x["score"], reverse=True)

    return scores