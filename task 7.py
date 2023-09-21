traffic_speed = [67,64,55,70]
for i in traffic_speed:
    if i > 70:
        print("Suspend Driver's license")
    elif 60<i<70:
        print("Issue a ticket")
    else:
        print("A car is good to go")
