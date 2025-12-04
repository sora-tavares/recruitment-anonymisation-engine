"""
anonymise.py

Main entry point for my CV and Cover Letter anonymisation engine.

This script is designed to work with:
- A SharePoint-style folder structure (0_Incoming_From_Email, 1_To_Anonymise,
  2_Anonymised, etc.)
- An Excel tracker table (tblRecruitmentTracker) that stores RefID, FileType
  and metadata.

Core responsibilities:
- Discover files to anonymise in 1_To_Anonymise.
- Parse RefID and FileType from filenames.
- Extract name tokens using metadata (filename, sender email).
- Apply the appropriate anonymisation pipeline (CV or Cover Letter).
- Save anonymised documents into 2_Anonymised.
- Update the tracker when appropriate (planned for a later version).
"""

from pathlib import Path
from dataclasses import dataclass
from typing import List, Set, Optional, Tuple

# Dependency: python-docx (pip install python-docx)
# from docx import Document


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

@dataclass
class FileContext:
    """
    Represents the context I need to anonymise a single document file.
    """

    path: Path
    ref_id: str
    file_type: str  # expected values: "CV", "CL", or "Other"
    original_filename: Optional[str] = None
    sender_email: Optional[str] = None


# ---------------------------------------------------------------------------
# High level workflow
# ---------------------------------------------------------------------------

def discover_files_to_anonymise(base_folder: Path) -> List[FileContext]:
    """
    Scan the 1_To_Anonymise folder and return a list of FileContext objects.

    Filenames are expected to follow the pattern:
        REC-YYYY-NNN_CV.docx
        REC-YYYY-NNN_CL.docx
        REC-YYYY-NNN_OTHER.docx

    This function only prepares metadata; it does not modify any files yet.
    """
    # TODO: implement file discovery and parsing of ref_id and file_type
    return []


def extract_name_tokens(original_filename: Optional[str],
                        sender_email: Optional[str]) -> Set[str]:
    """
    Build a set of candidate name tokens based on:
    - The original filename (e.g. 'Jane_Doe_CV.docx')
    - The sender email (e.g. 'jane.doe@example.com')

    The returned set might look like:
        {"jane", "doe", "jane doe"}

    I will implement this exactly according to my design specification.
    """
    # TODO: implement token extraction according to the design spec
    return set()


def anonymise_cv_text(text_lines: List[str],
                      name_tokens: Set[str]) -> List[str]:
    """
    Apply the CV anonymisation pipeline to a list of text lines.

    Steps will follow my design specification:
    - Remove PII (emails, phones, URLs, postcodes).
    - Replace name tokens.
    - Handle header name/address lines if needed.
    - Preserve skills, experience and education content.
    """
    # TODO: implement CV anonymisation pipeline
    return text_lines


def anonymise_cover_letter_text(text_lines: List[str],
                                name_tokens: Set[str]) -> List[str]:
    """
    Apply the Cover Letter anonymisation pipeline.

    Steps will follow my design specification:
    - Identify header, body and signature zones.
    - Remove name/contact lines in the header zone.
    - Preserve the greeting.
    - Remove signature block after the sign-off phrase.
    - Replace name tokens and PII throughout the body.
    """
    # TODO: implement Cover Letter anonymisation pipeline
    return text_lines


# ---------------------------------------------------------------------------
# Helpers for loading and saving .docx text
# ---------------------------------------------------------------------------

def load_docx_as_lines(path: Path) -> List[str]:
    """
    Load a .docx file and return its content as a list of lines.

    This is a placeholder for now. I will later use python-docx to read
    paragraphs from the document.
    """
    # TODO: implement using python-docx
    raise NotImplementedError("load_docx_as_lines is not implemented yet")


def save_lines_to_docx(lines: List[str], output_path: Path) -> None:
    """
    Save a list of lines into a new .docx file at output_path.

    This is a placeholder for now. I will later use python-docx to create
    a new Document and add each line as a paragraph.
    """
    # TODO: implement using python-docx
    raise NotImplementedError("save_lines_to_docx is not implemented yet")


# ---------------------------------------------------------------------------
# Main processing function
# ---------------------------------------------------------------------------

def process_file(context: FileContext,
                 incoming_root: Path,
                 anonymised_root: Path) -> None:
    """
    Process a single file given its FileContext.

    - Load the .docx content into a list of lines.
    - Build name_tokens using original_filename and sender_email.
    - Apply the CV or CL anonymisation pipeline depending on file_type.
    - Save the anonymised version with the _Anon suffix.
    """
    # TODO: implement my main per-file logic
    raise NotImplementedError("process_file is not implemented yet")


def main() -> None:
    """
    Entry point for running my anonymisation engine locally.

    Example usage:
        python anonymise.py

    Folder paths might look like:
        base = Path(r"C:/Recruitment")
        to_anonymise = base / "1_To_Anonymise"
        anonymised = base / "2_Anonymised"

    In a future version I may use a config file or environment variables
    to make these paths more flexible.
    """
    # TODO: wire up folder paths and call discover_files_to_anonymise,
    # then call process_file for each FileContext.
    pass


if __name__ == "__main__":
    main()
