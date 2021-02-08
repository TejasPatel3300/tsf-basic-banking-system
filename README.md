# tsf-banking-system
Simple Banking System in flask web framework


In this project Flask Web Framework is used along with html & css.
There is no customer/user creation in this project.

If you want to add customer, two ways you can do it in this project.

1. Delete test.db file. (CAUTION: this approach will  result in lost of all previous transactions as it deletes the database itself.)
  >>> Open python shell in terminal. Then write following...
   from app import db    (press enter)
   db.create_all()       (this will create new test.db file)
   exit()                (exit python shell)

  >>> Open test.py file and add a new dictionary into customerlist as previous ones. And run the test.py.It will add a new customer/user in database.

2.open the test.py file and remove all the previous dictionaries and add a new dictionary into customerlist as previous ones.
Run test.py file. New cuustomer will be added to the database.
