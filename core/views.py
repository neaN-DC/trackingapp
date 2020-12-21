from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests
from bs4 import BeautifulSoup
from .models import UsersIds
from .models import SteamId
from .forms import HomeForm


def get_html_content(playerId):
	USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
	LANGUAGE = "en-US,en;q=0.5"
	session = requests.Session()
	session.headers['User-Agent'] = USER_AGENT
	session.headers['Accept-Language'] = LANGUAGE
	session.headers['Content-Language'] = LANGUAGE

	return session.get('https://www.battlemetrics.com/players/'+ str(playerId))



def home(request):

	playerIds = UsersIds.objects.all()
	playerList = []



	for playerId in playerIds:
		html_content = get_html_content(playerId)
		soup = BeautifulSoup(html_content.text, 'html.parser')
		current_player = soup.find("h3", attrs={"class": "css-8uhtka"}).text
		last_seen_result = soup.find('dd').next_sibling.next_sibling.text
		current_server_result = soup.find('dt').next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text

		tempdict = { 'current_player' : current_player,
		            'last_seen_result' : last_seen_result,
		            'current_server_result' : current_server_result,
		             }
		playerList.append(tempdict)


	steamids = SteamId.objects.all()
	playerSteamidList = []
	for playersid in steamids:

		url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=948ADFC5AA39BFA48B536A316B0A333E&steamids='+ str(playersid)
		r = requests.get(url).json()

		try:
			playerSteam_list = {
				'playernameapi': r["response"]["players"][0]["personastate"],
				'playerGame':  r["response"]["players"][0]["gameextrainfo"], 
			}
		except:
			playerSteam_list = {
				'playernameapi': r["response"]["players"][0]["personastate"],
				'playerGame': "Not Playing", 
			}

		playerSteamidList.append(playerSteam_list)

		print (playerSteamidList)
	

	return render(request, 'core/home.html', {'playerSteamidList': playerSteamidList,'playerList': playerList , 'playerIds': playerIds})




def index(request):

	playerIds = UsersIds.objects.all()
	playerList = []
	for playerIdq in playerIds:

		url = 'https://api.battlemetrics.com/players/'+ str(playerIdq) +'/relationships/sessions'
		r = requests.get(url).json()
		player_list = {
			'last_online': r["data"][0]["attributes"]["stop"],
			'playernameapi': r["data"][0]["attributes"]["name"],

		}
		playerList.append(player_list)

	

	return render(request, 'core/playerid.html', {'playersList': playerList,})





def save_player_id(request):
	form = HomeForm(request.POST)

	if form.is_valid():
		form.save()
		form = HomeForm()
		
	context = { 'form': form }
	return render (request, 'core/playerid.html', context)


