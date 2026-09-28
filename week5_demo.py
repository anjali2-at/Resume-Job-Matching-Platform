from conversation_state import ConversationState
from resume_parser import extract_skills
from job_matcher import match_skills


resume = """
I am a student with experience in Python, SQL, Pandas and Git.
I have also worked on machine learning projects.
"""

job_description = """
We are looking for a candidate with Python, SQL, React and Java skills.
Git knowledge is also required.
"""


state = ConversationState()

# Store resume and job description
state.update_resume(resume)
state.update_job(job_description)

# Extract skills
resume_skills = extract_skills(resume)
job_skills = extract_skills(job_description)

state.update_resume_skills(resume_skills)
state.update_job_skills(job_skills)

# Match skills
matched, missing, score = match_skills(
    resume_skills,
    job_skills
)

state.set_match_results(matched, missing)

# Display result
print("Resume Skills:")
print(resume_skills)

print("\nJob Skills:")
print(job_skills)

print("\nMatched Skills:")
print(matched)

print("\nMissing Skills:")
print(missing)

print("\nMatch Score:")
print(str(score) + "%")

print("\nConversation State:")
print(state.get_state())