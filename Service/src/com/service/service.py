'''
Created on 02/08/2016

@author: cv07285
'''
import web
import model
import json
urls = (
    '/hola/(.*)', 'hello', 
    '/adios/(.*)','adios'
)
app = web.application(urls, globals())



class Student:
    def __init__(self,name,email,contact,skills,edu):
 
        self.email=email
        self.contact=contact
        self.name=name
        self.skills=skills
        self.edu=edu 
lista = list()
james=Student("James","j@j.com","+1 7789990007","Python","University")
james2=Student("Cesar","c@c.com","+1 12345678","Java","Degree")

lista.append(james)
lista.append(james2)

class hello:
    def GET(self, name):
        def default(o):
            return o.__dict__
        todos = model.get_todos()
        if not name: 
            name = 'World'
            
        return json.dumps(lista, default=default,indent=4)

class adios:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Adios, ' + name + '!'

if __name__ == "__main__":
    app.run()