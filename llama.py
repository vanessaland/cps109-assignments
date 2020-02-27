#LLAMA---------------------------
llama = '/Users/vanessalandayan/Downloads/CPS109/mediasources-4ed/llama.jpg'
llamapic = makePicture(llama)

def llamaPic():
  addBox(llamapic)
  addBox2(llamapic, 260, 80, 290, 110, yellow)
  addCircle(llamapic, 290, 230, 30, green)
  addLine(llamapic, 0, 50, 100, 50)
  addLine(llamapic, 0, 100, 100, 100)
  addLine(llamapic, 0, 150, 100, 150)
  addLine(llamapic, 0, 200, 100, 200)
  addLine(llamapic, 0, 250, 100, 250)
  addLine(llamapic, 0, 300, 100, 300)
  addLine(llamapic, 0, 350, 100, 350)
  addLine2(llamapic, 0, 20, 359, 20, 20, pink)
  show(llamapic)
    
#-Function 1-----------------------------
# This function puts a red box on the llama 
# First explore to find the coordinates
def addBox(picture) :
  pixels = getPixels(picture) 
  for pixel in pixels :
     x = getX(pixel)
     y = getY(pixel)
     if 171 < x < 233 and 152 < y < 200 :
       setColor(pixel, red) 
       
#-Function 2-----------------------------
# Function addBox2 is a parameterization so that we can put a 
# box of a given color anywhere
def addBox2(picture, x1, y1, x2, y2, color) :
  pixels = getPixels(picture)
  for pixel in pixels:
    X = getX(pixel)
    Y = getY(pixel)
    if x1 < X < x2 and y1 < Y < y2 :
      setColor(pixel, color)

#-Function 3-----------------------------
# Add a circle of a given radius and color 
def addCircle(picture, xc, yc, radius, color) :
  pixels = getPixels(picture) 
  for pixel in pixels :
    x = getX(pixel)
    y = getY(pixel)
    distance = math.sqrt((x - xc)**2 + (y - yc)**2) 
    if distance < radius :
      setColor(pixel, color)
      
#-Function 4-----------------------------
# Draw a black line on the picture, given two points defining the line # Given two points on a line: (x1, y1), (x2, y2)
# the slope is m = (y2 - y1) / (x2 - x1)
# the intercept is b = y1 - m * x1
# the line is y = m * x + b
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

#-Function 5-----------------------------
# Draw a line on the picture, given two points defining the line
# and a parameter defining the thickness, and a parameter for color # Given two points on a line: (x1, y1), (x2, y2)
# the slope is m = (y2 - y1) / (x2 - x1)
# the intercept is b = y1 - m * x1
# the line is y = m * x + b
def addLine2(picture, x1, y1, x2, y2, thickness, color) : 
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

