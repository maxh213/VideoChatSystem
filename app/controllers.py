from app import mock_data

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
		if call['host_id'] == user['id']: 
			calls.append({'host': user['username'], 'invited': get_user_account_by_id(call['invited_id'])['username'], 'timestamp': call['timestamp']})
		elif call['invited_id'] == user['id']:
			calls.append({'host': get_user_account_by_id(call['host_id'])['username'], 'invited': user['username'], 'timestamp': call['timestamp']})
	return calls
