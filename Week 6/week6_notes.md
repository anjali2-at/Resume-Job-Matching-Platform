# Week 6 - Edge Case Handling

## Objective
Improve system reliability by handling invalid,
incomplete and unusual resume/job inputs.

## Edge Cases Tested

1. Empty resume
2. Empty job description
3. Very short resume
4. Resume without skills
5. Duplicate skills
6. Special characters
7. Unrelated resume
8. Unsupported file type
9. Large file
10. Invalid file

## Expected Result

The system should not crash for invalid input.
It should return a meaningful message to the user.

## Outcome

Edge-case validation and error handling were added
to the resume-job matching pipeline.