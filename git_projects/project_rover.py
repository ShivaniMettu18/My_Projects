# # project.py
# from dronekit import connect, VehicleMode
# import time
# connection_string = 'COM9' # Replace with the serial port of your Pixhawk
# baud_rate = 57600 # Replace with the baud rate that your Pixhawk is configured to use
# vehicle = connect(connection_string, baud=baud_rate, wait_ready=False)

# # Set the mode of the vehicle to MANUAL
# vehicle.mode = VehicleMode("MANUAL")

# # Arm the vehicle
# vehicle.armed = True

# # Move forward
# def square(d):
#   for i in range(d):
#     vehicle.channels.overrides['3'] = 1800
#     vehicle.channels.overrides['1']=1800
#     time.sleep(1)
#   vehicle.channels.overrides['1']=1500
#   vehicle.channels.overrides['3']= 1500

#   # Turn right
#   vehicle.channels.overrides['3'] = 1600
#   vehicle.channels.overrides['1'] = 1400
#   time.sleep(0.46)
#   vehicle.channels.overrides['1'] = 1500
#   vehicle.channels.overrides['3'] = 1500

# d=int(input("Enter the side length"))
# for j in range(8):
#   square(d)
# vehicle.armed = False
# vehicle.close()
# exit()

from dronekit import connect, VehicleMode
import time

connection_string = 'COM9' # Replace with the serial port of your Pixhawk
baud_rate = 57600 # Replace with the baud rate that your Pixhawk is configured to use
vehicle = connect(connection_string, baud=baud_rate, wait_ready=False)

# Set the mode of the vehicle to MANUAL
vehicle.mode = VehicleMode("MANUAL")

# Arm the vehicle
vehicle.armed = True

# Move forward
def forward(d):
  for i in range(d):
    vehicle.channels.overrides['3'] = 1600
    vehicle.channels.overrides['1'] = 1600
    time.sleep(1)
  vehicle.channels.overrides['3'] = 1500
  vehicle.channels.overrides['1'] = 1500


#back
def backward(d):
  for i in range(d):
    vehicle.channels.overrides['3'] = 1400
    vehicle.channels.overrides['1'] = 1600
    time.sleep(1)
  vehicle.channels.overrides['3'] = 1500
  vehicle.channels.overrides['1'] = 1500

# Turn right
def right():
  vehicle.channels.overrides['3'] = 1900
  vehicle.channels.overrides['1'] = 1300
  time.sleep(0.41)
  vehicle.channels.overrides['1'] = 1500
  vehicle.channels.overrides['3'] = 1500


#left
def left():
  vehicle.channels.overrides['3'] = 1400
  vehicle.channels.overrides['1'] = 1400
  time.sleep(0.5)
  vehicle.channels.overrides['3'] = 1500
  vehicle.channels.overrides['1'] = 1500

while(1):
  print("1.Forward")
  print("2.Backward")
  print("3.Right")
  print("4.Left")
  print("5.Exit")
  c=int(input("Enter your choice:"))
  if c==1:
    d=int(input("Enter the distance"))
    forward(d)
  elif c==2:
    d=int(input("Enter the distance"))
    backward(d)
  elif c==3:
    right()
  elif c==4:
    left()
  elif c==5:
    vehicle.channels.overrides['3'] = 1500
    vehicle.channels.overrides['1'] = 1500
    vehicle.armed = False
    vehicle.close()
    exit()