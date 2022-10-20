from flask import render_template

from saleapp.templates._init_ import app


@app.route('/')
def index():
    #categories = dao.load_categories()
   return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)