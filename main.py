from flask import Flask, request, jsonify
import requests
import json
import urllib
import numpy as np
import datetime
app = Flask(__name__)

# from flask import Flask, request, jsonify



# app = Flask(__name__)


# @app.route('/api/wheather_forecast/', methods=['GET','POST'])
# def get_data_wheater_forecast_api():
#     location = request.args.get('location', default = '', type = str)
#     period = request.args.get('period', default = '', type = str)
    
#     params = {"q": "{}".format(location),
#               "units": "metric",
#               "cnt": "{}".format(period),
#               "appid": "4e93850ac268dce834aa12f633bb047d"}
    
#     url = "https://api.openweathermap.org/data/2.5/forecast/daily?" + urllib.parse.urlencode(params)
#     resp = requests.get(url, verify=False).json()
#     return jsonify(extract_average_temperature_forecast(resp))   #(resp.text, resp.status_code, resp.headers.items()) 

# def extract_average_temperature_forecast(data):
#     temperature = []
#     temperature_day = dict()
#     for day in data['list']: 
#         temperature.append(day['temp']['morn'])
#         temperature.append(day['temp']['eve'])
#         temperature.append(day['temp']['night'])
#         datum = datetime.datetime.fromtimestamp(day['dt']).date()
#         temperature_day[str(datum)]=np.mean(temperature)
#     return temperature_day


# @app.route('/api/wheather_history/', methods=['GET','POST'])
# def get_data_wheater_historic_api():
#     key = '2b1429258084a742'
#     location = request.args.get('location', default = '', type = str)
#     period = request.args.get('period', default = '', type = str)
#     url_list = create_urls_historic_wheater_api(key,location,period)
#     return jsonify(extract_average_temperature_historic(url_list))
    
# def create_urls_historic_wheater_api(key,location='Leiden',period='7'):
#     base = datetime.datetime.today() - datetime.timedelta(days=1)
#     date_list = [base - datetime.timedelta(days=x) for x in range(0, int(period))]
#     date_list = [date.strftime('%Y%m%d') for date in date_list]
#     url_list = ['http://api.wunderground.com/api/{}/history_{}/q/CA/{}.json'\
#                 .format(key,date,location) for date in date_list]
#     return url_list

# def extract_average_temperature_historic(url_list):
#     temperature_day = dict()
#     for url in url_list:
#         resp = requests.get(url=url)
#         data = json.loads(resp.text)
#         temperature = data['history']['dailysummary'][0]['meantempm']
#         datum = datetime.datetime.strptime(data['history']['utcdate']['pretty'],'%B %d, %Y').date()
#         temperature_day[str(datum)]=temperature
#     return temperature_day



@app.route('/')
def hello_world():
  return 'Check another change if we can see this change!'

if __name__ == '__main__':
  app.run()
