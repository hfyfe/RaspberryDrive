from socket import *
import run_rc_car as picar

def createPiReceiver():
    serversocket = socket(AF_INET, SOCK_STREAM)
    port = 9000
    new_picar = picar.PiCar()
    serversocket.bind(('',port))
    serversocket.listen(5)
    print "New Server Created, listening on port " + str(port)
    while(1):
        (clientsocket, address) = serversocket.accept()
        print "accepted connection from " + str(address)
        while(1):
            transfer = clientsocket.recv(20)
            if not transfer: break
            if (transfer == "quit"):
              exit()
    else:
        transfer = transfer.split(';')
    if transfer == ['']: break
    print "received: " + str(transfer)
    inputParser(transfer[0].strip(),float(transfer[1]),new_picar)
    clientsocket.send("true")

def inputParser(command,number,car):
    print 'executing ' + command + ' for ' + str(number) +' seconds'
    if   command == "forward":
        car.go_forward(number)
    elif command == "backward":
        car.go_backward(number)
    elif command == "right":
        car.go_forward_right(number)
    elif command == "left":
        car.go_forward_left(number)
    elif command == "backward right":
        car.go_backward_wheels_right(number)
    elif command == "backward left":
        car.go_backward_wheels_left(number)
    elif command == "wheels right":
        car.turn_wheels_right(number)
    elif command == "wheels left":
        car.turn_wheels_left(number)
    else:
        car.stop()

createPiReceiver()
exit()