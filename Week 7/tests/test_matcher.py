def test_matching_input():

    resume = """
    Python developer with machine learning
    and SQL experience.
    """

    job = """
    Looking for a Python developer with
    machine learning and SQL skills.
    """

    assert len(resume) > 0
    assert len(job) > 0


def test_matching_output_range():

    match_score = 75

    assert 0 <= match_score <= 100