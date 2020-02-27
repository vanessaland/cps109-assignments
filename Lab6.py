#1
def blueAndGold(picture):
  bottom = getHeight(picture) - 10
  for px in getPixels(picture):
    y = getY(px)
    if y < 10:
      setColor(px, blue)
    if y > bottom:
      setColor(px, blue)
  right = getWidth(picture) - 10
  gold = makeColor(212, 175, 55)
  for px in getPixels(picture):
    x = getX(px)
    if x < 10:
      setColor(px, gold)
    if x > right:
      setColor(px, gold)

#2
def purpleTeeth(picture):
  pixels = getPixels(picture)
  for pixel in pixels:
    R = getRed(pixel)
    G = getGreen(pixel)
    B = getBlue(pixel)
    Y = getY(pixel)
    X = getX(pixel)
    if R > 180 and 298 < Y < 323 and 160 < X < 261 and G > 150 and B > 155:
      setRed(pixel, R*1.5)
      setGreen(pixel, 0)
      setBlue(pixel, B*2)
  show(picture)    

#3
def checkLuminance(r,g,b):
  luminance = (r*0.3)+(g*0.6)+(b*0.1)
  if luminance < 10:
    print "That's going to be awfully dark."
  elif 50 < luminance < 200:
    print "Looks like a good range."
  elif luminance > 250:
    print "That's nearly white."
  
#4
def chromakeyBlueAbove(picture, background, skyY):
  pixels = getPixels(picture)
  for pixel in pixels:
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    y = getY(pixel)
    x = getX(pixel)
    if ((r+g) < (b+140)) and y < skyY:
      bgpx = getPixel(background, x, y)
      bgcol = getColor(bgpx)
      setColor(pixel, bgcol)

#5
def interleave(picture1, picture2):
  W = getWidth(picture1)
  H = getHeight(picture1)
  canvas = makeEmptyPicture(W,H)
  canvaspx = getPixels(canvas)
  pixels1 = getPixels(picture1)
  pixels2 = getPixels(picture2)
  
  for pixel in canvaspx:
    x = getX(pixel)
    y = getY(pixel)
    tester = x % 40
    if tester <= 19 :
      pic1Pixel = getPixel(picture1,x,y)
      pic1Color = getColor(pic1Pixel)
      setColor(pixel,pic1Color)
    elif tester < 40:
      pic2Pixel = getPixel(picture2,x,y)
      pic2Color = getColor(pic2Pixel)
      setColor(pixel, pic2Color)
      
  explore(canvas)

#6
def getRegion(picture, x1, y1, x2, y2):
  W = getWidth(picture)
  H = getHeight(picture)
  canvas = makeEmptyPicture(W, H)
  canvaspx = getPixels(canvas)
  picpixels = getPixels(picture)
  for px in picpixels:
    x = getX(px)
    y = getY(px)
    picColor = getColor(px)
    if x1 <= x <= x2 and y1 <= y <= y2:
      pixelcanvas = getPixel(canvas, x, y)
      setColor(pixelcanvas, picColor)
  show(canvas)

#7
def getRegionTwice(picture, x1,y1,x2,y2):
  W = getWidth(picture)
  H = getHeight(picture)
  xrange = x2 - x1
  yrange = y2 - y1
  canvas = makeEmptyPicture(W, H)
  canvaspx = getPixels(canvas)
  picpixels = getPixels(picture)
  for px in picpixels:
    x = getX(px)
    y = getY(px)
    picColor = getColor(px)
    if x1 <= x <= x2 and y1 <= y <= y2:
      pixelcanvas = getPixel(canvas, x, y)
      pixelcanvas2 = getPixel(canvas, x, y+yrange)
      setColor(pixelcanvas, picColor)
      setColor(pixelcanvas2, picColor)
  show(canvas)
           
    
    
      