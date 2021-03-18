from datetime import datetime
import json
import os
import requests
import time


class Cache:
    def __init__(self):
        self.cache_file = "./Cache.csv"
        self.requests_cache = {}
        self.session = requests.session()
        self.session.headers.update({
            "platform": "pc",
            "language": "en"
        })
        self.load()
        self.last_api = ""
        self.needs_save = False

    def get(self, url, key_ttl=(2 * 86400)):
        current_api = url.split("/")[2]

        if current_api == "api.warframe.market":
            if "items" in url and "statistics" not in url:
                key_name = "item_list"
            elif "ducats" in url:
                key_name = "ducats"
            else:
                key_name = url.split("/")[-2]
        elif current_api == "api.warframestat.us":
            key_name = url.split("/")[-1]
        else:
            raise Exception

        is_cached = False
        if key_name in self.requests_cache.keys():
            is_cached = True
        if is_cached and (datetime.now() - self.requests_cache[key_name].timestamp).total_seconds() > key_ttl:
            is_cached = False
        
        if is_cached:
            return self.requests_cache[key_name]
        else:
            if current_api == self.last_api:
                time.sleep(1/3)
            response = NewResponse(self.session.get(url))
            if response.status_code == 200:
                self.requests_cache[key_name] = response
                self.needs_save = True
            self.last_api = current_api
            return response

    def load(self):
        if os.path.isfile(self.cache_file):
            file = open(self.cache_file, "r", encoding="utf-8")
            try:
                for line in file:
                    temp = line.split(";")
                    response = CachedResponse()
                    response.timestamp = datetime.strptime(temp[1], "%Y-%m-%d %H:%M:%S.%f")
                    response.json_data = json.loads(temp[2])
                    self.requests_cache[temp[0]] = response
                file.close()
            except (json.JSONDecodeError, TypeError, KeyError, IndexError) as e:
                print("ERROR: Couldn't load cache! %s" % e)
                file.close()
                os.remove(self.cache_file)

    def save(self):
        with open(self.cache_file, "w", encoding="utf-8") as file:
            for key in self.requests_cache.keys():
                file.write(key + ";")
                file.write(str(self.requests_cache[key].timestamp) + ";")
                file.write(str(json.dumps(self.requests_cache[key].json_data)) + "\n")
        self.needs_save = False


class CachedResponse:
    def __init__(self):
        self.json_data = []
        self.status_code = 200
        self.timestamp = 0


class NewResponse(CachedResponse):
    def __init__(self, response):
        super().__init__()
        self.status_code = response.status_code
        self.timestamp = datetime.now()
        self.is_vaulted = False
        
        try:
            json_response = response.json()
        except json.JSONDecodeError:
            json_response = {response.text}
        if "payload" in json_response:
            if "statistics_closed" in json_response["payload"].keys():
                time_frame = ""
                if len(json_response["payload"]["statistics_closed"]["90days"]) > 0:
                    time_frame = "90days"
                if len(json_response["payload"]["statistics_closed"]["48hours"]) > 0:
                    time_frame = "48hours"
                if time_frame != "":
                    self.json_data = {
                        "payload": {
                            "statistics_closed": {
                                "48hours": [{
                                    "wa_price": "N/A"
                                }],
                                "90days": [{
                                    "wa_price": "N/A"
                                }]
                            }
                        }
                    }
                    json_response = json_response["payload"]["statistics_closed"][time_frame][0]["wa_price"]
                    self.json_data["payload"]["statistics_closed"][time_frame][0]["wa_price"] = json_response
            elif "previous_hour" in json_response["payload"].keys():
                self.json_data = {
                    "payload": {
                        "previous_hour": []
                    }
                }
                remove_keys = ["datetime", "position_change_month", "position_change_week", "position_change_day",
                               "plat_worth", "volume", "ducats_per_platinum", "ducats_per_platinum_wa", "median",
                               "wa_price", "id"]
                for item in json_response["payload"]["previous_hour"]:
                    for key in remove_keys:
                        item.pop(key)
                    self.json_data["payload"]["previous_hour"].append(item)
            elif "items" in json_response["payload"].keys():
                self.json_data = {
                    "payload": {
                        "items": []
                    }
                }
                for item in json_response["payload"]["items"]:
                    if "prime" in item["url_name"]:
                        if item["url_name"].endswith("_set"):
                            continue
                        item.pop("thumb")
                        item.pop("item_name")
                        self.json_data["payload"]["items"].append(item)
        elif isinstance(json_response, list) and "place" in json_response[0].keys():
            if len(json_response) == 24:
                self.is_vaulted = True
            for place in json_response:
                if " Relic" in place["place"]:
                    place["vaulted"] = self.is_vaulted
                    self.json_data.append(place)
        else:
            self.json_data = str(json_response)
