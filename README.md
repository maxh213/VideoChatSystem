# VideoChatSystem
This project is my first time using the flask framework so I would very much like to here feedback in regard to best practices or anything I could improve on.

I managed to complete the following functionality:
* Created a system which can be logged into and keep track of multiple users logged in at once.
* Have a page where users can create their own video calls
* Have a page where users can see a history of video calls they participated in
* Allow users to share a link to a video call which other users can join, where all the participants of the call get logged

Due to the limited time I had I couldn't complete everything I wished to do so on this project, given more time I would have:
* Replaced the mock data I was using with real data from a database.
* Improve on the overall look of the application
* Spent more time researching the best way to implement Flask applications
* Add unit tests (Usually I'd make this in TDD but I had never written tests before for Flask so I didn't want to add that to the list of things to learn and risk not delivering all the functionality. This wouldn't have been an issue had I known Flask going into this project.)
* There are a couple TODOs throughout the code which can give you an idea of what I would have liked to add given more time. They were left in more for the reader's benefit, normally I don't make a habit of leaving TODOs in code I write.
* Added a profile page so users could invite other users through the application, not just through a link

# Frameworks used:
* Flask
* JQuery
* Skeleton CSS boilerplate

# Requirements needed to run:
* Python3.5
* Flask

# How to run:
First time setup:
~~~~
pip3 install -r requirements.txt
~~~~

Then run the server with:
~~~~
python3 run.py
~~~~
and visit localhost:5000/

There are two test account users:
* username: admin password: admin
* username: admin2 password: admin2

Accounts are not necessary for any of the functionality except checking your call history.

# Support
Do not hesitation to get in touch if you have any questions or run into any problems.
Email: max.o.harris@outlook.com
Phone: 07835367449
