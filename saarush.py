import pyttsx3, datetime, webbrowser, random, os, wolframalpha, MyAlarm,urllib.request
import cv2, requests, wikipedia, smtplib, ssl, pyjokes, pyautogui,time, instaloader, psutil, speedtest
import speech_recognition as sr
from pywikihow import search_wikihow
from email.message import EmailMessage
import pywhatkit as kit
import pandas as pd
from pygame import mixer
from bs4 import BeautifulSoup as bb
import numpy as np

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

app_id= "VGW9JT-JLWUT6EXPJ"
client = wolframalpha.Client(app_id)

emaildata = pd.read_csv("M:\\SAARUSH 2.0\\Email_ID.csv")

def wakeup():
    while True:
        per = takeCommand()
        if 'wake up' in per:
            FaceAuthenticator()
        if 'goodbye' in per or "you can close now" in per:
            speak("Ok sir goodbye, see you next time")
            exit()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning") 

    elif hour>=12 and hour<=18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")
    speak("Hello. my name is saarush. say wakeup when you want my help")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening...")
        r.adjust_for_ambient_noise(mic, duration=0.2)
        audio = r.listen(mic)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-IN')
        print(f"User said: {query}\n")
        
       
    except Exception as e:
        print(e)
        #speak('I did not recognize what you say. Please say that again')
        return ''
    query = query.lower()
    return query

def sendemail(to, content):
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = 'This is auto generated email'
    msg['From'] = "aftab.m1011@gmail.com"
    msg['To'] = to
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
    server.login('aftab.m1011@gmail.com', 'vnsiottwswdneykq')
    server.send_message(msg)

def intro():
    na = takeCommand()
    print(f"i hear your name is {na} is that correct")
    speak(f"i hear your name is {na} is that correct")
    query = takeCommand()
    if 'yes' in query:
        print(f"hello {na} how may i assist you")
        speak(f"hello {na} how may i assist you")
        return na
    elif 'no' in query:
        speak("oh i am so sorry please enter your name")
        na = input("enter your name:")
        print(f"is {na} is your correct name")
        speak(f"is {na} is your correct name")
        query = takeCommand()

        if 'yes' in query:
            print(f"hello {na} how may i assist you")
            speak(f"hello {na} how may i assist you")
            return na
    else:
        return na
    return query

def news():
    url = 'http://newsapi.org/v2/top-headlines?sources-techcrunch&apiKey3f4388e2946e4785aae1e2de44057812'
    page = requests.get(url).json()
    article = page['articles']
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth"]
    for ar in article:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"todays {day[i]} news is {head[i]}")
      
def startprogram():
    speak("verification successfull")
    speak("tell me what to do")
    taskexec()
        
def taskexec():
    while True:
        query = takeCommand()
        if 'sleep' in query or 'exit' in query:
            print("ok bye. call me when you need me")
            speak("ok bye. call me when you need me")
            wakeup()
        elif 'goodbye' in query or "you can close now" in query:
            speak("Ok sir goodbye, see you next time")
            exit()
            
        elif 'take me to' in query:
            query = query.replace("open", "")
            query = query.replace(" ", "")
            print("ok")
            speak('ok')
            webbrowser.open(f"www.{query}.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime) 
            
        elif 'open google' in query:
            speak(" what should I search on Google")
            cm =  takeCommand()
            webbrowser.open(cm)

        elif 'who are you' in query:
            speak("hello I am saarush. Your personal assistant. I am here to make your life easier. You can command me to do various tast")
            
            
        elif "calculate" in query:
            indx = query.split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'channel' in query:
            query = query.replace("channel", "")
            query = query.replace(" ", "")
            text ='https://www.youtube.com/results?search_query='+ query
            webbrowser.open(text)
            
        elif 'open notepad' in query:
            npath = 'C:\\Windows\\System32\\notepad.exe'
            os.startfile(npath)
        
        elif 'open command prompt' in query:
            os.system('start cmd')
            
        elif 'open camera' in query:
            FaceRecognition()

        elif 'music' in query:
            path = 'C:\\Users\\aftab\\OneDrive\\Desktop\\a6\\SAARUSH\\music\\'
            songs = os.listdir(path)
            #ran = random.choice(songs)
            for song in songs:
                if song.endswith('mp3'):
                    os.startfile(os.path.join(path, song))
                    
        elif 'ip address' in query:
            ip = requests.get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
            
        elif 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("according to wikipedia")
            print(results)
            speak(results)
            
        elif 'play song on youtube' in query:
            speak(" what song should I search on YouTube")
            srch = takeCommand()
            kit.playonyt(srch)
                        
        elif 'tell me a joke' in query:
            jokes = pyjokes.get_joke()
            speak(jokes)
            
        elif 'shut down the system' in query:
            speak("ok")
            os.system("shutdown /s /t 5")
            
        elif 'restart the system' in query:
            speak("ok")
            os.system("shutdown /r /t 5")
            
        elif 'sleep the system' in query:
            speak("ok")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            
        elif 'open mobile camera' in query:
            url = 'http://192.168.0.102:8080/shot.jpg'
            recognizer = cv2.face.LBPHFaceRecognizer_create() 
            recognizer.read('trainer/trainer.yml') 
            cascadePath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier (cascadePath) 
            font = cv2.FONT_HERSHEY_SIMPLEX 
            id = 2 
            names= ['', 'aftab', 'karan', 'atharva', 'rakesh'] 
            cam = np.array(bytearray(urllib.request.urlopen(url).read()), dtype=np.uint8)
            cam.set(3, 640) 
            cam.set(4, 480) 
            minW = 0.1*cam.get(3)
            minH = 0.1*cam.get(4)
            
            while True:
                img = cv2.imdecode(cam, -1)
                cv2.imshow('IPWebcam', img)
                converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
                faces = faceCascade.detectMultiScale(
                    converted_image,
                    scaleFactor = 1.2,
                    minNeighbors = 5,
                    minSize = (int(minW), int(minH)),
                )
                for(x,y,w,h) in faces:
                    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a
                    id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w])
                    if (accuracy <100):
                        id= names[id]
                        accuracy = "{0}%".format(round (100 - accuracy))
                    else:
                        id="unknown"
                        accuracy = "{0}%".format(round (100 - accuracy))
                    cv2.putText(img, str(id), (x+5, y-5),font,1, (255, 255, 255), 2)
                    cv2.putText(img, str(accuracy), (x+5, y+h-5), font, 1, (255, 255, 0), 1)
                    
                cv2.imshow('camera',img)
                k = cv2.waitKey(10) & 0xff
                if k == 27:
                    break
            cam.release()   
            cv2.destroyAllWindows()
            
        elif 'switch the window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')
            
        elif 'tell me news' in query:
            speak(" Please wait Sir fetching the latest news")
            news()
              
        elif 'where am i' in query or 'where are we' in query:
            speak(" wait Sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_re = requests.get(url)
                geo_data = geo_re.json()
                lon = geo_data['longitude']
                lat = geo_data['latitude']
                country = geo_data['country']
                speak(f" Sir I am not sure but I think we are in {country} country with {lon} longitude and {lat} latitude")
            except Exception as e:
                speak(" sorry Sir due to network issue I am not able to find where we are")
                pass
            
        elif 'instagram profile' in query or 'profile on instagram in query' in query:
            speak(" Sir please enter the user name correctly")
            name = input("Enter username here: ")
            webbrowser.open(f"www.instagram.com/{name}")
            time.sleep(5)
            speak(" Sir would you like to download the profile picture of this account")
            condition = takeCommand()
            if 'yes' in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak(" I am done Sir profile picture has been added to the main folder")
            else: 
                pass
            
        elif 'send email' in query or 'send mail' in query:
            try:
                speak(" to whom should I send the mail")
                nm = takeCommand()
                index = emaildata.loc[emaildata['name'] == nm].index[0]
                speak(" What should I say")
                content = takeCommand()
                to = emaildata.iloc[index, 1]
                sendemail(to, content)
                speak(f"Email has been sent to {nm}")
            except Exception as e:
                print(e)
                speak(" sorry sir I am not able to send this email")
                
        elif 'volume up' in query:
            pyautogui.keyDown('volumeup')
            time.sleep(5)
            pyautogui.keyUp('volumeup')
            
        elif 'volume down' in query:
            pyautogui.keyDown('volumedown')
            time.sleep(5)
            pyautogui.keyUp('volumedown')
        
        elif 'mute' in query:
            pyautogui.press('volumemute')
                
        elif 'temperature' in query:
            words = query.split()
            city = words[-1]
            condi = f'temperature in {city}'
            url = f'https://www.google.com/search?q={condi}'
            r = requests.get(url)
            data = bb(r.text,"html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f" current {condi} is {temp} ")
            
        elif 'how to do mode' in query or 'how to do mod' in query:
            speak(" how to do mode is activated. please tell me what you want to know.")
            while True:  
                how = takeCommand()
                try:
                    if 'exit' in how or 'close' in how:
                        speak("OK sir, how to do more is deactivated.")
                        break
                    else: 
                        max_r = 1
                        how_to = search_wikihow(how, max_r)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)       
                except Exception as e:
                    speak(" sorry Sir I am not able to find this.")
                    
        elif 'how much power left ' in query or 'how much power we have' in query or 'battery' in query:
            battry = psutil.sensors_battery()
            percentages = battry.percent
            speak(f"Sir, our system have {percentages} percent battery")
            if percentages>=75:
                speak("we have enough power to continue our work")
            elif percentages>=40 and percentages<=75:
                speak("we should connect our system to charging point to charge our battery")
            elif percentages<=15 and percentages<=30:
                speak("we don't have enough power to work, please connect to charging")
            elif percentages<=15:
                speak("we have very low power, please connect to charging the system will shutdown very soon")

        elif 'internet speed' in query:
            speak("sir please wait. i am testing the internet speed. it will take some time")
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            dl_MB = dl / (1024 * 1024 * 8)
            up_MB = up / (1024 * 1024 * 8)
            print(f" Sir we have {dl_MB} bit per second downloading speed and {up_MB} bit per second uploading speed")
            speak(f" Sir we have {dl_MB} bit per second downloading speed and {up_MB} bit per second uploading speed")
            
        elif 'alarm' in query:
            speak("sir please tell me the time to set the alarm")
            tt = takeCommand()
            tt = tt.replace(".", "")
            tt = tt.upper()
            MyAlarm.alarm(tt)

def FaceRecognition():
    recognizer = cv2.face.LBPHFaceRecognizer_create() 
    recognizer.read('trainer/trainer.yml') 
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier (cascadePath) 
    font = cv2.FONT_HERSHEY_SIMPLEX 
    id = 2 
    names= ['', 'aftab', 'karan', 'atharva', 'rakesh'] 
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
    cam.set(3, 640) 
    cam.set(4, 480) 
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    while True:
        ret, img =cam.read() 
        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a
            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w])
            if (accuracy <100):
                id= names[id]
                accuracy = "{0}%".format(round (100 - accuracy))
            else:
                id="unknown"
                accuracy = "{0}%".format(round (100 - accuracy))
            cv2.putText(img, str(id), (x+5, y-5),font,1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy), (x+5, y+h-5), font, 1, (255, 255, 0), 1)
            
        cv2.imshow('camera',img)
        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break
    cam.release()   
    cv2.destroyAllWindows()
    
def FaceAuthenticator():
    recognizer = cv2.face.LBPHFaceRecognizer_create() 
    recognizer.read('trainer/trainer.yml') 
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier (cascadePath) 
    font = cv2.FONT_HERSHEY_SIMPLEX 
    id = 2 
    names= ['', 'aftab', 'karan', 'atharva', 'rakesh'] 
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
    cam.set(3, 640) 
    cam.set(4, 480) 
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    while True:
        ret, img =cam.read() 
        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a
            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w])
            if (accuracy <100):
                id = names[id]
                accuracy = "{0}%".format(round (100 - accuracy))
                cam.release()
                cv2.destroyAllWindows()
                startprogram()
            else:
                id="unknown"
                accuracy = "{0}%".format(round (100 - accuracy))
                speak("user authentication failed")
                
                break
            cv2.putText(img, str(id), (x+5, y-5),font,1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy), (x+5, y+h-5), font, 1, (255, 255, 0), 1)
            
        cv2.imshow('camera',img)

if __name__ == "__main__":
    wishMe()
    while True:
        per = takeCommand()
        if 'wake up' in per:
            FaceAuthenticator()
        if 'goodbye' in per or "you can close now" in per:
            speak("Ok sir goodbye, see you next time")
            exit()
