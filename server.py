from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def hello_world():
    print("\n","*" *50, "\n Running in the 'hello_world' function")
    return render_template('index.html', times=3, color="lightblue")

@app.route('/play/<num_times>')
def just_boxes(num_times):
    return render_template('index.html', times=int(num_times), color="lightblue")
    
@app.route('/play/<num_times>/<box_color>')
def box_and_color(num_times, box_color):
    print("the color is", box_color)
    return render_template('index.html', times=int(num_times), color=box_color)
    




if __name__=="__main__":
    app.run(debug=True)