import requests
import json

def get_data1():
    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-EB318A2B-32A0-447F-9E3B-3D129A05E43F&locationName=%E8%87%BA%E5%8D%97%E5%B8%82"
    params = {
        "Authorization": "CWB-EB318A2B-32A0-447F-9E3B-3D129A05E43F",
        "locationName": "台南市",
    }

    response = requests.get(url, params=params)
    print(response.status_code)

    if response.status_code == 200:
        # print(response.text)
        data = json.loads(response.text)

        location = data["records"]["location"][0]["locationName"]
        weather_elements = data["records"]["location"][0]["weatherElement"]
        ret= location+"\n"
        for i in range(0,3):
            start_time = weather_elements[0]["time"][i]["startTime"]
            end_time = weather_elements[0]["time"][i]["endTime"]
            weather_state = weather_elements[0]["time"][i]["parameter"]["parameterName"]
            rain_prob = weather_elements[1]["time"][i]["parameter"]["parameterName"]
            min_tem = weather_elements[2]["time"][i]["parameter"]["parameterName"]
            comfort = weather_elements[3]["time"][i]["parameter"]["parameterName"]
            max_tem = weather_elements[4]["time"][i]["parameter"]["parameterName"]

            ret+=start_time +"~"+ end_time+"\n" + weather_state+","+ comfort+"\n"

  
        return ret   

    else:
        print("Can't get data1!")
        

def get_data2():
    
    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-EB318A2B-32A0-447F-9E3B-3D129A05E43F&locationName=%E8%87%BA%E5%8D%97%E5%B8%82"
    params = {
        "Authorization": "CWB-EB318A2B-32A0-447F-9E3B-3D129A05E43F",
        "locationName": "台南市",
    }

    response = requests.get(url, params=params)
    print(response.status_code)

    if response.status_code == 200:
        # print(response.text)
        data = json.loads(response.text)

        location = data["records"]["location"][0]["locationName"]
        weather_elements = data["records"]["location"][0]["weatherElement"]
        ret= location+"\n"
        for i in range(0,3):
            start_time = weather_elements[0]["time"][i]["startTime"]
            end_time = weather_elements[0]["time"][i]["endTime"]
            weather_state = weather_elements[0]["time"][i]["parameter"]["parameterName"]
            rain_prob = weather_elements[1]["time"][i]["parameter"]["parameterName"]
            min_tem = weather_elements[2]["time"][i]["parameter"]["parameterName"]
            comfort = weather_elements[3]["time"][i]["parameter"]["parameterName"]
            max_tem = weather_elements[4]["time"][i]["parameter"]["parameterName"]

            ret+=start_time +"~"+ end_time+"\n" +"降雨機率 : "+ rain_prob +"\n"

  
        return ret   

    else:
        print("Can't get data2!")
              

def get_data3():
    
    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-EB318A2B-32A0-447F-9E3B-3D129A05E43F&locationName=%E8%87%BA%E5%8D%97%E5%B8%82"
    params = {
        "Authorization": "CWB-EB318A2B-32A0-447F-9E3B-3D129A05E43F",
        "locationName": "台南市",
    }

    response = requests.get(url, params=params)
    print(response.status_code)

    if response.status_code == 200:
        # print(response.text)
        data = json.loads(response.text)

        location = data["records"]["location"][0]["locationName"]
        weather_elements = data["records"]["location"][0]["weatherElement"]
        ret= location+"\n"
        for i in range(0,3):
            start_time = weather_elements[0]["time"][i]["startTime"]
            end_time = weather_elements[0]["time"][i]["endTime"]
            weather_state = weather_elements[0]["time"][i]["parameter"]["parameterName"]
            rain_prob = weather_elements[1]["time"][i]["parameter"]["parameterName"]
            min_tem = weather_elements[2]["time"][i]["parameter"]["parameterName"]
            comfort = weather_elements[3]["time"][i]["parameter"]["parameterName"]
            max_tem = weather_elements[4]["time"][i]["parameter"]["parameterName"]

            ret+=start_time +"~"+ end_time+"\n"  +"最低溫 : "+ min_tem+"度"+"\n" +"最高溫 : "+ max_tem +"度"+"\n\n\n"

  
        return ret   

    else:
        print("Can't get data3!")
        

    
def get_data():
    
    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-EB318A2B-32A0-447F-9E3B-3D129A05E43F&locationName=%E8%87%BA%E5%8D%97%E5%B8%82"
    params = {
        "Authorization": "CWB-EB318A2B-32A0-447F-9E3B-3D129A05E43F",
        "locationName": "台南市",
    }

    response = requests.get(url, params=params)
    print(response.status_code)

    if response.status_code == 200:
        # print(response.text)
        data = json.loads(response.text)

        location = data["records"]["location"][0]["locationName"]
        weather_elements = data["records"]["location"][0]["weatherElement"]
        ret= location+"\n"
        for i in range(0,3):
            start_time = weather_elements[0]["time"][i]["startTime"]
            end_time = weather_elements[0]["time"][i]["endTime"]
            weather_state = weather_elements[0]["time"][i]["parameter"]["parameterName"]
            rain_prob = weather_elements[1]["time"][i]["parameter"]["parameterName"]
            min_tem = weather_elements[2]["time"][i]["parameter"]["parameterName"]
            comfort = weather_elements[3]["time"][i]["parameter"]["parameterName"]
            max_tem = weather_elements[4]["time"][i]["parameter"]["parameterName"]

            ret+=start_time +"~"+ end_time+"\n" +"降雨機率 : "+ rain_prob+ "%"+"\n" +"最低溫 : "+ min_tem+"度"+"\n" +"最高溫 : "+ max_tem+"\n" + weather_state+","+ comfort+"\n"

  
        return ret   
        # print(location)
        # print(start_time)
        # print(end_time)
        # print(weather_state)
        # print(rain_prob)
        # print(min_tem)
        # print(comfort)
        # print(max_tem)

    else:
        print("Can't get data!")
        