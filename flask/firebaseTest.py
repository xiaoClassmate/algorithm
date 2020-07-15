from firebase import firebase
import json

firebase = firebase.FirebaseApplication('https://industriouswoman-myg36t91.firebaseio.com/', None)
data = {
	'serial' : 10,
	'name' : 'aaaaaaaaa',
	'price' : 12,
	'number' : 7
}
# # post
# result = firebase.post('/goods', data)

# # update
# result = firebase.put('/goods/-MCHi-uxVTVPd7-zvD0X', 'name', 'bbbbbbbb')

# get
# result = firebase.get('/goods', '')

# delete
result = firebase.delete('/goods', '-MCHi-uxVTVPd7-zvD0X')

# print(result)