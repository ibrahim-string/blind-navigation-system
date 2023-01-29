# Importing required modules
from flask import Flask, request, render_template, Response
import cv2

# Initiating flash 
app = Flask(__name__)


# Starting to cap
capture = cv2.VideoCapture(0)


# Home route
@app.route("/")
def index():
    return render_template("index.html")



# Function to generate the frame
def gen():
    while True:
        success, frame = capture.read()
        if success:
            try:
                ret, buffer = cv2.imencode('.jpg', cv2.flip(frame,1))
                frame = buffer.tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
            except Exception as e:
                pass   
        else:
            continue
        


# Path to feed the video to the html
@app.route('/video_feed')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')



# Some extra stuffs
@app.route("/requests", methods=['POST', 'GET'])
def tasks():
    return "<h1>Ariyal</h1>"


# To start the server
app.run()


capture.release()
cv2.destroyAllWindows()
