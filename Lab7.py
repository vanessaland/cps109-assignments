#1
def addSunset():
  beach = makePicture('/Users/vanessalandayan/Downloads/CPS109/mediasources-4ed/beach.jpg')
  beach.addArcFilled(orange, 200, 165, 50, 50, -4, 169)
  show(beach)

#2
def addBullseye(picture, x1, y1, width):
  pixels = getPixels(picture) 
  for pixel in pixels :
    x = getX(pixel)
    y = getY(pixel)
    distance = math.sqrt((x - x1)**2 + (y - y1)**2) 
    if distance < width :
      setColor(pixel, red)

    distance = math.sqrt((x - x1)**2 + (y - y1)**2) 
    if distance < (width*0.75) :
      setColor(pixel, blue)
    
    distance = math.sqrt((x - x1)**2 + (y - y1)**2) 
    if distance < (width*0.40) :
      setColor(pixel, yellow)
  show(picture)
      
#3
def addHouse (x1, y1):
  picture = makeEmptyPicture(500, 500)
  pixels = getPixels(picture)
  
  for pixel in pixels:
    setColor(pixel, white)
    
  for i in range(0,6):
  
    for j in range(0, 6):
      addRectFilled(picture, x1, y1, 50, 50, green)
      addRectFilled(picture, x1+15, y1+10, 15, 15, yellow)
      addRectFilled(picture, x1+35, y1+10, 15, 15, yellow)
      addRectFilled(picture, x1+30, y1+30, 15, 20, red)
      addLine(picture, x1, y1, x1+25, y1-30)
      addLine(picture, x1+20, y1-30, x1+50, y1)
    
      y1 = y1 + 80
    y1 = y1 - 480
    x1 = x1 + 80 
  show(picture)
  
#4 
def drawGrid(picture, spacing):
  height = getHeight(picture)
  width = getWidth(picture)
  y1 = 0
  y2 = 0
  x1 = 0
  x2 = 0
  
  for i in range(0, (height/spacing)):
    addLine(picture, 0, y1, width-1, y2)
    y1 += spacing
    y2 += spacing
   
  for i in range(0, (width/spacing)):
    addLine(picture, x1, 0, x2, height-1)
    x1 += spacing
    x2 += spacing
  show(picture)
  
#5
def drawGrid2(picture):
  height = getHeight(picture)
  width = getWidth(picture)
  y1 = 0
  y2 = 0
  x1 = 0
  x2 = 0
  spacing = 5
  for i in range(0, (height/spacing)):
    addLine(picture, 0, y1, width-1, y2)
    y1 += spacing
    y2 += spacing
    spacing += 3
  spacing = 5 
  for i in range(0, (width/spacing)):
    addLine(picture, x1, 0, x2, height-1)
    x1 += spacing
    x2 += spacing
    spacing += 3
  show(picture) 
  
#6
def flipHorizontally(picture):
  width = getWidth(picture)
  height = getHeight(picture)
  
  canvas = makeEmptyPicture(width-1, height)
  pixels = getPixels(picture)
   
  canvasX = 0
  for picX in range(width-1, 0, -1):
    canvasY = 0
    for picY in range(0, height):
      color = getColor(getPixel(picture, picX, picY))
      setColor(getPixel(canvas, canvasX, canvasY), color)
      canvasY += 1
    canvasX += 1
  show(canvas)
  
#7
def scaleup(picture):
  width = getWidth(picture)
  height = getHeight(picture)
  
  canvas = makeEmptyPicture(width*2, height*2)
  pixels = getPixels(picture)
   
  picX = 0
  for canvasX in range(0, width*2):
    picY = 0
    for canvasY in range(0, height*2):
      color = getColor(getPixel(picture, int(picX), int(picY)))
      setColor(getPixel(canvas, canvasX, canvasY), color)
      canvasY += 1
      picY += 0.5
      
    canvasX += 1
    picX += 0.5
  show(canvas)

#8
def scaledown(picture):
  width = getWidth(picture)
  height = getHeight(picture)
  
  canvas = makeEmptyPicture(width/2 + 1, height/2 + 1)
  pixels = getPixels(picture)
   
  canvasX = 0
  for picX in range(0, width,2):
    canvasY = 0
    for picY in range(0, height, 2):
      color = getColor(getPixel(picture, picX, picY))
      setColor(getPixel(canvas, canvasX, canvasY), color)
      canvasY += 1
    canvasX += 1
  show(canvas)
  
#9
def mirror20(picture):
  mirrorPoint = 20
  width = 40
  for y in range(0,getHeight(picture)):
    for x in range(0,mirrorPoint):
      leftPixel = getPixel(picture,x,y)
      rightPixel = getPixel(picture,width - x - 1,y)
      color = getColor(leftPixel)
      setColor(rightPixel,color)
  show(picture)
