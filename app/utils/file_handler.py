from fastapi import UploadFile
from models.soldier import Soldier
import csv
import io


def upload_csv(file: UploadFile):
    # is the file a CSV
    if file.content_type != "text/csv":
        return {"error": "File must be a CSV"}

    # Read file bytes
    content = file.file.read().decode("utf-8")

    # Parse CSV
    reader = csv.reader(io.StringIO(content))
    header = next(reader)
    return header, list(reader)