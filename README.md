# weather_full_stack
A seperate microservice for UI and API to find weather of city by redirecting it to a website.
 
# Running the project
1.Open terminal/cmd and direct it to a folder of weather_ui and run the project on port 8001 by typing "python manage.py runserver 8001"

2. Open another terminal and redirect it to weather_api and run the project on port 8000 by typing "python manage.py runserver 8000".

# How to get data
Open browser with port 8001 and enter the name of city.

# How it operates
The city name is send to a google search by adding as tring "weather". The first url is extracted and a pop up appears on the browse with permission to redirect. Once you hit ok it will be redirected to another website
