from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def match_resumes(jd, resumes):

    texts = [jd]

    for name, resume in resumes:
        texts.append(resume)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)

    jd_vector = vectors[0]

    scores = []

    for i in range(1, len(texts)):

        similarity = cosine_similarity(jd_vector, vectors[i])[0][0]

        scores.append((resumes[i-1][0], similarity))

    scores.sort(key=lambda x: x[1], reverse=True)

    return scores