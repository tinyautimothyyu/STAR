import firebase_admin
from firebase_admin import db
import json
from datetime import datetime

dt_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# def register (ref, name='', phone='', reg_dt=dt_str):
#     query = ref.child('users').order_by_child("Name").equal_to(name).get()
#     # update
#     if len(query) != 0:
#         for key, value in query.items():
#             if value['Phone'] == phone:
#                 dates = value["Dates"]
#                 dates.append(reg_dt)
#                 print(key, value)


#     # new
    
#     data = {
#         'Name':name,
#         'Phone':phone,
#         'Dates':
#     }

cred_obj = firebase_admin.credentials.Certificate('sars-94120-firebase-adminsdk-9o0wd-341f021de7.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://sars-94120-default-rtdb.firebaseio.com'
	})

ref = db.reference('/')
# print(ref.get())

# ref.set({
#     'users':{

#     }
# }
# )

# ref.child('users').push(
#     {
# 	'Name':'Timothy',
#     'Phone':'7786806698',
#     'Dates':['2022-01-01', '2022-02-01']
#     },
# )

# data = ref.get()
# for key, value in data.items():
#     if value['Name'] == 'Timothy' and value['phone_no'] == '7786807537':
#         # print(value['Date'])
#         # print(type(value['Date']))
#         dates = value['Date']
#         dates.append('2022-03-01')
#         # print(dates)
#         ref.child(key).update({"Dates":dates})

# data = {
#     u'Name':u'Timothy',
#     u'phone_no':u'7786807537',
#     u'Date':['2022-01-01', u'2022-02-01']
# }

# db.collections(u'ayaya').documents(u'attendance').push(data)

query = ref.child('users').order_by_child("Name").equal_to("Timothy").get()
print(len(query))
for key, value in query.items():
    if value['Phone'] == '7786807537':
        print(key, value)
        dates = value['Dates']
        dates.append('2022-03-01')
        user_ref = db.reference('/users')
        user_ref.child(key).update({"Dates":dates})