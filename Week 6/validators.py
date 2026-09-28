ALLOWED_EXTENSIONS = [".txt", ".pdf", ".docx"]


def validate_file_extension(filename):
    filename = filename.lower()

    for extension in ALLOWED_EXTENSIONS:
        if filename.endswith(extension):
            return True

    return False


def validate_file_size(size_in_bytes, max_size=5 * 1024 * 1024):
    return size_in_bytes <= max_size