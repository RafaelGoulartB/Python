import cv2

cap = cv2.VideoCapture(0)

def make_1080p():
	'''Change the resolution to 1080'''
	cap.set(3, 1920)
	cap.set(4, 1080)
def make_720p():
	'''Change the resolution to 720'''
	cap.set(3, 1280)
	cap.set(4, 1080)
def make_480p():
	'''Change the resolution to 480'''
	cap.set(3, 640)
	cap.set(4, 480)
def change_res(width, height):
	'''Change the resolution to a specific size'''
	cap.set(3, width)
	cap.set(4, height)


def rescale_frame(frame, percent=75):
    '''Set the resolution with the percent'''
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

while(True):
	#Capture Frame by Frame
	ret, frame = cap.read()
	
	#Change the image color
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#Show the normal image
	cv2.imshow('frame', frame)
	#Show image in gray scale
	cv2.imshow('frame2', gray)


	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cap.release()
cv2.destroyAllWindows()