class Drop:
    def __init__(self, c, name):
        self.name = name.strip()
        self.cache = c
        self.chance = 0
        # Replace "P.", "BP" and "&"
        replace_dict = {
            "P.": "Prime",
            "BP": "Blueprint",
            "&": "and"
        }
        for k in replace_dict.keys():
            if k in self.name:
                self.name = self.name.split(" ")
                self.name[self.name.index(k)] = replace_dict[k]
                self.name = " ".join(self.name)
        # Get Ducats
        self.ducats = "N/A"
        if "Prime" in self.name:
            self.ducats = self.get_ducats()
        # Get Price
        try:
            price = self.get_price()
            if price == "N/A":
                self.platinum = price
            elif price == int(price):
                self.platinum = int(price)
            else:
                self.platinum = round(price, 1)
        except (TypeError, KeyError, IndexError) as e:
            print("Couldn't get price for %s: %s" % (self.name, e))
            self.platinum = "N/A"

    def get_ducats(self):
        search_string = self.get_search_string()
        response = self.cache.get("https://api.warframe.market/v1/tools/ducats")
        if response.status_code != 200:
            return "N/A"
        item_id = self.get_id(search_string)
        for item in response.json_data["payload"]["previous_hour"]:
            if item["item"] == item_id:
                return item["ducats"]

    def get_id(self, search_string):
        response = self.cache.get("https://api.warframe.market/v1/items")
        if response.status_code != 200:
            return "N/A"
        for item in response.json_data["payload"]["items"]:
            if item["url_name"] == search_string:
                return item["id"]

    def get_price(self):
        search_string = self.get_search_string()
        response = self.cache.get("https://api.warframe.market/v1/items/" + search_string + "/statistics")
        if response.status_code != 200:
            return "N/A"
        item_data = response.json_data["payload"]["statistics_closed"]
        if len(item_data["48hours"]) > 0:
            return item_data["48hours"][0]["wa_price"]
        elif len(item_data["48hours"]) == 0 and len(item_data["90days"]) > 0:
            return item_data["90days"][0]["wa_price"]
        else:
            return "N/A"

    def get_search_string(self):
        search_string = self.name.lower().split(" ")
        if search_string[-1] == "blueprint" and search_string[1] == "prime" and len(search_string) == 4:
            search_string.pop()
        search_string = "_".join(search_string)
        if self.name.split(" ")[-1][-1] in [str(x) for x in range(10)]:
            search_string += "_intact"
        return search_string
