import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
from bs4 import BeautifulSoup as bs
import requests
import datetime

client = Bot(description="whattomine info", command_prefix="-", pm_help = True)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')

@client.command()
async def ping(*args):
	now = datetime.datetime.now()
	links = {'580':'https://whattomine.com/coins?utf8=%E2%9C%93&adapt_q_280x=0&adapt_q_380=0&adapt_q_fury=0&adapt_q_470=0&adapt_q_480=3&adapt_q_570=0&adapt_q_580=1&adapt_580=true&adapt_q_vega56=0&adapt_q_vega64=0&adapt_q_750Ti=0&adapt_q_1050Ti=0&adapt_q_10606=0&adapt_q_1070=0&adapt_q_1070Ti=0&adapt_q_1080=0&adapt_q_1080Ti=0&eth=true&factor%5Beth_hr%5D=30.2&factor%5Beth_p%5D=135.0&grof=true&factor%5Bgro_hr%5D=18.5&factor%5Bgro_p%5D=115.0&x11gf=true&factor%5Bx11g_hr%5D=6.9&factor%5Bx11g_p%5D=110.0&cn=true&factor%5Bcn_hr%5D=690.0&factor%5Bcn_p%5D=115.0&eq=true&factor%5Beq_hr%5D=290.0&factor%5Beq_p%5D=120.0&lre=true&factor%5Blrev2_hr%5D=5700.0&factor%5Blrev2_p%5D=120.0&ns=true&factor%5Bns_hr%5D=650.0&factor%5Bns_p%5D=150.0&lbry=true&factor%5Blbry_hr%5D=135.0&factor%5Blbry_p%5D=145.0&bk2bf=true&factor%5Bbk2b_hr%5D=990.0&factor%5Bbk2b_p%5D=150.0&bk14=true&factor%5Bbk14_hr%5D=1350.0&factor%5Bbk14_p%5D=130.0&pas=true&factor%5Bpas_hr%5D=690.0&factor%5Bpas_p%5D=145.0&skh=true&factor%5Bskh_hr%5D=18.5&factor%5Bskh_p%5D=115.0&factor%5Bl2z_hr%5D=420.0&factor%5Bl2z_p%5D=300.0&factor%5Bcost%5D=0.1&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=abucoins&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=bleutrade&factor%5Bexchanges%5D%5B%5D=cryptopia&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=yobit&dataset=&commit=Calculate',
	'1070ti':'https://whattomine.com/coins?utf8=%E2%9C%93&adapt_q_280x=0&adapt_q_380=0&adapt_q_fury=0&adapt_q_470=0&adapt_q_480=3&adapt_q_570=0&adapt_q_580=0&adapt_q_vega56=0&adapt_q_vega64=0&adapt_q_750Ti=0&adapt_q_1050Ti=0&adapt_q_10606=0&adapt_q_1070=0&adapt_q_1070Ti=1&adapt_1070Ti=true&adapt_q_1080=0&adapt_q_1080Ti=0&eth=true&factor%5Beth_hr%5D=30.5&factor%5Beth_p%5D=135.0&grof=true&factor%5Bgro_hr%5D=36.5&factor%5Bgro_p%5D=120.0&x11gf=true&factor%5Bx11g_hr%5D=13.2&factor%5Bx11g_p%5D=120.0&cn=true&factor%5Bcn_hr%5D=630.0&factor%5Bcn_p%5D=90.0&eq=true&factor%5Beq_hr%5D=470.0&factor%5Beq_p%5D=120.0&lre=true&factor%5Blrev2_hr%5D=41000.0&factor%5Blrev2_p%5D=120.0&ns=true&factor%5Bns_hr%5D=1050.0&factor%5Bns_p%5D=120.0&lbry=true&factor%5Blbry_hr%5D=310.0&factor%5Blbry_p%5D=120.0&bk2bf=true&factor%5Bbk2b_hr%5D=1800.0&factor%5Bbk2b_p%5D=120.0&bk14=true&factor%5Bbk14_hr%5D=2750.0&factor%5Bbk14_p%5D=120.0&pas=true&factor%5Bpas_hr%5D=1100.0&factor%5Bpas_p%5D=120.0&skh=true&factor%5Bskh_hr%5D=31.5&factor%5Bskh_p%5D=120.0&factor%5Bl2z_hr%5D=420.0&factor%5Bl2z_p%5D=300.0&factor%5Bcost%5D=0.1&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=abucoins&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=bleutrade&factor%5Bexchanges%5D%5B%5D=cryptopia&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=yobit&dataset=&commit=Calculate',
	'1080ti':'https://whattomine.com/coins?utf8=%E2%9C%93&adapt_q_280x=0&adapt_q_380=0&adapt_q_fury=0&adapt_q_470=0&adapt_q_480=3&adapt_q_570=0&adapt_q_580=0&adapt_q_vega56=0&adapt_q_vega64=0&adapt_q_750Ti=0&adapt_q_1050Ti=0&adapt_q_10606=0&adapt_q_1070=0&adapt_q_1070Ti=0&adapt_q_1080=0&adapt_q_1080Ti=1&adapt_1080Ti=true&eth=true&factor%5Beth_hr%5D=35.0&factor%5Beth_p%5D=140.0&grof=true&factor%5Bgro_hr%5D=58.0&factor%5Bgro_p%5D=210.0&x11gf=true&factor%5Bx11g_hr%5D=19.5&factor%5Bx11g_p%5D=170.0&cn=true&factor%5Bcn_hr%5D=830.0&factor%5Bcn_p%5D=140.0&eq=true&factor%5Beq_hr%5D=685.0&factor%5Beq_p%5D=190.0&lre=true&factor%5Blrev2_hr%5D=64000.0&factor%5Blrev2_p%5D=190.0&ns=true&factor%5Bns_hr%5D=1400.0&factor%5Bns_p%5D=190.0&lbry=true&factor%5Blbry_hr%5D=460.0&factor%5Blbry_p%5D=190.0&bk2bf=true&factor%5Bbk2b_hr%5D=2800.0&factor%5Bbk2b_p%5D=190.0&bk14=true&factor%5Bbk14_hr%5D=4350.0&factor%5Bbk14_p%5D=210.0&pas=true&factor%5Bpas_hr%5D=1700.0&factor%5Bpas_p%5D=210.0&skh=true&factor%5Bskh_hr%5D=47.5&factor%5Bskh_p%5D=190.0&factor%5Bl2z_hr%5D=420.0&factor%5Bl2z_p%5D=300.0&factor%5Bcost%5D=0.1&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=abucoins&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=bleutrade&factor%5Bexchanges%5D%5B%5D=cryptopia&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=yobit&dataset=&commit=Calculate'
	}

	message = "```\n" + now.strftime("%Y-%m-%d %H:%M") + " profit:\n"
	for card in links.keys():
		r = requests.get(links[card])
		soup = bs(r.text, "html.parser")
		top = soup.findAll('tr')[1]
		count = 0
		for eachTd in top:
			if count == 1:
				info = eachTd.findAll('div',{'style':'margin-left: 50px'})
				coin = info[0].text.strip()
				algo = info[1].text.strip()
			if count == 15:
				info = eachTd.text.strip().split('\n')
				profit = info[2].strip()
				break
			count += 1

		message += card + ": " + profit + " - " + coin + " / " + algo + "\n"

	message += "\n```"
	await client.say(message)

@client.command()
async def stop(*args):
	os.system('killall -9 python3')


client.run('tidepods')
