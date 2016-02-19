# Amanda Foun

from flask import Flask
app = Flask(__name__) # create instance of Flask class

@app.route('/search') # route decorator
@app.route('/') 
def search():
    return 'Hello'

if __name__ == '__main__':
    app.run()