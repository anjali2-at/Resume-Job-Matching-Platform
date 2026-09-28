# Resume Job Matching Platform - Project Documentation

## 1. Project Overview

The Resume Job Matching Platform is a system that compares a
candidate's resume with a job description and identifies relevant
skills.

The system extracts skills from both the resume and job description,
compares them, and calculates a basic matching score.

## 2. Main Objectives

- Extract skills from resumes.
- Extract required skills from job descriptions.
- Compare candidate skills with job requirements.
- Identify matched skills.
- Identify missing skills.
- Calculate a job matching score.
- Maintain conversation and matching state.

## 3. Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF
- Naive Bayes
- Git
- GitHub

## 4. Main Components

### Resume Parser

Extracts known skills from resume text.

### Job Matcher

Compares resume skills with job requirements.

### Conversation State

Stores resume information, job information, extracted skills,
matched skills and missing skills.

### Machine Learning Components

Earlier project weeks explored data preprocessing, regression,
TF-IDF and Naive Bayes concepts.

## 5. Working Flow

Resume
↓
Text Processing
↓
Skill Extraction
↓
Job Description
↓
Job Skill Extraction
↓
Skill Comparison
↓
Matched Skills + Missing Skills
↓
Match Score

## 6. Output

The system provides:

- Resume skills
- Required job skills
- Matched skills
- Missing skills
- Matching percentage