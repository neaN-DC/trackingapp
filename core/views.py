from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests
from bs4 import BeautifulSoup
from .models import UsersId
from user.models import UserslistId
from .forms import HomeForm
import lxml
from django.conf import settings




def home(request):

	def get_html_content(playerId):
		USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
		LANGUAGE = "en-US,en;q=0.5"
		session = requests.Session()
		session.headers['User-Agent'] = USER_AGENT
		session.headers['Accept-Language'] = LANGUAGE
		session.headers['Content-Language'] = LANGUAGE
		return session.get('https://www.battlemetrics.com/players/'+ str(playerId.player_id))

	def getsteamapi(playerId):
		url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=302232255A2C92632150EBB5B75918B3&steamids='+ playerId.playersteam_id
		session = requests.Session()

		return session.get(url).json()


	def online_status(player_steam_status):
		if player_steam_status == 0:
			return "Offline"
		elif player_steam_status == 1:
			return "Online"
		elif player_steam_status == 2:
			return "Busy"
		elif player_steam_status == 3:
			return "Away"
		elif player_steam_status == 4:
			return "Snooze"
		else:
			return "Error could not find status"

	if request.user.is_authenticated:
		playerIds = UserslistId.objects.filter(user_id = request.user.id)
	else:
		playerIds = UsersId.objects.all()

	playerList = []

	for playerId in playerIds:
		r = getsteamapi(playerId)
		html_content = get_html_content(playerId)
		soup = BeautifulSoup(html_content.text, 'lxml')

		#checking to see if player exists on battlemetrics
		try:
			current_player = soup.find("h3", attrs={"class": "css-8uhtka"}).text
			last_seen_result = soup.find('dd').next_sibling.next_sibling.text
			current_server_result = soup.find('dt').next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text
		except:
			current_player = "Not Found"
			last_seen_result = "Not Found"
			current_server_result = "Not found"
		#checking to see if player exists on steam
		try:
			player_steam_status = r["response"]["players"][0]["personastate"]
			try:
				playerSteam_list = {
					'player_steam_status': online_status(player_steam_status),
					'player_game_status':  r["response"]["players"][0]["gameextrainfo"], 
					'profile_status':  r["response"]["players"][0]["communityvisibilitystate"],
					'current_player' : current_player,
		            'last_seen_result' : last_seen_result,
		            'current_server_result' : current_server_result,
		            'players_name_given': playerId.players_name_given,
		            'steam_profile': 'https://steamcommunity.com/profiles/'+ playerId.playersteam_id,
		            'battlemetrics_profile': 'https://www.battlemetrics.com/players/'+ playerId.player_id,
				}
			except:
				playerSteam_list = {
					'player_steam_status': online_status(player_steam_status),
					'player_game_status':  "Not Playing", 
					'profile_status':  r["response"]["players"][0]["communityvisibilitystate"],
					'current_player' : current_player,
		            'last_seen_result' : last_seen_result,
		            'current_server_result' : current_server_result,
		            'players_name_given': playerId.players_name_given,
		            'steam_profile': 'https://steamcommunity.com/profiles/'+ playerId.playersteam_id,
		            'battlemetrics_profile': 'https://www.battlemetrics.com/players/'+ playerId.player_id,
				}
			playerList.append(playerSteam_list)
		except:
			playerSteam_list = {
				'player_steam_status': "Player not Found on Steam",
				'player_game_status':  "Player not Found on Steam", 
				'profile_status':  "Player not Found on Steam",
				'current_player' : current_player,
	            'last_seen_result' : last_seen_result,
	            'current_server_result' : current_server_result,
	            'players_name_given': playerId.players_name_given,
	            'steam_profile': 'https://steamcommunity.com/profiles/'+ playerId.playersteam_id,
	            'battlemetrics_profile': 'https://www.battlemetrics.com/players/'+ playerId.player_id,
			}
			playerList.append(playerSteam_list)

	return render(request, 'core/home.html', {'playerList': playerList})



def save_player_id(request):

	form = HomeForm(request.POST)

	if form.is_valid():
		form.save()
		form = HomeForm()

		
	context = { 'form': form }
	return render (request, 'core/playerid.html', context)




