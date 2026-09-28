def match_skills(resume_skills, job_skills):

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched = list(resume_set.intersection(job_set))
    missing = list(job_set - resume_set)

    if len(job_set) > 0:
        score = (len(matched) / len(job_set)) * 100
    else:
        score = 0

    return matched, missing, round(score, 2)