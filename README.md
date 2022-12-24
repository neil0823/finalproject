# TOC Final Project 2022

Code for TOC Final Project

A Line bot based on a finite state machine to forecast weather

## Setup

### Basic setting of env
**Know Channel access token in linebot**

**Know Channel serect in linebot**
    
### Prerequisite
* Python 3.6.7
* Pipenv
* HTTPS Server
* pygraphviz 1.6

#### Install Dependency
```sh
pip3 install pipenv

pipenv --three

pipenv install

pipenv shell
```

* pygraphviz (For visualizing Finite State Machine)
	* if you `don't install C++ compiler`,it `can't` successfully installed in python.
###

#### Run Locally
Using `ngrok` as a proxy.

#### How to use Ngrok?

**`ngrok` would be used in the following instruction**

```sh
ngrok http 8000
```

After that, `ngrok` would generate a https URL.

if you shut down your computer,you need to reedit the Webhook URL in linebot because ngrok will give you another https URL.

#### Run the sever

```sh
python app.py
```
## Finite State Machine
![fsm](https://raw.githubusercontent.com/neil0823/finalproject/master/fsm.png)

## How to get weather data?
1.We need to go to the website [click here](https://opendata.cwb.gov.tw/user/authkey)

2.`Create an account` of its member (Facebook `can't` login)

3.Get authorization code

4.Find the data you want(`don't choose weekly weather forecast`,my laptop `crashed` three times because I tried to open it)

5.Create a python program(to get data)
We can know that parameter `location` in json file is a `list`,so we just need to `find the elements` of the list and `match` in the program you created.

* This file have different time periods 
For example:I'm in **14:00**,the start time is **12:00**
Thus,we can know this file `initial start time(index 0)` is `the time depending on where you at`
```sh
weather_elements[0]["time"][0]["startTime"]
```
`initial end time` is **18:00**
```sh
weather_elements[0]["time"][0]["endTime"]
```
You  can see that `time period` is `12:00~18:00`,but we need to know weather in a whole day,not a period of time.
Use `for loop`
```sh
for i in range(0,3):
 start_time = weather_elements[0]["time"][i]["startTime"]
end_time = weather_elements[0]["time"][i]["endTime"]
```
So we can know the weather in`12:00~18:00 tomorrow`(36hrs)
other parameters follow the same pattern
## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.I add a new state because this project `needs` to have at least `four states`.Don't forget to include the program that you match json file(You need to get data in that program).

* user
    ```sh
   ret+=start_time +"~"+ end_time+"\n"  +"最低溫 : "+ min_tem+"度"+"\n" +"最高溫 : "+ max_tem +"度"+"\n\n\n"
    ```
	* Input: `"temperature"`
	
		* Reply:
		
		        臺南市
		
                2022-12-23 12:00:00~2022-12-23 18:00:00

                最低溫 : 16度
                
                最高溫 : 20度
                
                2022-12-23 18:00:00~2022-12-24 06:00:00
                
                最低溫 : 11度
                
                最高溫 : 16度
                
                2022-12-24 06:00:00~2022-12-24 18:00:00
                
                最低溫 : 11度
                
                最高溫 : 20度

	* Input: `"rain"` 
	
	   * Reply: 
	            臺南市

                2022-12-23 12:00:00~2022-12-23 18:00:00
                
                降雨機率:0
                
                2022-12-23 18:00:00~2022-12-24 06:00:00
                
                降雨機率:0
                
                2022-12-24 06:00:00~2022-12-24 18:00:00
                
                降雨機率:0

    * Input: `"weather"` 
	   * Reply:   
	            臺南市
	            
                2022-12-23 12:00:00~2022-12-23 18:00:00
                
                晴時多雲，稍有寒意
                
                2022-12-23 18:00:00~2022-12-24 06:00:00
                
                晴時多雲，稍有寒意
                
                2022-12-24 06:00:00~2022-12-24 18:00:00
                
                晴時多雲，稍有寒意
                
    * Input besides three words above: 
	   * Reply: "Please enter 'weather', 'rain' or 'temperature' to search today weather" 
	   because of this part of code
	   ```sh
        if response == False:
            send_text_message(event.reply_token, "Please enter 'weather', 'rain' or 'temperature' to search today weather")
        ```

## Reference
Thanks:
[Pipenv](https://medium.com/@chihsuan/pipenv-更簡單-更快速的-python-套件管理工具-135a47e504f4) ❤️ [@chihsuan](https://github.com/chihsuan)

[TOC-Project-2019](https://github.com/winonecheng/TOC-Project-2019) ❤️ [@winonecheng](https://github.com/winonecheng)

Flask Architecture ❤️ [@Sirius207](https://github.com/Sirius207)

[Line line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)
