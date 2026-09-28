def validate_resume_text(text):
    if text is None:
        return False, "Resume text is missing."

    text = text.strip()

    if len(text) == 0:
        return False, "Resume is empty."

    if len(text) < 50:
        return False, "Resume is too short."

    if not any(char.isalpha() for char in text):
        return False, "Resume does not contain meaningful text."

    return True, "Resume is valid."


def validate_job_description(text):
    if text is None:
        return False, "Job description is missing."

    text = text.strip()

    if len(text) == 0:
        return False, "Job description is empty."

    if len(text) < 50:
        return False, "Job description is too short."

    return True, "Job description is valid."