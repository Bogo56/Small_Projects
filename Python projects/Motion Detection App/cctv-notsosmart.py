import cv2,datetime,pyttsx3,pandas

## IT gets LAGGY when I add Sound

#alert=pyttsx3.init()
#alert.setProperty("rate",220)
#voices=alert.getProperty("voices")
#alert.setProperty("voice",voices[0].id)

#We Start capturing videowith the camera
vid=cv2.VideoCapture(0)
i=0
on_off=0
status=0

while True:
    
    now=datetime.datetime.now()
    date=now.strftime("%d/%m/%Y %H:%M:%S")

#Capturing the Frame, transforming it to Grayscale, and adding Gaussian Blur to reduce the many types of gray and white(easier to process)
    check,frame=vid.read()
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_gray=cv2.GaussianBlur(frame_gray,(25,25),0)
#We're gonna use this variable to measure movement vs no-movement


##Storing the first frame, so we can use is as a comparison base for movement afterwards
    if i<1:
        frame_one_gray=frame_gray
        frame_one_gray=cv2.GaussianBlur(frame_one_gray,(25,25),0)
        i+=1
        continue

    if status==1 and (on_off==2 or on_off==3):

        df=pandas.read_excel("controls_1.xlsx")

        with pandas.ExcelWriter("controls_1.xlsx",mode="w") as writer:
            new_row={"Object_Appeared":date}
            df=df.append(new_row,ignore_index=True)
            df.to_excel(writer)

    elif status==1 and on_off==1:
        
        df=pandas.read_excel("controls_1.xlsx")

        with pandas.ExcelWriter("controls_1.xlsx",mode="w") as writer:
            new_row={"Object_Disappeared":date}
            df=df.append(new_row,ignore_index=True)
            df.to_excel(writer)
        
        status=0
        on_off=0

    
    ## Measuring the difference between the base frame and each new frame
    delta=cv2.absdiff(frame_one_gray,frame_gray) 
    ##Coloring white(255)each pixel with intensity(difference) higher than 30
    treshold= cv2.threshold(delta,30,255,cv2.THRESH_BINARY)[1]

    #Getting the contours of the white objects
    (contours,_)=cv2.findContours(treshold.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    

    for contour in contours:

    ## We don't need smaller objects
        if cv2.contourArea(contour)<2000:
            on_off=1
            continue
    ##Drawing rectangle
        else:
            (x,y,w,h)=cv2.boundingRect(contour)
            cv2.rectangle(frame,(x,y),((x+w),(y+h)),(0,255,50),5)

        status=1
        on_off+=2
        #alert.say("Intruder,Alert!")
        #alert.runAndWait()



    cv2.imshow("Capturing", frame)
    key=cv2.waitKey(100)
    


    print(status, on_off)
                
    

    if key==ord("q"):
        break

vid.release()


