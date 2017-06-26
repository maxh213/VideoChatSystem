# VideoChatSystem
You are part of an engineering team that was asked to prototype a simple video chatting system. The users of the system should be able to: 
*⋅⋅ have a page where they can create their own video calls 
*⋅⋅ have a page where they can see the history of all the video calls 
*⋅⋅ Bonus: be able to invite other participants to join their calls 
*.. MAKE RESPONSIVE
*.. TESTS

You are asked to design and implement the system based on the above spec. 

The implementation of the backend system should be in Python. 
For the video chatting part you can use the appear.in Developer Javascript SDK (https://developer.appear.in/). 

If you require a database SQLite will be sufficient - no need for complex setups. You are free to use any industry standard libraries/frameworks for the UI part.


# Requirements needed to run:
..* Python3.5
..* Flask

# How to run:
Build the database first:
~~~~
sqlite3 database.db < schema.sql
~~~~

Then run the sever with:
~~~~
python3 run.py
~~~~
