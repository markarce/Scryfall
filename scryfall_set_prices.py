import requests
from ratelimit import limits, sleep_and_retry

set_prices = {
	"thb": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"eld": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"c19": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"m20": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"mh1": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"war": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"rna": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"grn": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"c18": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"m19": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"gs1": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"bbd": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"dom": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"rix": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"xln": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"c17": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"hou": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"e01": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"akh": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"aer": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"c16": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"kld": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"cn2": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"emn": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"soi": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"ogw": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"c15": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"bfz": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"ori": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"dtk": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"frf": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"c14": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"ktk": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"m15": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"cns": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"jou": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"bng": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"c13": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"ths": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"m14": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"dgm": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"gtc": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"rtr": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"m13": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"pc2": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"avr": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"dka": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"isd": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"m12": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"cmd": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"nph": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"mbs": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"som": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"m11": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"arc": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"roe": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"wwk": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"zen": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"hop": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"m10": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"arb": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"con": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"ala": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"eve": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"shm": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"mor": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"lrw": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"10e": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"fut": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"plc": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"tsp": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"tsb": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"csp": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"dis": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"gpt": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"rav": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"9ed": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"sok": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"bok": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"chk": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"5dn": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"dst": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"mrd": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"8ed": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"scg": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"lgn": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"ons": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"jud": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"tor": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"ody": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"apc": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"7ed": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"pls": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"inv": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"pcy": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"s00": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"nem": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"mmq": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"s99": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"uds": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"ptk": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"6ed": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"ulg": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"usg": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"exo": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"p02": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"sth": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"tmp": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"wth": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"por": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"5ed": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"vis": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"mir": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"all": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"hml": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"ice": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"4ed": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"fem": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"drk": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"leg": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"3ed": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"atq": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"arn": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"2ed": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"leb": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
	"lea": {
		"set_value": 0,
		"none_count": 0,
		"cards": [],
	},
}

valid_sets = list(set_prices.keys())
ONE_MINUTE = 60

@sleep_and_retry
@limits(calls=500, period=ONE_MINUTE)
def call_api(url):
    response = requests.get(url)
    if response.status_code !=200:
        raise Exception('API Response: {}'.format(response.status_code))
    return response

card_data = []
for i in range(1,1529):
    print("fetching page {} of 1529".format(i))
    url = "https://api.scryfall.com/cards?page=" + str(i)
    time.sleep(.100)
    print("appending page {} to card_data".format(i))
    card_data.append(call_api(url).json()["data"])
    print("page successfully appended")

for page in card_data:
    for card in page:
        exp = card["set"]
        if card["lang"] == "en" and exp in valid_sets:
            if card["prices"]["usd"]:
                set_prices[exp]["set_value"] = set_prices[exp]["set_value"] + float(card["prices"]["usd"])
            else: 
                set_prices[exp]["none_count"] = set_prices[exp]["none_count"] + 1
                print("{}: {} - {}".format(card["set"], card["name"], card["prices"]["usd"]))
              # build a smaller card object to append
            small_card = {}
            small_card["card_name"] = card["name"]
            small_card["card_price"] = card["prices"]["usd"]
            small_card["collector_number"] = card["collector_number"]
            set_prices[exp]["cards"].append(small_card)