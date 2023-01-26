# My Habit Tracking App / Project
The project habit tracker is about setting up a backend
application system which allows the user to manage and analyse habits. 
In this application the user can create, edit and delete certain habits,
that he/she wants to track over time on a daily or weekly basis. 
Furthermore the user can analyse its habits. For the start there are five
predefined habits (4 daily, 1 weekly) with four weeks tracking data. The 
predefined data can be loaded in to the application separately. 
The tracking data contains entries of every completed task included the 
date. If a habit was not completed there is no entry at that day.


## Installation

For installing all necessary packages for running the app, click on the 
following "install requirements.txt" command:

````shell
pip install -r requirements.txt
````

## Usage

To use the application click on the following link: 
````shell
python main.py 
````

or the enter the command into terminal. 
A questionary as Command Line Interface is set up to guide the user 
through the application. Using the arrow keys 
and pressing enter the implemented actions can be carried out. 
After using one of the managing functions (create, edit, delete or 
load predefined data) the 
program has to be closed via "Exit" and restarted for the new, edited, 
deleted or uploaded habit data to be updated. 
A completed task can only be updated once a day. Otherwise there could be
more than one entry a day. For analysing your habits use on of the 
defined methods.

## Tests

A test_project.py module is set up for testing the functions 
implemented into the app. There it is tested if the methods for 
managing and analysing the habits is running without any bugs. 
For testing the application use the following pytest command:
````shell
pytest . 
````
