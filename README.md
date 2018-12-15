# VS-Data-Science-and-Machine-Learning

Welcome to the Venture Sky's Data Science and Machine Learning course. Join the gitter lobby to stay updated on what is going on:
https://gitter.im/VS-Data-Science-and-Machine-Learning/Lobby


Following is the link for Data Science Syllabus course: http://bit.ly/2rAPWSl

Following is the link for Machine Learning Syllabus course: http://bit.ly/2QuyuxE


The course will be completed in lesser number of classes than shown in the curriculum and that would be decided as per need of students and pace which will get set from first class onwards.

There will be workshops and doubt clearing sessions during weekdays. In these workshops, you can provide a small use case for your lessons and we will implement that using Python or solve some sort of problem that you might face in your student/professional/personal life.

## DS lesson 1: Introduction to Python
The first lesson would be dedicated to python and everything useful it can do for us. We will try to explore as many realms of this language as possible. This will lay the foundation for the first workshop, details of which are provided down below. It would be a fast paced lesson since many students are already familiar with at least some coding language.

Main focus would be to get a native feel of Python and become comfortable with the syntax. Some small nuances and code writing style will also be discussed.


## Workshop 1 for DS: IMS Notices Automatic Notification System
In this workshop, we will first collect email ids of all students interested in a google sheet. We will create a python script that scrapes notices from IMS notice board and if there is a unique entry (new notice not seen before), then a notification along with contents of notice is sent to all the email ids. Then we will deploy this application on a AWS backend (it can be any VPS service). We will run a cron job (scheduled task) that runs this script every day.

This entire thing should be concluded in a matter of 4 hours.

I will host the backend on AWS. It can be hosted on Heroku or Digital Ocean or any other VPS. I will use SendGrid API for mailing the unique notices. If you guys feel that there is some aspect of this stack that you would like to explore, then based on public consensus, I will conduct a workshop for that topic too as long as it is related to Python/Data Science/Machine Learning.




Ideas for more workshops are welcome. You can open an issue on this repository or simply post in the gitter lobby, we will consider your proposals. If we don't get any ideas, we will host workshops based off our own judgement. A workshop topic will be chosen if atleast 10 or so people are interested in attending it.
