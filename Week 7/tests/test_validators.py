def test_valid_pdf():

    filename = "resume.pdf"

    assert filename.endswith(".pdf")


def test_valid_docx():

    filename = "resume.docx"

    assert filename.endswith(".docx")


def test_invalid_file():

    filename = "resume.exe"

    assert not filename.endswith((".pdf", ".docx", ".txt"))


def test_file_size():

    file_size = 1024

    maximum_size = 5 * 1024 * 1024

    assert file_size <= maximum_size