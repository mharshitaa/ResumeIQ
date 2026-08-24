import PyPDF2
import docx
import string
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


def read_pdf(file):
    text = ""
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def read_docx(file):
    doc = docx.Document(file)
    return " ".join([p.text for p in doc.paragraphs])


def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    words = [w for w in words if w not in ENGLISH_STOP_WORDS]
    return " ".join(words)
