# recruitment-anonymisation-engine
Python-based CV and cover letter anonymisation engine for fair recruitment at EduQual

# CV & Cover Letter Anonymisation Engine

This repository contains a work-in-progress Python-based anonymisation engine
designed to support fair, skills-based recruitment.

The tool is intended to:

- Remove personally identifiable information (PII) such as names, email
  addresses, phone numbers, URLs and postcodes from CVs and cover letters.
- Preserve skills, experience, education and achievements so shortlisting can
  focus on merit.
- Integrate with a SharePoint / Power Automate workflow using reference IDs
  (e.g. `REC-2025-001`) to keep candidate packs together (CV + cover letter).

This project was originally developed in the context of my role at EduQual,
but this repository contains only my own generic code and documentation.
No real candidate data or internal documents are included.

## Documentation

The detailed design specification is here:

- [`docs/design-spec.txt`](docs/design-spec.txt)

## Planned technical stack

- Python (3.x)
- `python-docx` (for working with `.docx` files)
- Regular expressions for PII detection (emails, phones, URLs, postcodes)
- Heuristic rules for name and signature-block anonymisation
- Optional integration with:
  - SharePoint document libraries
  - Power Automate flows for intake (email → SharePoint)
