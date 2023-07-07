import telegram
import time
import requests

# Replace TOKEN with your bot's token
bot = telegram.Bot(token='Your API Token')

def get_weather():
    # Get weather data from OpenWeatherMap
    city = "Kattangal" #change to your desired city
    country = "IN"
    api_key = "Your API Token"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}"
    weather_data = requests.get(url).json()


    # Get temperature in Celsius
    temperature = round(weather_data["main"]["temp"] - 273.15)
    description = weather_data["weather"][0]["description"]
    print(f"The weather in {city} is {temperature}°C and {description}")
    return f"The weather at NIT Calicut is <b>{temperature}°C</b> and <b>{description}</b>"

def get_inspirational_quote():
    # Get quote data from Forismatic
    url = "https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=text"
    quote_data = requests.get(url).text
    print(quote_data)
    return quote_data



def send_timetable_reminder():
    # Get the current day of the week
    day_of_week = time.strftime('%A')
    #day_of_week = "Wednesday"

    # This is an example timetable. You can replace this with your own timetable
    timetable = {
        'Monday': '8:00am - 9:00am: Biopharmaceutical Technology\n9:00am - 10:00am: Immunology\n10:00am - 11:00am: Enzyme kinetics and Technology\n11:00am - 12:00pm: Engineering Economics',
        'Tuesday': '9:00am - 10:00am: Enzyme kinetics and Technology\n10:00am - 11:00am: Engineering Economics\n11:00am - 12:00pm: Metabolic Engineering\n05:00pm - 06:00pm: Biopharmaceutical Technology',
        'Wednesday': '9:00am - 10:00am: Engineering Economics\n10:00am - 11:00am: Metabolic Engineering\n11:00am - 12:00pm: Instrumental Methods of Analysis\n12:00pm - 1:00pm: Biopharmaceutical Technology\n02:00pm - 05:00pm: Immunology Laboratory',
        'Thursday': '9:00am - 10:00am: Metabolic Engineering\n10:00am - 11:00am: Instrumental Methods of Analysis\n11:00am - 12:00pm: Immunology\n02:00pm - 05:00pm: Mini Project',
        'Friday': '9:00am - 10:00am: Instrumental Methods of Analysis\n10:00am - 11:00am: Immunology\n11:00am - 12:00pm: Enzyme kinetics and Technology'
    }#change according to your timetable in the given sample

    chat_id = ["17338xxxx"] #enter the chatid as a list
    name=["Sid","Mochx"] #enter the names of persons as a list
    msg=f'{get_weather()}  \n\nToday\'s Quote for you:\n{get_inspirational_quote()}\n\nHere is your timetable for {day_of_week}:\n{timetable[day_of_week]}\n\nHave a pleasant day ;)\n\n\n~~~~~~~~~~{day_of_week}~~~~~~~~~~'
    for i in range(1):
    # Send the reminder message to the user
        try:
            bot.send_message(chat_id=chat_id[i], text=f'~~~~~~~~~~{day_of_week}~~~~~~~~~~\n\n\nGood Morning <b><i>{name[i]}! </i></b>\n\n{msg}',parse_mode=telegram.ParseMode.HTML)
            print("messages sent")
        except:
            continue
    

send_timetable_reminder()

