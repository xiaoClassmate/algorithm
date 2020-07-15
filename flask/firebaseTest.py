from firebase import firebase
import json

firebase = firebase.FirebaseApplication('https://industriouswoman-myg36t91.firebaseio.com/', None)
data = {
	'serial' : 2,
	'name' : 'thrids',
	'price' : 12,
	'number' : 7
}
# # post
# result = firebase.post('/goods', data)

# update
# result = firebase.put('/goods/-MCFwDC4iPnaBlnMiBEc', 'name', 'oooo')

# # get
# result = firebase.get('/goods', '')

# # delete
# result = firebase.delete('/goods', 'key')

print(result)