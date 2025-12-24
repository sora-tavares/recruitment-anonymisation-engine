# Email Intake and Routing Flow (Phase 1)

This document describes the email intake and routing logic that prepares recruitment documents for anonymisation.

The intake process is implemented using Power Automate and a shared recruitment mailbox. It is designed to enforce document format rules, create a clear audit trail, and hand off valid documents to the anonymisation engine.

---

## Trigger

The flow is triggered when a new email arrives in the recruitment mailbox folder:

- `Inbox > 1.Rec > Applications`

Only emails with attachments are processed.

---

## Attachment handling

When an email is received, attachments are evaluated in the following way:

- Inline images and email signature assets are ignored.
- Only “real” attachments are considered for further processing.

Attachments are then classified by file extension:

- **DOCX** files are accepted.
- **PDF** files cause the application to be rejected.

---

## Decision logic

### PDF present
If one or more PDF files are detected:

- The application is rejected.
- A standard response is sent to the sender requesting DOCX format.
- The email is moved to the mailbox folder: `Rejected - PDF`.
- No files are forwarded for anonymisation.

This applies even if the email also contains DOCX files. Mixed submissions are rejected to enforce consistent intake rules.

---

### DOCX only
If the email contains only DOCX attachments:

- Each DOCX file is saved to the SharePoint folder:
  - `Recruitment/1_To_Anonymise`
- A tracker entry is created for each file.
- The email is moved to the mailbox folder:
  - `To anonymise`

---

## Tracker behaviour

The tracker records one row per DOCX file. Fields include:

- A shared reference ID (per email)
- A document sequence number (per file)
- Original filename
- Sender email and subject
- Date received
- File type label (CV / CL / Other)
- Processing status

File type labels are based on filename heuristics only.

---

## Status model

Tracker status reflects the **document lifecycle**:

- **Incoming**: recorded at intake
- **To Anonymise**: file saved to the anonymisation input folder
- **Done**: anonymised version created
- **Archived**: original file archived after successful anonymisation

Mailbox folders are used only for operational visibility.

---

## Design principles

- Intake must be deterministic and auditable.
- Document processing must not depend on filenames or user behaviour.
- Anonymisation should operate on all DOCX files placed in the input folder.
- No personally identifiable information is exposed beyond intake.

---

## Next phase

Phase 2 will introduce a Python-based anonymisation process that monitors the `1_To_Anonymise` folder, produces anonymised outputs, updates tracker status, and archives originals.
