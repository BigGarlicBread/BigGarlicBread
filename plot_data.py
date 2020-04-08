import requests
import json
import matplotlib.pyplot as plt
import numpy as np
import datetime

def request_plots(user_code_temp):

    try:
        url_temp = "https://corona.lmao.ninja/countries/" + user_code_temp

        payload = {}
        headers= {}

        response = requests.request("GET", url_temp, headers=headers, data = payload)

        data_temp = response.text.encode('utf8')
        js_temp = json.loads(data_temp)

        user_code = js_temp['countryInfo']['iso2']
        country_name = js_temp['country']
        #--------------------------------------------------------------------------

        url = "https://covid-19-report-api.now.sh/api/v1/cases/timeseries?iso=" + user_code

        payload = {}
        headers= {}

        response = requests.request("GET", url, headers=headers, data = payload)

        data = response.text.encode('utf8')
        js = json.loads(data)

        totalcases = []
        totalrecovery = []
        totaldeaths = []
        dailycases = []
        dailydeaths = []
        x_values = []

        case_now = 0
        case_prev = 0
        death_now = 0
        death_prev = 0

        for i in js['data'][0]['timeseries'].keys():
            if i == 'stat':
                break

            totalcases.append(js['data'][0]['timeseries'][i]['confirmed'])

            case_now = int(js['data'][0]['timeseries'][i]['confirmed'])
            dailycases.append(abs(case_now - case_prev))

            totaldeaths.append(js['data'][0]['timeseries'][i]['deaths'])

            death_now = int(js['data'][0]['timeseries'][i]['deaths'])
            dailydeaths.append(abs(death_now - death_prev))

            try:
                totalrecovery.append(js['data'][0]['timeseries'][i]['recovered'])
            except:
                totalrecovery.append(None)

            case_prev = int(js['data'][0]['timeseries'][i]['confirmed'])
            death_prev = int(js['data'][0]['timeseries'][i]['deaths'])

            x_values.append(i)

        dates = [datetime.datetime.strptime(d, "%m/%d/%y").date() for d in x_values]

        plot_data = [totalcases, totalrecovery, totaldeaths, dailycases, dailydeaths, dates, country_name]

    except:
        plot_data = ['0']

    return(plot_data)
