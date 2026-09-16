# Week 5 - Embeddings and Cosine Similarity

## Project

Resume Job Matching Platform

## Learn

This week I learned:

- Text Embeddings
- Cosine Similarity
- Text Vectorization
- Resume and Job Description Matching

## Build

Built a Resume and Job Description Matching Algorithm.

---

## 1. Embeddings

Embeddings convert text into numerical representations.

Machine learning algorithms cannot directly understand text.

Therefore, text is converted into numerical vectors.

In this project, TF-IDF Vectorizer is used to convert the resume and job description into numerical vectors.

## 2. TF-IDF Vectorization

TF-IDF converts text data into numerical feature vectors.

```python
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([
    resume,
    job_description
])