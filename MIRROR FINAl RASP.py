import tkinter as tk
from tkinter import *
import time
import requests
from newsapi import NewsApiClient
import os

decrypt = list()
global iteration
global timecount
global repull
global sleep
iteration = 0
timecount = 0
repull = 0
sleep = 0

def weather():
    api_key = "5cb1e254e4ad199e31dd9fd7d079667b"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = input("Mumbai:")
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
	
    day.config(text='Mumbai,India''\nTemperature:'+str(current_temperature)+'°C'+"\nDescription:"+ str(weather_description)+"\nHumidity:"+ str(current_humidity)+'%')
    

def dayy():
    day = time.strftime("%d/%B/%Y")
    clockk.config(text=day)
    clockk.after(200,tick)


while True:


    def tick(time1=''):
        time2 = time.strftime("%I")
        if time2 != time1:
            time1 = time2
            clock_frame.config(text=time2)
        clock_frame.after(200, tick)

    def tickk(time3=''):
        time4 = time.strftime("%M")
        if time4 != time3:
            time3 = time4
            clock_frame2.config(text=time4)
        clock_frame2.after(200, tickk)

     
    def tickkk(time3=''):
        time4 = time.strftime("%S")
        if time4 != time3:
            time3 = time4
            clock_frame3.config(text=time4)
        clock_frame3.after(200, tickkk)
   


    #This function waits for a certain amount of 'tocks' and then initiates 'newsheader' -function
    def tock():
        global timecount
        global repull
        global sleep
        global decrypt
        newstitle.after(200, tock)
        if timecount < 20:
            timecount +=1
        else:
            timecount = 0
            newsheader()
        if repull < 200:
            repull +=1
        else:
            repull = 0
            headlines = api.get_top_headlines(sources='the-times-of-india')
            payload = headlines
            decrypt = (payload['articles'])
            maxrange = len(decrypt)
        if sleep < 800:
            sleep+=1
        else:
            sleep = 0

    api = NewsApiClient(api_key='04f8cd2f31004c8d91c8d7bb3c4fda12')

    #This sequence decrypts the info feed for the script
    headlines = api.get_top_headlines(sources='the-times-of-india')
    payload = headlines
    decrypt = (payload['articles'])
    maxrange = len(decrypt)

    #This function iterates over the news headlines. Iteration is the news number, 'itemlist' brings out only the title.
    def newsheader():
        global iteration
        global decrypt
        itemlist = decrypt[iteration]
        #print(itemlist['title'])
        newstitle.config(text=itemlist['title'])
        source.config(text=itemlist['author'])
        if iteration < 9:
            iteration +=1
        else:
            iteration = 0
	

	
    root = tk.Tk()
    root.title('Mirror')

    masterclock = tk.Label(root)
    masterclock.pack(anchor=NW, fill=X, padx=45)
    masterclock.configure(background='black')
    clock_frame = tk.Label(root, font = ('caviar dreams', 130), bg='black', fg='white')
    clock_frame.pack(in_=masterclock, side=LEFT)
    clock_frame2 = tk.Label(root, font = ('caviar dreams', 70), bg='black', fg='white')
    clock_frame2.pack(in_=masterclock, side=LEFT, anchor = N, ipady=15)
    clock_frame3 = tk.Label(root, font = ('caviar dreams', 30), bg='black', fg='white')
    clock_frame3.pack(in_=masterclock, side=LEFT, anchor = N, ipady=25)
    newstitle = tk.Label(root, font = ('caviar dreams', 20), bg='black', fg='white')
    newstitle.pack(side=BOTTOM, anchor=W, fill=X)
    source = tk.Label(root, font = ('caviar dreams', 20), bg='black', fg='white')
    source.pack(side=BOTTOM, anchor=W, fill=X)
    day=tk.Label(root,font=("caviar dreams",20),bg="black",fg="white")
    day.place(x=1200,y=100)
    clockk = tk.Label(root, bg='black', fg='white',  font=("caviar dreams", 25))
    clockk.place(x=240,y=120)
    lbl = tk.Label(root, text="Looking Good!!", bg='black', fg='white',  font=("Arial Bold", 50))
    lbl.place(x=450,y=400)
 


    newsheader()
    tick()
    tickk()
    tock()
    weather()
    tickkk()
    dayy()
   
    root.attributes("-fullscreen", True)
    root.configure(background='black')
    root.mainloop()