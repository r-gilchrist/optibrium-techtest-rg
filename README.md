# Optibrium Technical Test - Updates Following the Initial Code Submission

- **Updates by**: *Ryan Gilchrist*
- **Date**: *11th June, 2022*
- [Endpoint specification](https://github.com/optibrium/python_developer_tech_test/blob/main/People.md)
 
### Introduction

Following the submission of my initial solution, I decided to revisit the code a few days later. I uncovered a few things and additions that I thought would be worth changing, as potential talking points.

### Docker

I learned a little bit about Docker after submitting, and thought it would be useful to include a Dockerfile for easier deployment on computers that aren't mine!

This also means that you can build and run the docker image, and then exectute `python -m unittest tests.py` without manually starting the server.

### Additional tests

I realised I hadn't tested any edge cases for POSTing names. So I added not-string, numbers only, numbers/letters combination, and zero-length tests in the POST test class. This uncovered a bug in the code; I was using `isalpha` instead of `isalnum`, so names with numbers weren't able to be submitted.

I also added exit code 411 for where the name wasn't a string in the first place!

Finally, I realised the DELETE request wasn't actually removing a person from the database, and have fixed.

### Security

Authentication tests have been moved to the first step of each function in `app.py` where appropriate. I would assume this is slightly better practice from a security standpoint!

### Minor edits

1. Functions, objects etc. have been made more descriptive where I felt improvements could be made.
2. Pretty much all of my comments could be removed and the user can still understand the code. On the one hand this makes the code more concise, but on the other hand I don't think the comments were doing anything particularly harmful, weren't overly long and so could have been useful to someone. I've left this updated version with minimal commentary to compare styles with the original.
3. Since I'm now using Docker to specify the version of Python, I added a Walrus operator `:=` to make part of the code slightly more concise.
4. One of the tests was broken (incorrectly-specified test - the code was OK). So I fixed the test


