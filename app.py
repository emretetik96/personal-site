from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.config['DEBUG'] = True #CHANGE LATER

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/writing_journalism')
def writing_journalism():
	return render_template('writing_journalism.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.errorhandler(404)
def not_found(error):
	return 'The page you are looking for does not exist...'

if __name__ == '__main__':
    app.run()