command =""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else: 
            started = True
            print("Car started successfully...")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else: 
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
start - car started
stop - car stopped
quit - to quit
              """
           )
    elif command == "quit":
        break
    else: print("Sorry, I don't understand")