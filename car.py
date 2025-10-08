# setting the flag
Flag = True

# setting the initial car status
car_status = "stop"
while Flag:
    user_wish = input("Enter your commands for the car please: ").strip().lower()
    if user_wish == car_status:
        if car_status == "move":
            print("Car is already moving")
        else:
            print(f"Car is already {car_status}")
    elif user_wish == "start" and car_status != "stop":
        print("Car has to be stopped first to start")
    elif user_wish == "move" and car_status != "start":
        print("Car has to start first to move")
    elif user_wish == "stop" and car_status != "move":
        print("Car has to move first to stop")
    elif user_wish == "exit":
        Flag = False
    else:
        if (user_wish == "start" and car_status == "stop" or
                user_wish == "move" and car_status == "start" or
                user_wish == "stop" and car_status == "move"):
            car_status = user_wish
            if car_status == "move":
                print("Car is now moving")
            else:
                print(f"Car is now {car_status}")
