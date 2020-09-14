#1.
def changeColor(picture, amount, rgbNumber):
  pixels = getPixels(picture)
  for pixel in pixels:
    if rgbNumber == 1: #red
      r = (getRed(pixel) * amount) + getRed(pixel)
      setRed(pixel, r)
      
    if rgbNumber == 2: #green
      g = (getGreen(pixel) * amount) + getGreen(pixel)
      setGreen(pixel, g)
      
    if rgbNumber == 3: #blue
      b = (getBlue(pixel) * amount) + getBlue(pixel)
      setBlue(pixel, b)
      
#2.
def posterize8(picture):
  pixels = getPixels(picture)
  for pixel in pixles:
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    
    if r < 100:
      setRed(pixel, 0)
    else:
      setRed(pixel, 255)
    
    if g < 100:
      setGreen(pixel, 0)
    else:
      setGreen(pixel, 255)
      
    if b < 100:
      setBlue(pixel, 0)
    else:
      setBlue(pixel, 255)
      
#3.
def border(picture, borderwidth, bordercolor):
  bottom = getHeight(picture) - borderwidth
  for px in getPixels(picture):
    y = getY(px)
    if y < borderwidth:
      setColor(px, bordercolor)
    if y > bottom:
      setColor(px, bordercolor)
  right = getWidth(picture) - borderwidth
  for px in getPixels(picture):
    x = getX(px)
    if x < borderwidth:
      setColor(px, bordercolor)
    if x > right:
      setColor(px, bordercolor)

#4.
def drawXequalsYline(picture, color):
  pixels = getPixels(picture)
  for pixel in pixels:
    x = getX(pixel)
    y = getY(pixel)
    if x == y:
      setColor(pixel, color)

#5
def drawQuadrants(picture, color):
  pixels = getPixels(picture)
  W = getWidth(picture)
  H = getHeight(picture)
  for pixel in pixels:
    x = getX(pixel)
    y = getY(pixel)
    if x == W/2:
      setColor(pixel, color)
    if y == H/2:
      setColor(pixel, color)
      
#6
def drawDiagonalLine2(picture, color):
  pixels = getPixels(picture)
  W = getWidth(picture)
  H = getHeight(picture)
  for pixel in pixels:
    x = getX(pixel)
    y = getY(pixel)
    line = int(H/W) * x
    if y == line:
      setColor(pixel,color)

#7
def posterize3(picture):
  pixels = getPixels(picture)
  for pixel in pixels:
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
  
    if r > 180:
      setColor(pixel, red)
    elif b > 180:
      setColor(pixel, blue)
    elif g > 180:
      setColor(pixel, green)
    else:
      setColor(pixel, black)

#8
def pinkify(picture):
  pixels = getPixels(picture)
  for pixel in pixels:
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    
    if r > 100 and g > 100 and b > 100:
      setColor(pixel, pink)
    
#9
def downupRed(picture):
  pixels = getPixels(picture)
  W = getWidth(picture)

  for pixel in pixels:
    x = getX(pixel)
    if x < W/2:
      setRed(pixel, getRed(pixel)*0.5)
    else:
      setRed(pixel, getRed(pixel)*2)
  
#10
def thirds(picture):
  pixels = getPixels(picture)
  H = getHeight(picture)
  for pixel in pixels:
    y = getY(pixel)
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    color = getColor(pixel)
    if y <= H/3:
      color = makeLighter(color)
      setColor(pixel, color)
    elif H/3 < y < (H/3)*2:
      setRed(pixel, r*0.7)
      setGreen(pixel, g*0.7)
    elif y >= (H/3)*2:
      negColor=makeColor(255-r, 255-g, 255-b)
      setColor(pixel,negColor)     
        