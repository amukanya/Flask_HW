from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return '<h2><em>Hi, I am Andy Mukanya</em></h2>'


@app.route('/info')
def info():
  year  = 2019;
  return 'My major is I.T Programming since ' + str(year)
  
app.run(host='0.0.0.0', port=8080)
