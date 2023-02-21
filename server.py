from flask import Flask,render_template

app = Flask(__name__)



@app.route('/play', defaults = {'number': 3 , 'c': 'aqua'})
@app.route('/play/<int:number>', defaults = {'c': 'aqua'})
@app.route('/play/<int:number>/<string:c>')
def level_3(number, c):
    c = f'style=background-color:{c};'
    return render_template("playground.html", times=number, color_style=c)

if __name__ == "__main__":
    app.run(debug = True, port = 5000)