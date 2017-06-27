import datetime

#Accounts:
USERS = [
	{'id': 0, 'username': 'admin', 'password': 'admin'},
	{'id': 1, 'username': 'admin2', 'password': 'admin2'},
	#The below is used to represent user's who don't have an account are invited to calls
	{'id': 2, 'username': None, 'password': None}
]

#Call data:
CALL_HISTORY = [
	{'host_id': 0, 'invited_id': 1, 'timestamp': datetime.date(2017, 10, 22)},
	{'host_id': 0, 'invited_id': 2, 'timestamp': datetime.date(2017, 3, 11)},
	{'host_id': 1, 'invited_id': 0, 'timestamp': datetime.date(2013, 6, 15)},
	{'host_id': 1, 'invited_id': 1, 'timestamp': datetime.date(2017, 10, 21)},
	{'host_id': 0, 'invited_id': 2, 'timestamp': datetime.date(2017, 3, 15)},
	{'host_id': 1, 'invited_id': 0, 'timestamp': datetime.date(2015, 6, 16)}
]