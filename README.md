# Raspberry Drive

### Purpose
Raspberry Drive was developed with the goal of creating an Autonomous Car. Utilizing Raspberry Pis and image recognition software, the car is able to detect obstacles and respond appropriately. 

The car sends a picture to the server. The server then analyzes and sends the command to a second Raspberry Pi, which passes that command to the car utilizing GPIO pins. 

### Built With
- Raspberry Pi
- PiCamera
- Python
- OpenCV / SimpleCV

### Developed by:
- Greg Garner
- Henry Fyfe
- Will Farrell
- John Warshaw

### License
Raspberry Drive is released under the [MIT License](https://opensource.org/licenses/MIT)

## To Run

1. Clone Repo
2. Run python controller/controller.py