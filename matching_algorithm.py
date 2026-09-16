from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Read resume
with open("resume.txt", "r") as file:
    resume = file.read()


# Read job description
with open("job_description.txt", "r") as file:
    job_description = file.read()


print("========== RESUME ==========")
print(resume)

print("\n========== JOB DESCRIPTION ==========")
print(job_description)


# Create embeddings using TF-IDF
vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform([
    resume,
    job_description
])


# Calculate cosine similarity
similarity_score = cosine_similarity(
    vectors[0],
    vectors[1]
)[0][0]


# Convert to percentage
match_percentage = similarity_score * 100


print("\n========== MATCHING RESULT ==========")

print("Similarity Score:", round(similarity_score, 2))

print("Match Percentage:", round(match_percentage, 2), "%")


# Match result
if match_percentage >= 70:
    print("\nResult: Good Match")
elif match_percentage >= 40:
    print("\nResult: Moderate Match")
else:
    print("\nResult: Low Match")