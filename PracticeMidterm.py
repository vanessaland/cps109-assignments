def factorRed(picture, factor):
  pixels = getPixels(picture)
  if factor < 0:
    for pixel in pixels:
      Red = getRed(pixel) * (1 + factor)
      setRed(pixel, Red)
  elif factor > 0:
    for pixel in pixels:
      Red = getRed(pixel) * factor
      setRed(pixel, Red)  

def dull(picture):
  pixels = getPixels(picture)
  for pixel in pixels:
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    
    if r > 125:
      setRed(pixel, 125)
    if g > 125:
      setGreen(pixel, 125)
    if b > 125:
      setBlue(pixel, 125)

def sumOfRed(picture):
  pixels = getPixels(picture)
  sum = 0
  for pixel in pixels:
    r = getRed(pixel)
    sum += r
  return sum
  
def border(picture, borderwidth, bordercolor):
  w = getWidth(picture) - 1
  h = getHeight(picture) - 1
  pixels = getPixels(picture)
  
  for pixel in pixels:
    y = getY(pixel)
    x = getX(pixel)
    
    if 0 <= y <= borderwidth or h-borderwidth <= y <= h:
      setColor(pixel, bordercolor)
    if 0 <= x <= borderwidth or w-borderwidth <= x <= w:  
      setColor(pixel, bordercolor)
      
def drawXequalsYline(picture, color):
  pixels = getPixels(picture)
  w = getWidth(picture)
  h = getHeight(picture)

  for pixel in pixels:
    y = getY(pixel)
    x = getX(pixel)

    if x == y:
      setColor(pixel, color)

def drawQuadrants(picture, color):
  w = getWidth(picture)
  h = getHeight(picture)
  yaxis = w/2 
  xaxis = h/2
  pixels = getPixels(picture)
  for pixel in pixels:
    y = getY(pixel)
    x = getX(pixel)
    
    if y == xaxis:
      setColor(pixel, color)
    if x == yaxis:
      setColor(pixel, color)

def posterize3(picture):
  pixels = getPixels(picture)
  for pixel in pixels:
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    
    if r > 180:
      setColor(pixel,red)
    elif b > 180:
      setColor(pixel, blue)
    elif g > 180:
      setColor(pixel, green)
    else:
      setColor(pixel, black)
      
def posterize4(picture):
  pixels = getPixels(picture)
  for pixel in pixels:
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)   
    
    if r >= g and r >= b:
      setColor(pixel, red)
    elif g >= r and g >= b:
      setColor(pixel, green)
    else:
      setColor(pixel, blue)    
      
def pinkify(picture):
  pixels = getPixels(picture)
  for pixel in pixels:
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)   
    
    if r > 100 and g > 100 and b > 100:
      setColor(pixel, pink)      
      
def downupRed(picture):
  pixels = getPixels(picture)
  w = getWidth(picture)
  for pixel in pixels:
    r = getRed(pixel)
    x = getX(pixel)
    
    if 0 <= x <= w/2:
      r *= 0.5
      setRed(pixel, r)
    if x > w/2:
      r *= 2 
      if r > 255:
        r = 255      
      setRed(pixel, r)

def thirds(picture):
  h = getHeight(picture)
  pixels = getPixels(picture)
  
  for pixel in pixels:
    y = getY(pixel)
    
    if y < h/3:
      color = getColor(pixel)
      newColor = makeLighter(color)
      setColor(pixel, newColor)
    if y > 2*h/3:
      color = getColor(pixel)
      newColor = makeDarker(color)
      setColor(pixel, newColor)