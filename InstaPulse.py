import cv2
import time
import rppg
import mediapipe as mp
from cv2 import destroyAllWindows
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

def on_close(event):
    """
    Liseten for close event
    """
    plt.savefig('graph.png')
    cap.release()
    destroyAllWindows()
    exit()

def plotter(id, signals, title):
    """
    Plots graph for different signals
    """
    for (i ,s, t) in zip(id, signals, title):
        plt.subplot(i).clear()
        ax = plt.subplot(i)
        ax.title.set_text(t)
        ax.plot(s)
        ax.grid()
        plt.pause(0.05)

mp_drawing = mp.solutions.drawing_utils
#face mesh
mp_face_mesh = mp.solutions.face_mesh.FaceMesh
face_mesh = mp_face_mesh()
#face detection
mp_face_detection = mp.solutions.face_detection.FaceDetection
face_detection = mp_face_detection()

forehead= {} #forehead points
green_signal=[]
num_frames  = 1
cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

bpm = [0] #record of bpm

def animator(i):
    while True:
        start = time.time()
        ret, frame = cap.read()
        if not ret:
            continue
        image = frame.copy()
        height, width,_ = frame.shape
        rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #convert to rgb for mediapipe
        face = face_detection.process(rgb_img) 
        land_marks = face_mesh.process(rgb_img)
        if not(face.detections and land_marks.multi_face_landmarks): #if no face detected
            cv2.putText(frame, "No faces, kindly be in frame to begin" ,(10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow(root_wind, frame)
            
        else:
            for facial_landmarks, facial_rect in zip(land_marks.multi_face_landmarks, face.detections):
                mp_drawing.draw_detection(image, facial_rect)
                for lmark in list([67, 299]): #67 is top left corner of forehead, 299 is bottom right corner
                    point = facial_landmarks.landmark[lmark]
                    x = int(point.x * width)
                    y = int(point.y * height)
                    forehead[lmark] = (x,y) #store points in dictionary
                (x1,y1),(x2,y2) = forehead[67], forehead[299]
            roi = frame[y1-8:y2, x1:x2] #crop forehead
            height, width,_ = roi.shape
            if height >0 and width > 0:
                cv2.rectangle(image, (x1, y1-8), (x2, y2), (0, 255, 0), 2) #draw rectangle for forehead
                g = roi[:,:,1] #green channel of roi
                green_signal.append(g.mean())
                if len(green_signal) != 0 and len(green_signal)%30==0:
                    det = rppg.detrend_signal(green_signal, 30) #deterend signal
                    filtered = rppg.filter_butterworth_bandpass(det, 30, 900, (0.7, 3.0)) #filter signal
                    f, P = rppg.signal.periodogram(filtered,fs=30.0) #sample freq & power scpectrum
                    hbeat = round(rppg.maxvalue(P, f) * 60, 2)
                    print("Your Heart Rate : ", hbeat)
                    bpm.append(hbeat)
                    plotter([311,312,313], [green_signal, det, filtered], ["Raw Signal", "Detrended Signal", "Filtered Signal"]) 
                    
                end = time.time()
                second = end - start
                fps = num_frames/second
                cv2.putText(image, "Estimated Heart Rate:" + str(bpm[-1]), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
                cv2.putText(image, "FPS: " + str(round(fps)), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1)
                cv2.putText(image, "To close app, closs the graph window", (10,90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255),1 )
                
                cv2.imshow(root_wind, image)
                cv2.imshow(roi_wind, g)

        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break

#openCV window      
root_wind = 'Extraction of Estimate Heart Pulse'
roi_wind = "Green Channel (Region of Interest)"
cv2.namedWindow(root_wind)
cv2.namedWindow(roi_wind)

#animator
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close)
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=1)
animation = FuncAnimation(plt.gcf(), animator)
plt.show()
#release camera
cap.release()
destroyAllWindows()
