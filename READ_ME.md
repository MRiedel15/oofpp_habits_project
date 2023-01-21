# My Habit Tracking App / Project
The project habit tracker is about setting up a backend
application system which allows the user to manage and analyse habits. 
In this application the user can create, edit and delete certain habits,
that he/she wants to track over time on a daily or weekly basis. 
A further function of the application is the analysing of their habits.


## Installation


```
pip install -r requirements.txt
```




## Usage

To use the application enter 
```
python main.py 
```
into terminal command line. A questionary as Command Line Interface is 
set up to guide the user through the application. Using the arrow keys 
and pressing enter the implemented actions can be carried out. 
After using one of the managing functions (create, edit or delete) the 
program as to be closed via "Exit" and restarted for the new, edited or 
deleted habit to be updated. A predefined habit cannot be edited or 
deleted because its values are written into the creation of the database. 
So with every restarted the database will reset for the predefined habits.
A completed task can only be updated once a day. Otherwise there could be
more than one entry a day. For analysing your habits use on of the 
defined methods.

