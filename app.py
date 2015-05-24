from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
  return 'Home'

@app.route('/about')
def about():
	return 'About'

@app.route('/projects')
def projects():
	return 'Projects'

@app.route('/writing_journalism')
def writing_journalism():
	return 'Writing/Journalism'

@app.route('/contact')
def contact():
	return 'contact'

@app.errorhandler(404)
def not_found(error):
	return 'The page you are looking for does not exist...'

if __name__ == '__main__':
    app.run()