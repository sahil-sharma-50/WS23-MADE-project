# Methods of Advanced Data Engineering Project

This project provides some structure for my open data project in the MADE module at FAU.
This repository contains (a) a data science project that was developed by me over the course of the semester, and (b) the exercises that are submitted over the course of the semester.
Before you begin, make sure you have [Python](https://www.python.org/) and [Jayvee](https://github.com/jvalue/jayvee) installed. We will work with [Jupyter notebooks](https://jupyter.org/). The easiest way to do so is to set up [VSCode](https://code.visualstudio.com/) with the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).


## Project Work: Analyze different weather conditions and their impact on different types of vehicles involved in road accidents.
This project aims to figure out how weather influences road safety, especially if the weather conditions affect the types of vehicles involved in an accident, which is super important for creating better safety rules. It checks out how different weather conditions relate to the number of accidents. It looks at accident data from Berlin to see how these weather conditions impact the number of accidents.<br><br>
This project aims to investigate the following aspects:
<ol>
	<li>Which road condition has the most impact on road accidents?</li>
	<li>Which type of vehicle is most likely to be involved in an accident?</li>
	<li>How do different weather conditions impact the types of vehicles involved in accidents?</li>
	<li>Is there any trend in vehicle accidents over the period of a year?</li>
</ol>

All project work is **present** in the `project` folder.

### Insights of the Project:
1. **Comprehensive Analysis Report: [report.ipynb](https://github.com/sahil-sharma-50/WS23-MADE-project/blob/main/project/report.ipynb)**
2. **Presentation Slides: [slides.pdf](https://github.com/sahil-sharma-50/WS23-MADE-project/blob/main/project/slides.pdf)**
3. **Presentation Video: [presentation-video.mp4](https://www.python.org/)**

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to html: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises, sometimes using [Python](https://www.python.org/), sometimes using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.<jv or py>`.

In regular intervalls, exercises will be given as homework to complete during the semester. We will divide you into two groups, one completing an exercise in Jayvee, the other in Python, switching each exercise. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv` or `./exercises/exercise1.py`
2. `./exercises/exercise2.jv` or `./exercises/exercise2.py`
3. `./exercises/exercise3.jv` or `./exercises/exercise3.py`
4. `./exercises/exercise4.jv` or `./exercises/exercise4.py`
5. `./exercises/exercise5.jv` or `./exercises/exercise5.py`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
