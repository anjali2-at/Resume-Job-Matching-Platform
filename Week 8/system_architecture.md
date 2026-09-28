# System Architecture

## Overall Architecture

The Resume Job Matching Platform follows a simple modular architecture.

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
  |
  v
Skill Matching
  |
  +------------------+
  |                  |
  v                  v
Matched Skills    Missing Skills
  |
  v
Match Score