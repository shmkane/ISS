#Soham Kane
#Where's ISS?
#04/12/16

import json
import turtle
import urllib.request
import codecs
import time
import threading
import sched

def divide():
  for x in range(2):
    print("")

def main():
  print("Creating a screen to display the map...")
  #Setup screen
  screen = turtle.Screen()
  screen.setup(720, 360)
  screen.setworldcoordinates(-180,-90,180,90)
  print("Displaying map...")
  screen.bgpic("/home/shmkane/Pictures/MAP.png")
  print("Screen created successfully!")
  
  divide()
  
  print("Marking your location...")
  #Mark my location
  mylocation = turtle.Turtle()
  mylocation.penup()
  mylocation.color('red')
  mylocation.goto(my_lat, my_long)
  mylocation.dot(5)
 
  #To make it a dot
  #Instead of an 'arrow'
  mylocation.hideturtle()
  print("Location marked")
  
  issloc = getLocation()
  longi = issloc[0];
  lati = issloc[1];
  
  ISSlocation = turtle.Turtle()
  
  ISSlocation.penup()
  ISSlocation.color('red') 
  ISSlocation.pencolor('red') 
  ISSlocation.pensize(5)
  ISSlocation.goto(float(lati), float(longi))
  
  infoLoc = turtle.Turtle()
  infoLoc.hideturtle()
  infoLoc.penup()
  infoLoc.color('red') 
  style = ('Arial', 10, 'bold')
  infoLoc.goto(-183, 87)
  infoLoc.write(issloc, font=style)

  getTime(mylocation)
  time_elapsed = 0
  while 1:
    time.sleep(1)
    time_elapsed+=1
    infoLoc.clear()
    infoLoc.write(str(issloc) + " Updates: " + str(time_elapsed), font=style)
    time.sleep(1)
    time_elapsed+=1
    infoLoc.clear()
    infoLoc.write(str(issloc) + " Updates: " + str(time_elapsed), font=style)
    time.sleep(1)
    time_elapsed+=1
    infoLoc.clear()
    infoLoc.write(str(issloc) + " Updates: " + str(time_elapsed), font=style)
    time.sleep(1)
    time_elapsed+=1
    infoLoc.clear()
    infoLoc.write(str(issloc) + " Updates: " + str(time_elapsed), font=style)
    time.sleep(1)
    time_elapsed+=1
    infoLoc.clear()
    infoLoc.write(str(issloc) + " Updates: " + str(time_elapsed), font=style)
    #divide()
    #print ("Attempting to grab ISS' location...")
    #Print location
    ISSlocation = turtle.Turtle()
    ISSlocation.hideturtle()
    ISSlocation.penup()
    ISSlocation.goto(float(lati), float(longi))
    ISSlocation.pendown()
    
    issloc = getLocation()
    longi = issloc[0];
    lati = issloc[1];
    ISSlocation.pencolor('red') 
    ISSlocation.goto(float(lati), float(longi))
    print("Updating location...")

  
def getTime(loc):
  divide()
  print("Getting time ISS will pass above you...")
  #When will it be overhead?
  timeurl = 'http://api.open-notify.org/iss-pass.json?lat=' + str(my_long) + '&lon=' + str(my_lat)
  time_response = urllib.request.urlopen(timeurl)
  time_result = json.load(reader(time_response))
  timeover = time.ctime(time_result['response'][0]['risetime'])
  style = ('Arial', 10, 'bold')
  loc.write(timeover, font=style)
  print("Got time!", timeover)
  return timeover
  
def getLocation():
  #print("Connecting to ISS...")
  #Make a connection with ISS
  url = 'http://api.open-notify.org/iss-now.json'
  response = urllib.request.urlopen(url)
  result = json.load(reader(response))
  #print("Connection established!")
  #Get the current longitude and latitude of the ISS
  longi = result['iss_position']['longitude']
  lati = result['iss_position']['latitude']
  location  = [lati, longi]
  #print("Location retrieved successfully!", location)
  #Print
  #print("Getting location...")

  return location
  
my_lat = -75.000000
my_long = 36.000000

reader = codecs.getreader("utf-8")

main()
