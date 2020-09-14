def compute() :
    distanceInMiles = 3279.8
    metersPerMile = 1609.34
    distanceInMeters = distanceInMiles * metersPerMile
    turtleSpeed = 0.5
    timeSeconds = distanceInMeters/turtleSpeed
    print('Time in seconds for turtle to go from Miami to Seattle')
    print(timeSeconds)
    minutes = timeSeconds/60
    print(minutes)
    hours = minutes/60
    days = hours/24
    weeks = days/7
    print("In weeks")
    print weeks

    