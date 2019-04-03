import gaia.mysql as con

ModelPeople = con.find("SELECT id, CONCAT(first_name, ' ', last_name) as full_name, username, password FROM auth_user")

class Person:
   def __init__(self, fullname, username, password):
    self.fullname = fullname
    self.username = username
    self.password = password

list = ['unknow']
for person in ModelPeople:
   list.insert(person[0], Person(person[1], person[2], person[3]))

def all():
   return list

def get(id):
   return list[id]