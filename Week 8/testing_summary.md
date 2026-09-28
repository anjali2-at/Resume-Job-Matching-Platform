
---

## 3. `testing_summary.md`

```markdown
# Testing Summary

## Objective

Testing was performed to verify that the main components of the
Resume Job Matching Platform work correctly.

## Components Tested

- Resume skill extraction
- Job skill extraction
- Skill matching
- Match score calculation
- Conversation state
- Input validation
- Edge cases

## Basic Test Cases

| Test Case | Expected Result |
|-----------|-----------------|
| Resume contains required skill | Skill is matched |
| Resume does not contain required skill | Skill is marked missing |
| Resume contains multiple skills | All known skills are extracted |
| Job description contains multiple skills | Required skills are extracted |
| Resume and job have no common skills | Match score is 0 |
| Resume and job have all common skills | Match score is 100 |
| Empty skill list | System does not crash |

## Result

The main components were tested using normal inputs and edge cases.

The system successfully performs basic resume-to-job skill matching.