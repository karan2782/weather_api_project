'''---This Project is about how we can find temperature using API'''

# here I am imporing requests which is useful for our project
import requests


# here I am taking while because If we want to know temperature more than one city, so we can do this through loop
while True:

    print("If you don't want to know tempertaure! Please enter |exit|: ")
    print("If you want to know temperatue! |Press any key|")

    # here I am taking choose variable If we enter exit so this loop will end otherwise loop will be taking again input of city
    choose = input("Enter: ")
    if choose=="exit":
        break

    # here enter name a city
    city = input("Enter the name of city: ")
    print("\n")

    # here we paste api_key which is copied from  website
    api_key = "07f74d20ca3e60e791f6eca11cdcc317"

    # this is function for get temperatue of city
    def get_weather(api_key, city):

        #here make a variable which name is url , here I am taking url of api website for temperature
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        # response take requests from url
        response = requests.get(url)

        # for check status code
        status = response.status_code

        # here we are checking our status_code is right or not
        if status==200:
            data = response.json()
            temp = data['main']['temp']
            temp_to_cel = temp-273.15  # convert kelvin to celsius
            print(f"The temperature in {city} is {int(temp_to_cel)}℃")
            print("\n")
        else:
            print(f"{status} error! please check your city name. If you choose correct city name, so you must check your url!")

    # here  call  function to get temperature of desired city
    get_weather(api_key, city)
