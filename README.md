# A Data-Driven Investigation of Crime and Arrest Disparities

## Main Question:
Which neighborhoods or regions have the highest disparities between crime reports and arrests?

## Description:
In urban areas, disparities between crime reports and arrests can indicate potential issues in law enforcement practices, resource allocation, or systemic biases. This report investigates which neighborhoods or regions have the highest disparities between crime reports and arrests in a specific city. By analyzing these disparities, we aim to highlight areas that may require additional attention or resources from law enforcement agencies

## Data Source:
### Crime Data:
- URL: https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD
- Content: This dataset contains records of reported crimes in Los Angeles, including descriptions, locations, dates, and areas.
- Data Structure: Columns for Crm Cd Desc, Date Rptd, Vict Sex, LOCATION, AREA NAME, DR_NO
- License Information: Open licensed CC0 1.0 Universal

### Arrest Data:
- URL: https://data.lacity.org/api/views/amvf-fr72/rows.csv?accessType=DOWNLOAD
- Content: This dataset includes records of arrests made in Los Angeles, providing details like arrest types, charges, locations, and dates.
- Data Structure: Columns for Charge, Arrest Date, Arrest Type Code, Charge Description, Location, Area Name, Report ID
- License Information: Open licensed CC0 1.0 Universal



# Methods of Advanced Data Engineering Template Project

This template project provides some structure for your open data project in the MADE module at FAU.
This repository contains (a) a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester.

To get started, please follow these steps:
1. Create your own fork of this repository. Feel free to rename the repository right after creation, before you let the teaching instructors know your repository URL. **Do not rename the repository during the semester**.

## Project Work
Your data engineering project will run alongside lectures during the semester. We will ask you to regularly submit project work as milestones, so you can reasonably pace your work. All project work submissions **must** be placed in the `project` folder.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to HTML: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervals, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/).

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions → Exercise Feedback in your repository.

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
