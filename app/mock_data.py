import datetime

#Accounts:
USERS = [
	{'id': '0', 'username': 'admin', 'password': 'admin'},
	{'id': '1', 'username': 'admin2', 'password': 'admin2'},
	#The below is used to record the activity of users who don't have an account
	{'id': '2', 'username': 'Anonymous Guest', 'password': None}
]

#Call data:
CALL_HISTORY = [
	{'call_id': '0', 'host_id': '0', 'guest_ids': ['1'], 'room_name': 'panoramic-pigeon', 'timestamp': datetime.date(2017, 10, 22).strftime('%Y-%m-%d %H:%M:%S')},
	{'call_id': '1', 'host_id': '0', 'guest_ids': ['2', '2'], 'room_name': 'funky-fox', 'timestamp': datetime.date(2017, 3, 11).strftime('%Y-%m-%d %H:%M:%S')},
	{'call_id': '2', 'host_id': '1', 'guest_ids': ['0', '2'], 'room_name': 'triangular-tree', 'timestamp': datetime.date(2013, 6, 15).strftime('%Y-%m-%d %H:%M:%S')},
	{'call_id': '3', 'host_id': '1', 'guest_ids': ['1'], 'room_name': 'slow-sloth', 'timestamp': datetime.date(2017, 10, 21).strftime('%Y-%m-%d %H:%M:%S')},
	{'call_id': '4', 'host_id': '0', 'guest_ids': ['2'], 'room_name': 'pesky-panda', 'timestamp': datetime.date(2017, 3, 15).strftime('%Y-%m-%d %H:%M:%S')},
	{'call_id': '5', 'host_id': '1', 'guest_ids': ['0'], 'room_name': 'radical-racoon', 'timestamp': datetime.date(2015, 6, 16).strftime('%Y-%m-%d %H:%M:%S')}
]

def get_next_call_id(): 
	ids = [call['call_id'] for call in CALL_HISTORY]
	return str(int(max(ids)) + 1)

def get_call_by_call_id(call_id):
	for call in CALL_HISTORY:
		if call['call_id'] == call_id:
			return call
	return None