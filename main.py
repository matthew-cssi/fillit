import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/home.html')
        self.response.write(template.render())

class Signup(webapp2.RequestHandler):
    def post(self):
        age = int(self.request.get('age'))
        pokemons = self.request.get_all('pokemon')
        templateVars = {
            'username': self.request.get('username'),
            'password': self.request.get('password'),
            'tier': self.request.get('tier'),
            'legal': age >= 13,
            'newsletter': bool(self.request.get('newsletter')),
            'pokemons': pokemons,
        }
        template = env.get_template('templates/signup.html')
        self.response.write(template.render(templateVars))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', Signup),
], debug=True)
