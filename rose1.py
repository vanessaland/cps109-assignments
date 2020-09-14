#LLAMA PARTY
#This is a party for all of the llamas to play in.
def llamaParty():
  pic = makePicture('/Users/vanessalandayan/Downloads/CPS109/mediasources-4ed/llama.jpg')
  gift(pic)
  ribbon(pic)
  streamers(pic, 0, 20, 359, 20, 10, pink)
  streamers(pic, 0, 30, 359, 30, 10, cyan)
  streamers(pic, 0, 40, 359, 40, 10, pink)
  circle(pic, 190, 200, 30, green)
  redLights(pic)
  show(pic)

#Function 1
#This function puts a blue gift box beside the llama.  
def gift(picture):
  pixels = getPixels(picture)
  for pixel in pixels:
    x = getX(pixel)
    y = getY(pixel)
    if 245 < x < 345 and 350 < y < 410:
      setColor(pixel, blue)

#Function 2
#This function puts green lines for ribbon on top of the gift.            
def ribbon(picture):
  pixels = getPixels(picture)
  for pixel in pixels:
    x = getX(pixel)
    y = getY(pixel)
    if 295 < x < 305 and 350 < y < 410:
      setColor(pixel, green)
    if 245 < x < 345 and 380 < y < 390:
      setColor(pixel, green)

#Function 3
#This function puts creates a thick lines for streamers on the ceiling.        
def streamers(picture, x1, y1, x2, y2, thickness, color) : 
  pixels = getPixels(picture)
  m = 1.0 * (y2 - y1) / (x2 - x1)
  b = y1 - m * x1
  for pixel in pixels : 
    x = getX(pixel)
    y = getY(pixel)
    y_line = m * x + b
    distance = int(abs(y_line - y) + 0.5) 
    if distance < thickness / 2 :
      setColor(pixel, color)

#Function 4
#This function makes the color of the picture more red, so it looks like
#there are red lights for the party.  
def redLights(picture):
  for p in getPixels(picture):
    Blue = getBlue(p)
    Red = getRed(p)
    Green = getGreen(p)
    setBlue(p, Blue/2)
    setRed(p, Red*1.25)
    setGreen(p, Green/2) 

#Function 5
#This function makes a circle to resemble a ball on the llama's back for him
#to play with at the party.
def circle(picture, xc, yc, radius, color) :
  pixels = getPixels(picture) 
  for pixel in pixels :
    x = getX(pixel)
    y = getY(pixel)
    distance = math.sqrt((x - xc)**2 + (y - yc)**2) 
    if distance < radius :
      setColor(pixel, color)
