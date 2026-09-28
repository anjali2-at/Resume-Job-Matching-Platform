from app.services.edge_case_handler import (
    validate_resume_text,
    validate_job_description
)


def test_empty_resume():
    valid, message = validate_resume_text("")

    assert valid is False


def test_none_resume():
    valid, message = validate_resume_text(None)

    assert valid is False


def test_short_resume():
    valid, message = validate_resume_text("Python developer")

    assert valid is False


def test_valid_resume():
    resume = """
    Python developer with experience in machine learning,
    SQL, FastAPI and data analysis.
    """

    valid, message = validate_resume_text(resume)

    assert valid is True


def test_empty_job():
    valid, message = validate_job_description("")

    assert valid is False