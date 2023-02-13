import random
import pandas as pd
import requests as r
import datetime as dt


def get_random_quote():
  df = pd.read_csv('Quotes.csv')
  lists = ['quotes', 'authors', 'URL']
  quotes_only = df.loc[:, lists]
  random_df = quotes_only.sample()
  dicts = random_df.to_dict('list')
  return dicts


def get_stock():
  token = "zjNUF4abiX0eUwDn1Kl9GCKGNB50sWc4KcfJxHMO"
  url = f"https://api.marketaux.com/v1/news/all?symbols=TSLA,AMZN,MSFT&filter_entities=true&language=en&api_token={token}"
  data = r.get(url).json()
  title = data['data'][0]["title"]
  snippet = data['data'][0]["snippet"]
  snippet = ''.join(snippet.splitlines())
  url0 = data['data'][0]["url"]
  stock_data = {
    'title': title,
    'snippet': snippet,
    'url0': url0,
  }
  return stock_data


def get_weather_forecast():
  api_key = 'd242f826443de65584d2d0a8ee695543'
  location = 'sungai besar'
  url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
  data = r.get(url).json()
  kelvin = data['main']['temp']
  celcius = kelvin - 273.15
  weather_discription = data['weather'][0]['description']
  icon = data['weather'][0]['icon']
  URL_icon = f'https://openweathermap.org/img/wn/{icon}d@2x.png'
  img_data = r.get(URL_icon).content
  country_code = data['sys']['country']
  location_name = data['name']
  sun_rise = dt.datetime.utcfromtimestamp(data['sys']['sunrise'] +
                                          data['timezone'])
  sun_set = dt.datetime.utcfromtimestamp(data['sys']['sunset'] +
                                         data['timezone'])
  weather_data = {
    'celcius': celcius,
    'weather_discription': weather_discription,
    'country_code': country_code,
    'location_name': location_name,
    'sun_rise': sun_rise,
    'sun_set': sun_set,
    'img_data': img_data
  }
  return weather_data


def get_response(message: str) -> str:
  p_message = message.lower()
  quote = get_random_quote()
  eco = get_stock()
  weather = get_weather_forecast()
  list_ = ['tek cik', 'nek cik', 'sigma']
  nl = '\n'

  if p_message == 'quote':
    return f'Quote of the day: {quote["quotes"][0]} by {quote["authors"][0]} - read more: {quote["URL"][0]}'

  if p_message == 'weather':
    return f'Weather location at {weather["country_code"]} , {weather["location_name"]} on {dt.date.today().strftime("%d %b %Y")}: \nWeather condition is {weather["weather_discription"]}, with temperature {weather["celcius"]:.2f}°C {nl}Sunrise time: {weather["sun_rise"]} {nl}Sunset time: {weather["sun_set"]}'

  if p_message == 'stock':
    return f'~*~Today Economic News~*~{nl}Title: {eco["title"]}{nl}Snippet: {eco["snippet"]}{nl}Read more at {eco["url0"]}'

  if message == 'roll':
    return str(random.randint(1, 6))

  if any(word in p_message for word in list_):
    return f'hahahahah {p_message} xD'

  if p_message == '!help':
    return f'`Here is the command that you can call:{nl}"quote" - to give quote of the day{nl}"weather" - give current weather condition{nl}"stock" - to give latest economic news {nl}"roll" - give dice random number (from 1 to 6){nl}"?" - bot will message you personally`'
