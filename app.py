from flask import Flask, render_template
app = Flask(__name__)

app.config['DEBUG'] = True #CHANGE LATER

@app.route('/')
def home():
  return render_template('home.html')

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