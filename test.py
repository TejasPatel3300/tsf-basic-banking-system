from app import db, Customers

customerlist = [
    {'name' : 'bill gates', 'email': 'bill@gmail.com', 'current_balance' : 33447866},
    {'name' : 'jeff bezos', 'email': 'jeff@gmail.com', 'current_balance' : 48348664},
    {'name' : 'ratan tata', 'email': 'ratan@gmail.com', 'current_balance' : 39445567},
    {'name' : 'elon musk', 'email': 'elonmusk@gmail.com', 'current_balance' : 94467848},
    {'name' : 'cnn network', 'email': 'cnn@gmail.com', 'current_balance' : 76447856}
]

for i in customerlist:
    new_customer = Customers()
    new_customer.name = i['name']
    new_customer.email = i['email']
    new_customer.current_balance = i['current_balance']
    db.session.add(new_customer)
    db.session.commit()

print("finished")