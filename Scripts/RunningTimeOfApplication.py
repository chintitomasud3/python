from flask import Flask, render_template
import psutil
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_running_time")
def get_running_time():
    running_times = {}

    for proc in psutil.process_iter(['name', 'create_time']):
        create_time = proc.info['create_time']
        running_time = int(time.time() - create_time)
        process_name = proc.info['name']
        if process_name in running_times:
            running_times[process_name].append(running_time)
        else:
            running_times[process_name] = [running_time]

    return running_times

if __name__ == "__main__":
    app.run(debug=True)