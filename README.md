# Interview Patterns
[![Build Status](https://app.travis-ci.com/patchneranartkomol/InterviewPatterns.svg?branch=main)](https://app.travis-ci.com/patchneranartkomol/InterviewPatterns)

This is a list of implementations of data structures, algorithms, and solutions to problems using those building blocks. There are many lists and resources out there, and this one is no different.

Hopefully, this list serves as a demonstration of learning psychology. The purpose of this list is to created and refined, but not to be reviewed, except as an outline, to help create a hierarchical structure of relevant concepts.

## Running Examples
For now, there are Python3 examples in each subfolder, pertaining to a topic. There's no libraries to install, so as long as you have Python3 installed, you can run any of them code samples.

To run all tests in the repo:
```
python -m unittest discover -p "*.py"
```

To run all tests in a directory:
```
python -m unittest arrays-and-hashing
```

To run a single module:
```
python -m unittest arrays-and-hashing.contains_duplicate
```

To run a single test case:
```
python -m unittest arrays-and-hashing.contains_duplicate.TestSolution.test_contains_duplicates
```

## Linting
Using [yapf](https://github.com/google/yapf) for formatting. To install for this project, create and activate a virtual env.
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then run the linter over a file or recursively over a folder of choice.
```
yapf -i [file.py]
yapf -ir [folder]
```

TODO: Add a pre-commit hook to run the linter.

## Addendum on Learning
In some models of learning psychology, there are 3 stages of memory processing - encoding, storage, and retrieval.

Effective encoding is the key to storing and working information effectively.

Reading and reviewing solutions, on their own, is not enough. One must implement from the leaner's perspective, explain from the teacher's perspective, and engage in deep processing to effectively encode concepts.

Tools like spaced repetition, reviewing the concepts one would like to learn, at regular intervals, ensures that knowledge leads to deeper understanding over time, and minimizing the forgetting our minds often do.

When retrieving this information learned in previous sessions, it tends to be better remembered when one generates it independently, instead of through passively reviewing notes.

References - [Make it Stick: How Intentional Usage of Encoding Strategies by Students and Instructors Can Improve Learning and Memory](https://www.psychologyinaction.org/psychology-in-action-1/2021/12/12/make-it-stick-how-intentional-usage-of-encoding-strategies-by-students-and-instructors-can-improve-learning-and-memory)
