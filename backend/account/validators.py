import os

def validate_file_extension(name):
    isValid = True

    ext = os.path.splitext(name)[1]
    validate_extension = ['.pdf']

    if not ext.lower() in validate_extension:
        isValid = False

    return isValid