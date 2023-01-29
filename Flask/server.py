from flask import Flask, request, render_template, Response
import camera


global capture

app = Flask(__name__)

# @app.route("/")
# def main():
#     return "<h1>Hello world</h1>"

@app.route("/")
def index():
    return render_template("index.html")


def gen(camera):
    while True:
        #get camera frame
        frame = camera
        # print(type(frame))
        return (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        

@app.route('/video_feed')
def video_feed():
    return Response(gen(camera.capture()),mimetype='multipart/x-mixed-replace; boundary=frame')




# @app.route('/video_feed')
# def video_feed():
#     return Response(camera.capture())

@app.route("/requests", methods=['POST', 'GET'])
def tasks():
    return "<h1>Ariyal</h1>"

app.run()