def test_resume_text_exists():

    resume_text = """
    Python developer with experience in
    machine learning and SQL.
    """

    assert resume_text.strip() != ""


def test_resume_contains_text():

    resume_text = "Python Developer"

    assert len(resume_text) > 0