import cv2
def Diagnosis(frame,label,reaction):
    if (label==0):
        reaction[0] = reaction[0]+1
        cv2.imwrite("Diagnosis Report/Angry.jpg",frame)
    if (label == 1):
        reaction[1] = reaction[1] + 1
        cv2.imwrite("Diagnosis Report/Disgust.jpg", frame)
    if (label==2):
        reaction[2] = reaction[2] + 1
        cv2.imwrite("Diagnosis Report/Fear.jpg",frame)
    if (label==3):
        reaction[3] = reaction[3] + 1
        cv2.imwrite("Diagnosis Report/Happy.jpg",frame)
    if (label==4):
        reaction[4] = reaction[4] + 1
        cv2.imwrite("Diagnosis Report/Neutral.jpg",frame)
    if (label==5):
        reaction[5] = reaction[5] + 1
        cv2.imwrite("Diagnosis Report/Sad.jpg",frame)
    if (label==6):
        reaction[6] = reaction[6] + 1
        cv2.imwrite("Diagnosis Report/Surprise.jpg",frame)
def Write1(par):

    file=open('Diagnosis Report/Report.txt','w')
    file.write("\t\t\t\t"+"//The Diagnosis Report//"+"\n")
    file.write("Angry:"+str(par[0])+"\n")
    file.write("Disgust:"+str(par[1])+"\n")
    file.write("Fear:" + str(par[2]) + "\n")
    file.write("Happy:" + str(par[3]) + "\n")
    file.write("Neutral:" + str(par[4]) + "\n")
    file.write("Sad:"+str(par[5])+"\n")
    file.write("Surprise:" + str(par[6]) + "\n")
    file.close()
