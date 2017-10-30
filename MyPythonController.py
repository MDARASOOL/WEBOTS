# File:          MyPythonController.py
# Date:          30 oct 2017         
# Description:   e-puck robot 
# Author:        Md.A.Rasool    
# Modifications: version 1

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, LED, DistanceSensor
#
# or to import the entire module. Ex:
#  from controller import *
from controller import DifferentialWheels,LED,DistanceSensor,Camera,LightSensor

# Here is the main class of your controller.
# This class defines how to initialize and how to run your controller.
# Note that this class derives Robot and so inherits all its functions
Robot = DifferentialWheels()
  
  # User defined function for initializing and running
  # the MyPythonController class

    print("Robot is running")
    timestep=60
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  led = self.getLed('ledname')
    led=[0]*8
    count=0
    for i in range(8):
      name="led"+str(i)
      led[i]=LED(name)
      led[i].set(1)
      
    # initialize sensors ( ps0 to ps7) and we ned 2sensors left and right
    irLeft=DistanceSensor("ps7") 
    irRight=DistanceSensor("ps0")
    irLeft.enable(timestep) 
    irRight.enable(timestep)
    
    
    gsLeft=DistanceSensor("gs0")  
    gsCenter=DistanceSensor("gs0")  
    gsRigth=DistanceSensor("gs0")  
    gsLeft.enable(timestep) 
    gsCenter.enable(timestep) 
    gsRight.enable(timestep)
    
    camera = Camera("camera")
    camera.enable(timestep*2)
    print("camera width = ", Camera.getWidth(), "camera height = " ,Camera.getHeight() )
    
    robot.enableEncoders(timestep)
    print ( "LeftEncoder = ", robot.getLeftEncoder()  \n "RightEncoder = ", robot.getRightEncoder()  )
     
    # Main loop
    while robot.step(timestep)!= -1:
      # Perform a simulation step of 64 milliseconds
      # and leave the loop when the simulation is over
      
        
      
      # Read the sensors:
      # Enter here functions to read sensor data, like:
      #  val = ds.getValue()
      
      print ("IR DISTANCES : Left=", irLeft.getValue() ,
      "IR DISTANCES : Right=", irRight.getValue())
      
      # Process sensor data here.
      
       print ("line sensor : Left=", gsLeft.getValue() ,
               "center = "gsCenter.getValue() , 
               "Right = "gsRight.getValue())
      
      # Enter here functions to send actuator commands, like:
      #  led.set(1)
      
      
      image= camera.getImage()
      robot.setSpeed(-100,100)
      
      led[i//10].set(0)
      i=+1
      if i>=80: i = 0
      led[i//10].set(1)
    # Enter here exit cleanup code

# The main program starts from here

# This is the main program of your controller.
# It creates an instance of your Robot subclass, launches its
# function(s) and destroys it at the end of the execution.
# Note that only one instance of Robot should be created in
# a controller program.

