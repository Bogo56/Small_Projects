import cv2,datetime,pyttsx3,pandas

## IT gets LAGGY when I add Sound

#alert=pyttsx3.init()
#alert.setProperty("rate",220)
#voices=alert.getProperty("voices")
#alert.setProperty("voice",voices[0].id)

#We Start capturing video with the camera
vid=cv2.VideoCapture(0)
i=0
status_list=[]
#Creating Excel Structure
report={"Date_Appeared":[],"Date_Disappeared":[]}

while True:
    
    now=datetime.datetime.now()
    date=now.strftime("%d-%m-%Y %H:%M:%S")
#We're gonna use this variable to measure movement vs no-movement
    status=0
#Capturing the Frame, transforming it to Grayscale, and adding Gaussian Blur to reduce the many types of gray and white(easier to process)
    check,frame=vid.read()
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_gray=cv2.GaussianBlur(frame_gray,(25,25),0)


##Storing the first frame, so we can use is as a comparison base for movement afterwards
    if i<1:
        frame_one_gray=frame_gray
        frame_one_gray=cv2.GaussianBlur(frame_one_gray,(25,25),0)
        i+=1
        continue
    
##Keeping the last 10 values, so the list doesn't get too big
    status_list=status_list[-10:]

    if len(status_list)>2:
        if status_list[-1]>status_list[-2]:
            report["Date_Appeared"].append(date)
    

        elif status_list[-1]<status_list[-2]:
            report["Date_Disappeared"].append(date)

            


    ## Measuring the difference between the base frame and each new frame
    delta=cv2.absdiff(frame_one_gray,frame_gray) 
    ##Coloring white(255)each pixel with intensity(difference) higher than 30
    treshold= cv2.threshold(delta,30,255,cv2.THRESH_BINARY)[1]

    #Getting the contours of the white objects
    (contours,_)=cv2.findContours(treshold.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    

    for contour in contours:

    ## We don't need smaller objects
        if cv2.contourArea(contour)<2000:
            continue
    ##Drawing rectangle
        else:
            (x,y,w,h)=cv2.boundingRect(contour)
            cv2.rectangle(frame,(x,y),((x+w),(y+h)),(0,255,50),5)

        status=1
        #alert.say("Intruder,Alert!")
        #alert.runAndWait()

    status_list.append(status)

    cv2.imshow("Capturing", frame)
    key=cv2.waitKey(100)
    

 
    print(status)
                
    

    if key==ord("q"):
        break


with pandas.ExcelWriter("controls_1.xlsx",mode="w") as writer:
    
    df=pandas.DataFrame(report)
    df.to_excel(writer)


vid.release()

