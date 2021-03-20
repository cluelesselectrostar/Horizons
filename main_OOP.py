# Unique token code hiding in a vent!
from token_file import code
from strings import *

import discord
import random
from discord.ext import commands
import pandas as pd
import numpy as np
import pickle
import os
from collections import defaultdict
import asyncio

import time

# Print Packages
from tabulate import tabulate

async def fprint(msg, temp_df):
	table_string = tabulate(temp_df, headers='keys', tablefmt='fancy_grid')
	await msg.channel.send("""```{}```""".format(table_string))

def append_event(event_string, temp_df):
	event_time = event_string.split()[0]
	event_name= event_string.split()[1]
	event_place= event_string.split()[2]
	new_event = {'Time':event_time, 'Event':event_name, 'Location':event_place}
	new_df = temp_df.append(new_event, ignore_index = True)
	return new_df

async def new_event(reaction, event_string):
	event_time = event_string.split()[0]
	event_name= event_string.split()[1]
	event_place= event_string.split()[2]

	myEmbed = discord.Embed(
		title = "New event!",
		description = "You have just scheduled an event with the details as follows:",
		color = 0x93CEBA
	)
	myEmbed.add_field(
		name = "⏰ Time",
		value = """```{}```""".format(event_time),
		inline = False
	)
	myEmbed.add_field(
		name = "🎫 Event name",
		value = """```{}```""".format(event_name),
		inline = False
	)
	myEmbed.add_field(
		name = "📌 Location",
		value = """```{}```""".format(event_place),
		inline = False
	)
	myEmbed.set_footer(
		text = "from Thyme"
	)
	myEmbed.set_author(
		name = "Requested by this nosy guy ",
	)
	await reaction.message.channel.send(embed = myEmbed)

class cluelessBot(commands.Bot):

	df = pd.DataFrame(columns = ['Time','Event','Location','Directions'])
	index = 0

	########## INITIALISE and EVENTS ##########
	def __init__(self, command_prefix, self_bot):
		commands.Bot.__init__(self, command_prefix=command_prefix, self_bot=self_bot)
		self.message1 = "[INFO]: Thyme is now online"
		self.add_commands()

		# Calendar
		event_1 = {'Time':'09:00-11:00', 'Event':'Electromagnetism, Laboratory', 'Location':'Imperial College EEE Building'}
		event_2 = {'Time':'12:00-13:00', 'Event':'Power Electronics, Lecture', 'Location':'Imperial College EEE Building'}
		event_3 = {'Time':'16:00-18:00', 'Event':'Horizons, Changemakers', 'Location':'Imperial College Sherfield Building'}
		self.df = self.df.append(event_1, ignore_index = True)
		self.df = self.df.append(event_2, ignore_index = True)
		self.df = self.df.append(event_3, ignore_index = True)
		self.index = 0

	async def on_reaction_add(self, reaction, user):

		# Remove previous message
		if not user.bot:
			#await reaction.message.delete()
			await reaction.message.channel.send('----------')

		emoticon = reaction.emoji 

		def check_manual(m):
				return m.content != ''

		# Home
		if (emoticon == "🏠") and not user.bot:
			msg = await reaction.message.channel.send(home)
			reactions = ['⏭','📕','💡','🛠','🪑','⏹']
			for react in reactions:
				await msg.add_reaction(str(react))

		# Summary 📕
		if (emoticon == "📕") and not user.bot:
			msg = await reaction.message.channel.send("Greetings, these are your events for today:  📅 ")
			await fprint(reaction.message, self.df)
			msg = await reaction.message.channel.send(tmrschedule)
			reactions = ['⏭','💡','📝','🏠','⏹']
			for react in reactions:
				await msg.add_reaction(str(react))
		
		# Next journey
		if (emoticon == "⏭") and not user.bot:
			await reaction.message.channel.send(embed = journeyEmbed)
			await reaction.message.channel.send('These are the details for your next journey. I will send it to you once again before you depart!')
			await reaction.message.channel.send(file=discord.File('images/journey_map.jpeg'))
			msg = await reaction.message.channel.send(requestdetail)
			reactions = ['📖','🏠','⏹']
			for react in reactions:
				await msg.add_reaction(str(react))
		
		# Detailed journey
		if (emoticon == "📖") and not user.bot:
			await reaction.message.channel.send(embed = detailedEmbed)
			msg = await reaction.message.channel.send(anything_else)
			reactions = ['🏠','⏹']
			for react in reactions:
				await msg.add_reaction(str(react))

		# Settings
		if (emoticon == "🛠") and not user.bot:
			msg = await reaction.message.channel.send(notifications)
			reactions = ['📞','💬','📲','📵','🏠','⏹']
			for react in reactions:
				await msg.add_reaction(str(react))
		
		# Initial Setup
		if (emoticon == "🪑") and not user.bot:
			msg = await reaction.message.channel.send(link)
			reactions = ['🎓','📅','🏠','⏹']
			for react in reactions:
				await msg.add_reaction(str(react))

		# Linking calendars
		if (emoticon == "🎓" or emoticon =="📅") and not user.bot:
			msg1 = await reaction.message.channel.send('Transferring 🔄...')
			time.sleep(1)
			msg2 = await reaction.message.channel.send('Transferring 🔄...')
			time.sleep(1)
			msg3 = await reaction.message.channel.send('Transferring 🔄...')
			await msg1.delete()
			await msg2.delete()
			await msg3.delete()
			msg = await reaction.message.channel.send(linked)
			reactions = ['📞','💬','📲','📵','🏠','⏹']
			for react in reactions:
				await msg.add_reaction(str(react))

		# Active/Passive Notifications
		if (emoticon in ['📞','💬','📲','📵']) and not user.bot:
			msg = await reaction.message.channel.send(time_interval)
			reactions = ['1️⃣','2️⃣','3️⃣','4️⃣','🏠','⏹']
			for react in reactions:
				await msg.add_reaction(str(react))

		# Time interval updated - All done!
		if (emoticon in ['1️⃣','2️⃣','3️⃣','4️⃣']) and not user.bot:
			msg = await reaction.message.channel.send(settings_updated)
			reactions = ['🏠','⏹']
			for react in reactions:
				await msg.add_reaction(str(react))

		# Create manual events
		if emoticon == "💡" and not user.bot:
			msg = await reaction.message.channel.send(requestmanual)	
			try:
				m = await client.wait_for(event='message', check=check_manual, timeout=60)
			except asyncio.TimeoutError:
				msg = await reaction.message.channel.send('You haven\'t reacted to the message within 30 seconds. Please restart with `*start`')
			else:
				event_string = m.content
				self.df = append_event(event_string, self.df)
				await new_event(reaction, event_string)
				msg = await reaction.message.channel.send(anything_else)
				reactions = ['🏠','⏹']
				for react in reactions:
					await msg.add_reaction(str(react))
		
		# Modify an event
		if emoticon == "📝" and not user.bot:
			msg = await reaction.message.channel.send(requestmodify)
			try:
				m = await client.wait_for(event='message', check=check_manual, timeout=60)
			except asyncio.TimeoutError:
				msg = await reaction.message.channel.send('You haven\'t reacted to the message within 30 seconds. Please restart')
			else:
				self.index = int(m.content)
				try:
					temp_df = self.df.iloc[0]
					msg = await reaction.message.channel.send(modifyoptions)
					reactions = ['⏱','🔏','📌','🗺','🗑','🏠','⏹']
					for react in reactions:
						await msg.add_reaction(str(react))
				except:
					msg = await reaction.message.channel.send(modifyerror)
					reactions = ['🏠','⏭','📝 ','⏹']
					for react in reactions:
						await msg.add_reaction(str(react))

		# Delete event
		if emoticon == "🗑" and not user.bot:
			self.df = self.df.drop(self.index)
			msg = await reaction.message.channel.send(deletedone)
			reactions = ['🏠','⏹']
			for react in reactions:
				await msg.add_reaction(str(react))

		# Modify event time/loc/name/directions
		if (emoticon in ['⏱','🔏','📌','🗺']) and not user.bot:
			msg = await reaction.message.channel.send(modifylimit)
			reactions = ['🏠','⏹']
			for react in reactions:
				await msg.add_reaction(str(react))
		

	async def on_ready(self):
		print(self.message1)

	async def on_command_error(self, context, error):
		await context.send("Gulp! {}".format(str(error)))
	
	def add_commands(self):

		@self.command(name = 'start', pass_context=True)
		async def _start(context, *args):
			msg = await context.message.channel.send(home)
			reactions = ['⏭','📕','💡','📝','🛠','🪑','⏹']
			for react in reactions:
				await msg.add_reaction(str(react))
					

# INITIALISE CLIENT
client = cluelessBot(command_prefix="*", self_bot=False)

# Run Client
client.run(code)