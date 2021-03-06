from flask import Flask, render_template, Response, request
from Camera import VideoCamera
import colorpicker

app = Flask(__name__)


@app.route('/')
def index():
	# rendering webpage
	return render_template('index.html', inpobj1 = True, outshow = False)


@app.route('/showoutput')
def showoutput():
	# rendering webpage
	showoutput.colorobj1 = detect.color
	return render_template('index.html', object1 = showoutput.colorobj1, inpobj1 = False, outshow = True)
	

def detect(Camera):
	while True:
		frame = Camera.get_roi()
		detect.color = colorpicker.color()

		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')   

def gen(Camera):
	while True:
		frame = Camera.get_frame(showoutput.colorobj1)
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
	return Response(gen(VideoCamera()),
					mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/color_detect')
def color_detect():
	return Response(detect(VideoCamera()),
					mimetype='multipart/x-mixed-replace; boundary=frame')

			
if __name__ == '__main__':
	# defining server ip address and port
	app.run(debug=True)