from pathlib import Path
from anonymiser.anonymise import load_docx_as_lines

test_path = Path("test_files/Dummy_CV.docx")

lines = load_docx_as_lines(test_path)

for i, line in enumerate(lines, start=1):
    print(f"{i:02}: {line}")
