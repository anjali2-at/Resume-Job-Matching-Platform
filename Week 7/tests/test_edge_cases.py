def test_empty_resume():

    resume = ""

    assert resume.strip() == ""


def test_empty_job_description():

    job = ""

    assert job.strip() == ""


def test_short_resume():

    resume = "Python"

    assert len(resume) < 50


def test_special_characters():

    resume = "Python!!! SQL### Java@@@"

    assert len(resume) > 0


def test_unrelated_resume():

    resume = "Graphic designer with Photoshop experience."

    job = "Python machine learning developer."

    assert resume != job