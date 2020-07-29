import requests
import json
from add_comma_numbers import *



def request_latest_data(user_code):
    if user_code == 'world':
        url = "https://api.covid19api.com/summary"

        payload = {}
        headers= {}

        response = requests.request("GET", url, headers=headers, data = payload)

        data = response.text.encode('utf8')
        js = json.loads(data)

        world_total = add_comma(js['Global']['TotalConfirmed'])
        world_recovered = add_comma(js['Global']['TotalRecovered'])
        world_deaths = add_comma(js['Global']['TotalDeaths'])
        latest_data = [world_total, world_recovered, world_deaths]


        return latest_data

    else:

        try:
            url = "https://corona.lmao.ninja/v3/covid-19/countries/" + user_code

            payload = {}
            headers= {}

            response = requests.request("GET", url, headers=headers, data = payload)

            data = response.text.encode('utf8')
            js = json.loads(data)

            flag_warn = 0
            total_cases = js['cases']
            recoveries = js['recovered']
            deaths = js['deaths']
            active = js['active']
            cases_per_1m = js['casesPerOneMillion']
            deaths_per_1m = js['deathsPerOneMillion']
            tests = js['tests']
            test_per_1m = js['testsPerOneMillion']
            last_updated = js['updated']
            country = js['country']
            flag = js['countryInfo']['flag']

            if int(tests) == 0:
                tests = 'No Data'
                test_per_1m = 'No Data'
                flag_warn = 1

            if int(deaths) == 0:
                deaths_per_1m = '0'

            latest_data = [total_cases, recoveries, deaths, active, cases_per_1m, deaths_per_1m, tests, test_per_1m, country, flag]

            if flag_warn == 1:
                for i in range (len(latest_data) - 4):
                    latest_data[i] = add_comma(latest_data[i])

            else:
                for i in range (len(latest_data) - 2):
                    latest_data[i] = add_comma(latest_data[i])

        except:
            latest_data = ['N/A', 'N/A','N/A','N/A','N/A','N/A','N/A','N/A', 'Invalid Country!', '0']
        return latest_data
