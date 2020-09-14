#ALICE FUN
#This function changes the photo of Alice to make her look like she's in a different world.
def aliceFun():
  alice = makePicture('/Users/vanessalandayan/Downloads/CPS109/mediasources-4ed/Alice.jpg')
  background = makePicture('/Users/vanessalandayan/Downloads/TheCreationOfAdam.jpg')
  backgroundSwitch(alice, background)
  addLine(alice, 0, 0, 10, 10)
  colorHalf(alice)
  yellowBackground(alice)
  border(alice)
  show(alice)
  
  
#Function 16
#This function changes the background of the image and makes the photo all brighter.
def backgroundSwitch(source,bg):
  for px in getPixels(source):
    x = getX(px)
    y = getY(px)
    if (getRed(px) + getBlue(px) < getGreen(px)):
      bgpx = getPixel(bg,x,y)
      bgcol = getColor(bgpx)
      setColor(px,bgcol)
    r = getRed(px)
    g = getGreen(px)
    b = getBlue(px)
    newcol = makeColor(r*1.2, g*1.2, b*1.2)
    setColor(px, newcol)

#Function 17
#This function adds a line to the photo
def addLine(picture, x1, y1, x2, y2) : 
  pixels = getPixels(picture)
  m = 1.0 * (y2 - y1) / (x2 - x1)
  b = y1 - m * x1
  for pixel in pixels : 
    x = getX(pixel)
    y = getY(pixel) 
    y_line = m * x + b 
    if y == y_line :
      setColor(pixel, black)

#Function 18
#This function nagates the top half of the picture with also changing the RGB values.
def negateColorHalf(picture):
  pixels = getPixels(picture)
  for px in range (0, len(pixels)/2):
    i = pixels[px]
    red=getRed(i)
    green=getGreen(i)
    blue=getBlue(i)
    negColor=makeColor((255-red)*2, (255-green)*0.75, (255-blue)*0.5)
    setColor(i,negColor)

#Function 19
#This function makes the bottom half of the picture bright yellow.
def yellowBackground(picture):
  pixels = getPixels(picture)
  for px in range (len(pixels)/2, len(pixels)-1):
    i = pixels[px]
    red=getRed(i)
    green=getGreen(i)
    blue=getBlue(i)
    color=makeColor(red*2, green*2, 0)
    setColor(i,color)
    
#Function 20
#This function adds a black border to the top and bottom of the image 
def border(picture) : 
  pixels = getPixels(picture)
  x2 = getWidth(picture)-1
  y2 = 0
  m = 0
  b = 0
  thickness = 100
  for pixel in pixels : 
    x = getX(pixel)
    y = getY(pixel)
    y_line = m * x + b
    distance = int(abs(y_line - y) + 0.5) 
    if distance < thickness / 2 :
      setColor(pixel, black)
      
  x2 = 0
  y2 = getHeight(picture)-1
  m = 0
  b = getHeight(picture)-1

  for pixel in pixels : 
    x = getX(pixel)
    y = getY(pixel)
    y_line = m * x + b
    distance = int(abs(y_line - y) + 0.5) 
    if distance < thickness / 2 :
      setColor(pixel, black)
      
  


