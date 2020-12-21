import requests
import os





def get_information():


	url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=948ADFC5AA39BFA48B536A316B0A333E&steamids=76561198023347029'
	r = requests.get(url)
	steamid = r.json()
	steamid_list = []
	for i in range(len(steamid['steamid'])):
	    steamid_list.append(steamid['steamid'][i])	
	return steamid_list

