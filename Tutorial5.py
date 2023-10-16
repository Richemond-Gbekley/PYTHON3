#command = ""
started = False
while True:
        command = input("> ").lower()
        if command == "start":
           # print("car start")
            if started :
                print("Car is already started")
            else:
                 if started == False :
                     print("Car Start")
               
                              
        elif  command == "stop" :
            if not started:
              print("Car already stopped")
        #if not started:
         #    print("Car already stopped")
            else:
             started = False 
             print("car stopped")
         
         
        elif command == "quit":
                break
        elif command == "help":
                 print('''
Start - to start the car
Stop - to stop the car
Quit - to quit
              ''')
        else:
             print("sorry i dont understand that")
    