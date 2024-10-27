import  socket

URL = input(" x7raj Team --> Enter Your URL --> : ")
IP = socket.gethostbyname(URL)
print ("Your IP Is = " +IP) 
