# Automated Resume Screener

## Description

The Automated Resume Screener is a Python-based application that scans resumes in PDF and DOCX formats, extracts their text, compares the content with predefined job-related keywords, and generates a screening report. It helps recruiters quickly identify suitable candidates based on their skills.

## Features

* Reads resumes in PDF and DOCX formats
* Extracts text automatically
* Matches resumes against predefined job keywords
* Calculates a score based on matched skills
* Classifies candidates as Shortlisted or Rejected
* Exports the results to an Excel file

## Technologies Used

* Python
* pdfplumber
* python-docx
* pandas
* openpyxl

## Project Structure

```text
Automated_Resume_Screener/
│── resume_screener.py
│── requirements.txt
│── README.md
│── shortlisted_candidates.xlsx
└── resumes/
    └── resume.docx
```

## Installation

Install the required libraries:

```bash
pip install pdfplumber python-docx pandas openpyxl
```

Or install from the requirements file:

```bash
pip install -r requirements.txt
```

## Usage

1. Place one or more resume files in the `resumes` folder.
2. Run the program:

```bash
python resume_screener.py
```

3. The program will:

   * Read all PDF and DOCX resumes.
   * Compare resume content with predefined keywords.
   * Calculate a matching score.
   * Generate `shortlisted_candidates.xlsx`.

## Sample Output

| Resume      | Score | Matched Skills                | Status      |
| ----------- | ----: | ----------------------------- | ----------- |
| resume.docx |     3 | python, django, communication | Shortlisted |

## Keywords Used

The default keywords are:

* Python
* Django
* SQL
* Machine Learning
* Git
* Communication

These keywords can be modified in the `JOB_KEYWORDS` list inside `resume_screener.py`.

## Future Improvements

* Resume ranking based on percentage
* Graphical User Interface (GUI)
* Job description upload and automatic keyword extraction
* Support for image-based resumes using OCR
* Email notification for shortlisted candidates

