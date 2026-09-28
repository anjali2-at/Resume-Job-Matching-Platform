def safe_match(resume_text, job_text, matching_function):

    if not resume_text or not resume_text.strip():
        return {
            "success": False,
            "message": "Resume is empty."
        }

    if not job_text or not job_text.strip():
        return {
            "success": False,
            "message": "Job description is empty."
        }

    try:
        score = matching_function(resume_text, job_text)

        return {
            "success": True,
            "score": score
        }

    except Exception as error:
        return {
            "success": False,
            "message": "Unable to calculate match.",
            "error": str(error)
        }