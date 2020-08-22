from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def portfolio():
   return render_template('portfolio.html')

#local only
#if __name__ == '__main__':
#   app.run()