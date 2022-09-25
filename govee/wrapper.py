from json import dumps

from requests import put,get
from requests.structures import CaseInsensitiveDict


#GOVEE ENDPOINTS
DEV_C = "https://developer-api.govee.com/v1/devices/control" #control devices
DEV_S ="https://developer-api.govee.com/v1/devices/state" #query state if device
DEV = "https://developer-api.govee.com/v1/devices" #list devices and attributes
APP_C = "https://developer-api.govee.com/v1/appliance/devices/control" #control appliance devices
APP = "https://developer-api.govee.com/v1/appliance/devices" #list appliance devices

class Govee():
    """
        Parameter(s): 
            - mac: The MAC address of the device\n
            - mod: The model number of the device\n

    """
    def __init__(self,key:str,mac:str = None,mod:str = None) -> None:
        self.key = key
        self.mac = mac
        self.mod = mod

    def set_color(self,col:tuple) -> str:
        """
            Parameter(s): 
                - col: The rgb level to set\n
            Returns: 'Success' or Error Message
        """
        #Headers
        header = CaseInsensitiveDict()
        header["Govee-API-Key"] = self.key
        header["Content-Type"] = "application/json"

        #Body
        body = dumps({
            "device":self.mac,
            "model":self.mod,
            "cmd":{"name":"color","value":{"r":col[0],"g":col[1],"b":col[2]}}})

        #Store data as json
        data = put(DEV_C,headers=header,data=body)

        return data.json()['message']

    def turn_on(self) -> str:
        """
            Returns: 'Success' or Error Message
        """
        #Headers
        header = CaseInsensitiveDict()
        header["Govee-API-Key"] = self.key
        header["Content-Type"] = "application/json"

        #Body
        body = dumps({
            "device":self.mac,
            "model":self.mod,
            "cmd":{"name":"turn","value":"on"}})

        #Store data as json
        data = put(DEV_C,headers=header,data=body)

        return data.json()['message']
    
    def turn_off(self) -> str:
        """
            Returns: 'Success' or Error Message
        """
        #Headers
        header = CaseInsensitiveDict()
        header["Govee-API-Key"] = self.key
        header["Content-Type"] = "application/json"

        #Body
        body = dumps({
            "device":self.mac,
            "model":self.mod,
            "cmd":{"name":"turn","value":"off"}})

        #Store data as json
        data = put(DEV_C,headers=header,data=body)

        return data.json()['message']

    def set_brightness(self,val:int) -> str:
        """
            Parameter(s): 
                - val: The value to set the brightness 0-100\n
            Returns: 'Success' or Error Message
        """
        #Headers
        header = CaseInsensitiveDict()
        header["Govee-API-Key"] = self.key
        header["Content-Type"] = "application/json"

        #Body
        body = dumps({
            "device":self.mac,
            "model":self.mod,
            "cmd":{"name":"brightness","value":val}})

        #Store data as json
        data = put(DEV_C,headers=header,data=body)

        return data.json()['message']

    def get_all_devices(self) -> list[tuple]:
        """
            Parameter(s): None
            Returns: A list of tuples containing the devices MAC and Model Number respectively
        """
        #Headers
        header = CaseInsensitiveDict()
        header["Govee-API-Key"] = self.key

        #Store data as json
        data = get(DEV,headers=header).json()['data']['devices']
        
        #Get the devices and models
        devs = []
        for dev in data:
            devs.append((dev['deviceName'],dev['device'],dev['model']))
        return devs
            
    def get_brightness(self) -> int:
        """
            Returns: The brightness level from 0 to 100
        """
        #Headers
        header = CaseInsensitiveDict()
        header["Govee-API-Key"] = self.key

        #Param
        param = {
            "device":self.mac,
            "model":self.mod
        }

        #Store brightness level
        bri = get(DEV_S,headers=header,params=param).json()['data']['properties'][2]['brightness']

        return int(bri)
    
    def get_color(self):
        """
            Returns: The rgb levels from 0 to 255 in a tuple (0,0,0)
        """
        #Headers
        header = CaseInsensitiveDict()
        header["Govee-API-Key"] = self.key

        #Param
        param = {
            "device":self.mac,
            "model":self.mod
        }

        #Store data as json
        data = get(DEV_S,headers=header,params=param).json()['data']['properties'][3]['color']
        color = (int(data['r']),int(data['g']),int(data["b"]))

        return color

    def get_commands(self,name = None) -> list[str]:
        """
            Parameter(s):
                - name: The name of the device\n
            Returns: A list of strings containing the commands the device can take
        """
        #Headers
        header = CaseInsensitiveDict()
        header["Govee-API-Key"] = self.key

        #Store data as json
        data = get(DEV,headers=header).json()['data']['devices']

        #Search for model name 
        devs = []
        for dev in data:
            if dev['deviceName'] == name:
                if dev['supportCmds']:
                    return dev['supportCmds']
                return "Not Controllable"
            elif not name:
                devs.append((dev['deviceName'],dev['supportCmds']))
        if name:
            return "Device Not Found"
        else:
            return devs
    
    def is_controllable(self,name:str = None) -> bool:
        """
            Parameter(s):
                - name: The name of the device\n
            Returns: True if the device is controllable; Otherwise false
        """
        #Headers
        header = CaseInsensitiveDict()
        header["Govee-API-Key"] = self.key

        #Store data as json
        data = get(DEV,headers=header).json()['data']['devices']

        #Search for model name
        devs = []
        for dev in data:
            if dev['deviceName'] == name:
                return dev['controllable']
            elif not name:
                devs.append((dev['deviceName'],dev['controllable']))
        if name:        
            return "Device Not Found"
        else:
            return devs
    
    def is_retrievable(self,name:str = None) -> bool:
        """
            Parameter(s):
                - name: The name of the device\n
            Returns: True if the device is retrieveable; Otherwise false
        """
        #Headers
        header = CaseInsensitiveDict()
        header["Govee-API-Key"] = self.key

        #Store data as json
        data = get(DEV,headers=header).json()['data']['devices']

        #Search for model name
        devs = []
        for dev in data:
            if dev['deviceName'] == name:
                return dev['retrievable']
            elif not name:
                devs.append((dev['deviceName'],dev['retrievable']))
        if name:        
            return "Device Not Found"
        else:
            return devs
    
    def is_online(self) -> str:
        """
            Returns: 'true' if device is online; Otherwise 'false'
        """
        #Headers
        header = CaseInsensitiveDict()
        header["Govee-API-Key"] = self.key

        #Param
        param = {
            "device":self.mac,
            "model":self.mod
        }

        #Store online status
        online = get(DEV_S,headers=header,params=param).json()['data']['properties'][0]['online']
        
        return online
        
    def is_on(self) -> str:
        """
            Returns: 'on' if device is on; Otherwise 'off'
        """
        #Headers
        header = CaseInsensitiveDict()
        header["Govee-API-Key"] = self.key

        #Param
        param = {
            "device":self.mac,
            "model":self.mod
        }

        #Store if light is on
        on = get(DEV_S,headers=header,params=param).json()['data']['properties'][1]['powerState']
        
        return on
