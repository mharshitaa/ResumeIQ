# ResumeIQ – AI Resume Analyzer

ResumeIQ is an AI-powered web application that analyzes resumes and compares them with job descriptions to determine candidate-job compatibility.

The system uses Natural Language Processing (NLP) and Machine Learning techniques to calculate resume matching scores and categorize applicants based on their suitability for a role.

---

## Project Overview

Recruiters often spend a lot of time manually screening resumes. This project automates the process using AI and NLP techniques.

The application accepts resumes in PDF or DOCX format, extracts important information, and compares it with the provided job description using TF-IDF vectorization and cosine similarity.

---

## Features

- Upload resumes in PDF or DOCX format
- Enter custom job descriptions
- Resume-job matching score generation
- Candidate categorization system
- NLP-based text preprocessing
- Clean and responsive user interface
- AI-powered similarity analysis

### Match Categories
- Excellent Match (85% and above)
- Good Match (70% – 84%)
- Average Match (40% – 69%)
- Low Match (Below 40%)

---

## Screenshots

### Home Page
![Home](screenshots/Home.png)

### Resume Upload
![Upload](screenshots/ResumeUpload.png)

### Match Result
![Result](screenshots/Result.png)

---

## Tech Stack

### Frontend
- HTML
- CSS

### Backend
- Python
- Flask

### AI / NLP
- NLTK
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

---

## How It Works

1. User uploads a resume
2. User enters a job description
3. Resume text is extracted and cleaned
4. NLP preprocessing is performed
5. TF-IDF converts text into numerical vectors
6. Cosine similarity calculates the match score
7. Final match percentage is displayed

---


## Project Structure

```text
ResumeIQ/
│
├── app.py
├── matcher.py
├── resume_parser.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── sample_resumes/
├── screenshots/
└── README.md

```

## How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/mharshitaa/ResumeIQ.git
cd ResumeIQ
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

### 4. Open in Browser

```bash
http://127.0.0.1:5000
```


## Use Cases

- Resume screening for recruiters and HR teams
- ATS-style candidate shortlisting
- Resume optimization and job matching analysis
- Learning project for NLP and ML beginners

---

## What I Learned

- Text extraction from PDF and DOCX files
- Natural Language Processing using NLTK
- Feature extraction using TF-IDF
- Similarity measurement using Cosine Similarity
- Flask backend development
- Frontend-backend integration

---

## Future Improvements

- Skill gap analysis and missing skill detection
- Resume ranking system for multiple candidates
- Advanced NLP models (Word2Vec, BERT)
- Database integration for resume storage
- Cloud deployment using AWS, Render, or Vercel

---

## Limitations

- Matching is based mainly on textual similarity
- Does not currently detect hidden or inferred skills
- Resume formatting can affect extraction accuracy
- Limited support for advanced resume templates

---

## Conclusion

This project demonstrates how Artificial Intelligence and Natural Language Processing can automate resume screening and candidate evaluation. It combines machine learning concepts with full-stack web development to create a practical recruitment assistance tool.

---

## Author

Harshita Manchanda
