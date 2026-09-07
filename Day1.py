email_id = "saketh@codegnan.com"
print(email_id[7:15])

email_ids = ['meenav1143@gmailcom', 'meghanav0224@gmail.com', 'vandanav12@gmail.com','ankithay134@gmail.com']
print(len(email_ids))
print(email_ids[1])
print(email_ids[-2:])
email_ids.extend(['abc23@gmail.com', 'iuygh132@gmail.com', 'uygh234@gmail.com'])

'''print(email_ids)

for i in range(len(email_ids)):
    print(email_ids[i])
for mail in email_ids:
    print(f'Mail id of the person: {mail}')

users={}
#print(users.fromkeys(email_ids))
users = dict.fromkeys(email_ids)
users['abc23@gmail.com'] = 54
print(users)


#n = len(email_ids)
#for i in range(len(email_ids):
#    print(f'{i} : {email_ids[i]}')
users={}
for i in range(len(email_ids)):
    users[i +1] = email_ids[i]
print(users)
'''
#Enumerate - It provides by default a counter object (You can store in desired collection

data = dict(enumerate(email_ids, 1))
print(data)

#python - object
#Function - first class objects (function can use another function)
#Set - It is anunordered collection as it has no indexing
