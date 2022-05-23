from geopy.geocoders import Nominatim
from geopy import distance


#Creating a funtion that will ask the user to enter their registration details.
def rider_details():

    #Requesting user input.
    name = input("Please enter your name: ") 
    surname = input("Please enter your surname: ")
    payment = input("Please enter the method of payment you will be using (card/cash): ")
    
    #Displaying the registration information.
    print(f"""Name: {name}
Surname: {surname}
Payment type: {payment}""")


#Creating a function that will allow the user to book a ride.
def book_ride():
    # PLEASE NOTE THAT THE PROGRAM NAME HAS TO BE THE SAME AS THE USER AGENT
    geolocator = Nominatim(user_agent="test.py")
    #Requesting user input.
    location = geolocator.geocode(input("Enter your location (4 Station Road RSA)"))
    destination = geolocator.geocode(input("Enter your destination (112 Loop Street RSA)"))

    location_1 = (location.latitude, location.longitude)
    destination_1 = (destination.latitude, destination.longitude)
    book_ride.distance = distance.distance(location_1, destination_1).km


    ride_type = input("Please choose which type of ride you would like (cheap, comfort, luxury)")
    if ride_type.lower() =="luxury" :
            book_ride.distance*=2
    if ride_type.lower() == "cheap" :
            book_ride.distance-=5
    if ride_type.lower() == "comfort" :
            book_ride.distance +=5
    else :
            print("Please go back and choose your ride type again")


    #Dispplaying the ride details.
    print(f"""Location: {location.address}
Destination: {destination.address}
Type of ride: {ride_type}""")


#Creating a function to calculate the cost of the ride.
def calc_ride():
    calc_ride.out = format(((book_ride.distance+20)*1.62),".2f")
    print(f"Your final price is: R{calc_ride.out}")


        
    
#Creating a function that will allow the user to tip the driver.
def tip_driver():
    num = float(calc_ride.out)
    tip = float(input("How much would you like to tip the driver in Rands\n"))
   
    print (f"The Final amoint is {num + tip}")
    print("Thank you for tipping the driver!")

      


#Displaying a welcome message.
print("Welcome to the Uber-Lite Program!")

#Creating a while loop that will continually execute allowing the user to choose more than 1 option from the menu.
while True:

    #The 'try' statement to ensure that the user enters the correct corresponding numbers from the menu.
    try:

        #Asking the user to select an option from the menu.
        choice = int(input("Please select one of the following option: \n 1 - Enter rider details \n 2 - Book a ride \n 3 - Calculate the ride fare \n 4 - Tip the driver \n :"))

        #Calling the corresponding function of the option that was entered by the user.
        if choice == 1:
            rider_details()

        if choice == 2:
            book_ride()

        if choice == 3:
            calc_ride()

        if choice == 4:
            tip_driver()
            break;
        
    #The 'except statement' will handle any errors found in the code.
    except ValueError:
        print("Please try again.")
    


    
