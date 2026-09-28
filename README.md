# Resume Job Matching Platform

A Python-based Resume Job Matching Platform that analyzes resume and job description text, extracts relevant skills, compares them, and generates a basic job matching score.

## Project Overview

Recruiters often need to compare candidate resumes with job descriptions to identify whether a candidate's skills match the requirements of a job.

This project aims to build a basic automated system that can:

- Process resume and job description text
- Extract relevant skills
- Compare candidate skills with job requirements
- Identify matched skills
- Identify missing skills
- Calculate a basic matching percentage
- Maintain the state of resume and job information

The project was developed incrementally over **8 weeks**, covering data processing, machine learning concepts, NLP, conversation state, job matching, validation, testing, and documentation.

---

## Objectives

The main objectives of this project are:

1. Extract useful information from resume text.
2. Identify skills required by a job description.
3. Compare candidate skills with job requirements.
4. Identify skills that match the job.
5. Identify missing skills.
6. Generate a basic job matching score.
7. Build the project using modular Python components.
8. Test and document the complete system.

---

## Key Features

### Resume Skill Extraction

The system identifies predefined technical skills from resume text.

Examples include:

- Python
- Java
- SQL
- JavaScript
- React
- HTML
- CSS
- Machine Learning
- Pandas
- NumPy
- FastAPI
- Git
- GitHub

### Job Skill Extraction

The same skill extraction process is applied to job descriptions to identify required skills.

### Skill Matching

The candidate's skills are compared with the skills required by the job.

The system identifies:

- Matched skills
- Missing skills

### Match Score

A basic matching percentage is calculated using:

```text
Match Score = (Number of Matched Job Skills / Total Job Skills) × 100
```

### Conversation State

The system maintains information such as:

- Resume text
- Job description
- Resume skills
- Job skills
- Matched skills
- Missing skills

---

## System Workflow

```text
                    User
                     |
                     v
            Resume / Job Description
                     |
                     v
               Text Processing
                     |
                     v
               Skill Extraction
                  /       \
                 /         \
                v           v
        Resume Skills    Job Skills
                \           /
                 \         /
                  v       v
                 Skill Matching
                      |
             +--------+--------+
             |                 |
             v                 v
       Matched Skills    Missing Skills
             |
             v
          Match Score
```

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data processing |
| Scikit-learn | Machine learning |
| TF-IDF | Text feature extraction |
| Naive Bayes | Text classification |
| Git | Version control |
| GitHub | Project repository |
| Markdown | Documentation |

---

## Project Structure

```text
Resume-Job-Matching-Platform/
│
├── Week 1/
│   └── Data preprocessing and dataset preparation
│
├── Week 2/
│   └── Linear regression and model evaluation
│
├── Week 3/
│   └── TF-IDF and Naive Bayes
│
├── Week 4/
│   └── Intent design
│
├── Week 5/
│   ├── conversation_state.py
│   ├── resume_parser.py
│   ├── job_matcher.py
│   ├── week5_demo.py
│   └── week5_notes.md
│
├── Week 6/
│   ├── edge_case_handler.py
│   ├── matcher.py
│   ├── test_edge_cases.py
│   ├── text_cleaner.py
│   ├── validators.py
│   └── week6_notes.md
│
├── Week 7/
│   ├── evaluation_dataset.csv
│   ├── evaluate_model.py
│   ├── test_results.csv
│   ├── week7_testing.md
│   ├── final_results.md
│   └── tests/
│
├── Week 8/
│   ├── project_documentation.md
│   ├── system_architecture.md
│   ├── testing_summary.md
│   ├── limitations.md
│   ├── future_scope.md
│   └── week8_summary.md
│
└── README.md
```

---

## 8-Week Development Timeline

### Week 1 — Data Preprocessing

- Introduction to datasets
- Understanding features and labels
- Data cleaning
- Basic data preparation using Pandas

### Week 2 — Machine Learning Basics

- Linear regression
- Train-test splitting
- Model training
- Model evaluation

### Week 3 — Text Classification

- TF-IDF
- Text vectorization
- Naive Bayes
- Basic text classification

### Week 4 — Intent Design

- Identifying user intents
- Designing possible conversation flows
- Preparing the system for user interaction

### Week 5 — Conversation State & Job Matching

- Resume information storage
- Job description storage
- Skill extraction
- Skill comparison
- Matched and missing skill identification
- Basic matching score

### Week 6 — Validation & Edge Cases

- Input validation
- Text cleaning
- Handling unusual inputs
- Testing edge cases

### Week 7 — Testing & Evaluation

- Unit testing
- Evaluation dataset
- Test result analysis
- Model/system evaluation
- Refinement of components

### Week 8 — Final Documentation

- System architecture
- Project documentation
- Testing summary
- Limitations
- Future scope
- Final project organization

---

## How the Matching Works

Suppose a candidate has:

```text
Python
SQL
Pandas
Git
Machine Learning
```

And the job requires:

```text
Python
SQL
React
Java
Git
```

The system identifies:

```text
Matched Skills:
Python
SQL
Git

Missing Skills:
React
Java
```

The matching score is calculated based on the required job skills:

```text
3 matched skills / 5 required skills × 100

= 60%
```

This is a basic skill-based score and does not represent a complete recruitment decision.

---

## Running the Project

### Requirements

Install Python and the required libraries used by the project.

For example:

```bash
pip install pandas scikit-learn
```

### Run the Week 5 Demonstration

Navigate to the Week 5 directory:

```bash
cd "Week 5"
```

Run:

```bash
python week5_demo.py
```

The program displays:

```text
Resume Skills
Job Skills
Matched Skills
Missing Skills
Match Score
Conversation State
```

---

## Testing

The project includes testing and evaluation work in Week 7.

The testing process covers:

- Skill extraction
- Job skill extraction
- Skill matching
- Match score calculation
- Conversation state
- Input validation
- Edge cases

Example cases include:

| Test Case | Expected Result |
|---|---|
| Resume contains a required skill | Skill is matched |
| Resume does not contain a required skill | Skill is marked missing |
| All required skills are present | High matching score |
| No required skills are present | Matching score is 0 |
| Empty input | System handles the input safely |

---

## Limitations

The current version has several limitations:

1. The skill database is predefined.
2. Skill extraction is primarily keyword-based.
3. The matching score is a basic calculation.
4. The system does not fully understand the semantic meaning of text.
5. Years of experience are not currently considered.
6. Education and certifications are not included in the basic score.
7. Resume file upload and advanced document parsing are not part of the current basic implementation.

Therefore, the current matching score should be considered a **basic technical-skill matching indicator**, not a complete hiring recommendation.

---

## Future Scope

The project can be further improved by adding:

### Advanced NLP

Use modern NLP techniques to understand resume and job description text more effectively.

### Semantic Matching

Use embeddings or transformer-based models to identify similar skills even when different words are used.

### Resume Upload

Allow users to upload PDF and DOCX resumes directly.

### Advanced Matching Score

Consider:

- Skills
- Experience
- Education
- Certifications
- Job requirements

### Job Recommendations

Recommend relevant job opportunities based on a candidate's resume.

### Web Application

Convert the project into a complete web application using technologies such as FastAPI and a frontend framework.

### Explainable Matching

Provide explanations showing why a candidate received a particular matching score.

---

## Learning Outcomes

Through this project, the following concepts were explored:

- Python programming
- Data preprocessing
- Machine learning fundamentals
- Train-test splitting
- Model evaluation
- Natural Language Processing
- TF-IDF
- Naive Bayes
- Text processing
- Skill extraction
- Set-based matching
- Input validation
- Edge-case handling
- Software testing
- Git and GitHub
- Technical documentation

---

## Conclusion

The Resume Job Matching Platform demonstrates how text processing, machine learning concepts, and rule-based skill matching can be combined to create a basic automated resume-to-job matching system.

The project was developed incrementally over eight weeks, progressing from data preprocessing and machine learning fundamentals to NLP, skill matching, validation, testing, and final documentation.

The current system provides a foundation that can be extended into a more advanced recruitment-support application using semantic NLP, larger skill databases, document processing, and explainable matching techniques.

---

## Project Status

**Status: Completed — 8 Week Development**

The project has completed its planned development, testing, documentation, and organization stages.