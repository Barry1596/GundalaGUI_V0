import requests
import datetime

#==== Thermistor Saint Gobain =======
class AccesLiveData():

    def __init__(self, ID, N_data, step):
        self.ID = ID
        self.N_data = N_data
        self.step = step
        self.AccesLive()

    def AccesLive(self):

        http = 'http://api.gundala.co.id/rmcs/data/common/8193/105/{}'.format(self.ID)

        current_date_Time = datetime.datetime.now().replace(microsecond=0)
        current_date_Time = current_date_Time - datetime.timedelta(seconds=current_date_Time.second%12)
        c_str_datetime = str(current_date_Time)
        
        time_now = datetime.datetime.now().replace(microsecond=0).time()
        delta_round = datetime.timedelta(seconds=time_now.second%12)
        delta_time = datetime.timedelta(seconds=self.step)

        round_time = (datetime.datetime.combine(datetime.date(1,1,1),time_now)-delta_round).time()

        data = {
            "data": ["data0", "battery"],
            "options": {
                "filterTime" : c_str_datetime,
                "filterNumberBefore" : self.N_data,
                "filterStep" : self.step
                
            }
        } 

        headers = {
            'Authorization' : 'bearer GYmjIVhAmsQKuAXnMb3TYJO4xoeCL9Q',
            'Content-Type'  : 'application/json'
        }

        Request_Data = requests.get(http, json = data, headers=headers)

        Data_json = Request_Data.json()

        time = []
        Temperatur = []
        battery = []

        for i in range(len(range(self.N_data))):
            Temperatur_plot = float(Data_json['data'][i]['data0'])
            Temperatur.append(Temperatur_plot)

            # time_plot = Data_json['data'][i]['time']
            # time_plot = time_plot.split(' ')
            # time_plot = time_plot[1]
            round_time = (datetime.datetime.combine(datetime.date(1,1,1),round_time) + delta_time).time()
            time_plot = round_time.strftime("%H:%M:%S")
            time.append(time_plot)

            battery_plot = float(Data_json['data'][i]['battery'])
            battery.append(battery_plot)

            
        
        #time.reverse()
        Temperatur.reverse()
        battery.reverse()

        return[time, Temperatur, battery]

class AccesHistoryData():

    def __init__(self, ID, date_begin, date_end, step):
        self.ID = ID
        self.date_begin = date_begin
        self.date_end = date_end
        self.step = step
        self.AccesHistory()
    
    def AccesHistory(self):
        http = 'http://api.gundala.co.id/rmcs/data/common/8193/105/{}'.format(self.ID)

        
        data = {
            "data": ["data0", "battery"],
            "options": {
                "filterBegin" : self.date_begin,
                "filterEnd" : self.date_end,
                "filterStep" : self.step
                
            }
        } 

        headers = {
            'Authorization' : 'bearer GYmjIVhAmsQKuAXnMb3TYJO4xoeCL9Q',
            'Content-Type'  : 'application/json'
        }

        Request_Data = requests.get(http, json = data, headers=headers)

        Data_json = Request_Data.json()

        time = []
        Temperatur = []
        battery = []

        for i in range(len(Data_json['data'])):
            Temperatur_plot = float(Data_json['data'][i]['data0'])
            Temperatur.append(Temperatur_plot)

            time_plot = Data_json['data'][i]['time']
            time_plot = time_plot.split(' ')
            time_plot = time_plot[1]
            time.append(time_plot)

            battery_plot = float(Data_json['data'][i]['battery'])
            battery.append(battery_plot)

        return[time, Temperatur, battery]


#=====Test Live Plot======
# b = AccesLiveData(1,5,12).AccesLive()

# print(b)
# print(b[0])
# print(b[1])


#======Test History Plot======

# a = AccesHistoryData(1,"2021-01-06 16:00:00","2021-01-06 16:10:00",60).AccesHistory()

# print(a[0])
# print(a[1])
# print(a[2])




