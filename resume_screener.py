import os
import pdfplumber
import docx
import pandas as pd

# Keywords to search for
JOB_KEYWORDS = [
    "python",
    "django",
    "sql",
    "machine learning",
    "git",
    "communication"
]

RESUME_FOLDER = "resumes"

results = []


def extract_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    return text


def extract_docx(path):
    doc = docx.Document(path)
    return " ".join([paragraph.text for paragraph in doc.paragraphs])


for file in os.listdir(RESUME_FOLDER):

    filepath = os.path.join(RESUME_FOLDER, file)

    if file.endswith(".pdf"):
        text = extract_pdf(filepath)

    elif file.endswith(".docx"):
        text = extract_docx(filepath)

    else:
        continue

    text = text.lower()

    matched = []

    for keyword in JOB_KEYWORDS:
        if keyword.lower() in text:
            matched.append(keyword)

    score = len(matched)

    if score >= 3:
        status = "Shortlisted"
    else:
        status = "Rejected"

    results.append({
        "Resume": file,
        "Score": score,
        "Matched Skills": ", ".join(matched),
        "Status": status
    })

df = pd.DataFrame(results)

df.to_excel("shortlisted_candidates.xlsx", index=False)

print(df)
print("\nScreening Complete!")
print("Results saved in shortlisted_candidates.xlsx")