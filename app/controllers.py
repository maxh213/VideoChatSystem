from app import mock_data
from datetime import datetime

#In an app with real data this would not happen, the username/password(which is hashed) would be compared against a database
def get_user_account_with_login(username, password):
	for user in mock_data.USERS:
		if user['username'] == username and user['password'] == password:
			return {'id': user['id'], 'username': user['username']} #done to remove the password from the session
	return None

def get_user_account_by_id(user_id):
	for user in mock_data.USERS:
		if user['id'] == user_id:
			return user
	return None

def get_user_call_history(user):
	calls = []
	for call in mock_data.CALL_HISTORY:
		guest_names = get_guest_names_from_ids(call['guest_ids']) 
		if call['host_id'] == str(user['id']): 
			calls.append({'host': user['username'], 'guests': guest_names, 'timestamp': call['timestamp']})
		elif str(user['id']) in call['guest_ids']:
			calls.append({'host': get_user_account_by_id(call['host_id'])['username'], 'guests': guest_names, 'timestamp': call['timestamp']})
	return calls

def get_guest_names_from_ids(guest_ids):
	guest_names = []
	for guest_id in guest_ids:
		guest_names.append(get_user_account_by_id(guest_id)['username'])
	return guest_names

def log_new_call(host_id, room_name):
	new_call_id = mock_data.get_next_call_id()
	mock_data.CALL_HISTORY.append({
			"call_id": new_call_id,
			"host_id": host_id,
			"guest_ids": [],
			"room_name": room_name,
			"timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		})
	return new_call_id

def update_guest_id_in_an_active_call(call_id, guest_id):
	#TODO: MAKE SURE TO HANDLE NONE
	call = mock_data.get_call_by_call_id(call_id)
	if call is not None:
		call['guest_ids'].append(guest_id)
		return True
	else:
		return False

