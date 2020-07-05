from flask import Flask, render_template, Response
from Camera import VideoCamera

app = Flask(__name__)

class object1:
	minbgr = (94, 56, 0)
	maxbgr = (218, 167, 33)

class object2:
	minbgr = (27, 144, 168)
	maxbgr = (61, 164, 181)

@app.route('/')
def index():
    # rendering webpage
    return render_template('index.html', object1 = object1, object2 = object2,)
	
	
def gen(Camera):
	while True:
		frame = Camera.get_frame(object1, object2)
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
					
if __name__ == '__main__':
    # defining server ip address and port
    app.run(debug=True)