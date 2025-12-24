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

## Current status (December 2025)

This project is being developed in phases.

### Phase 1: Email intake and routing (Complete)
A Power Automate intake pipeline is in place to support the anonymisation engine. This phase:

- Monitors a shared recruitment mailbox
- Accepts applications submitted as Microsoft Word (.docx) files and returns a receipt confirmation email
- Automatically rejects PDF submissions with a standard response
- Logs each received document in a tracker with a shared reference ID
- Routes valid documents into a SharePoint folder for anonymisation

This phase is intentionally filename-agnostic. Documents may be labelled as CV, cover letter, or "Other" based on heuristics, but **all DOCX files are passed forward for anonymisation** to avoid accidental exclusion.

### Phase 2: Python anonymisation engine (In progress)
The Python anonymisation engine will process documents placed in the anonymisation input folder, generate anonymised outputs, and archive originals once processing is complete.

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
