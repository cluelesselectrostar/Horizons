		@self.command(name = 'next', pass_context=True, help = 'shows your next journey')
		async def _next(context, *args):
			await context.message.channel.send(embed = journeyEmbed)
			await context.message.channel.send('These are the details for your next journey. I will send it to you once again before you depart!')
			await context.message.channel.send(file=discord.File('images/journey_map.jpeg'))


		@self.command(name = 'tmr', pass_context=True, help = 'shows your events for tmr')
		async def _tmr(context, *args):			
			await context.message.channel.send("Greetings, these are your events for tomorrow:  📅 ")
			await fprint(context, self.df)
			body = tmrschedule # import			
			msg = await context.message.channel.send(body)
			reactions = ['🏠','⏭','📝','⏹']
			for react in reactions:
				await msg.add_reaction(str(react))

		@self.command(name = 'today', pass_context=True, help = 'shows your events for today')
		async def _today(context, *args):			
			await context.message.channel.send("Greetings, these are your events for today:  📅 ")
			await fprint(context, self.df)
			body = tmrschedule # import			
			msg = await context.message.channel.send(body)
			reactions = ['🏠','⏭','📝','⏹']
			for react in reactions:
				await msg.add_reaction(str(react))

		@self.command(name = 'settings', pass_context=True, help = 'modify notification settings')
		async def _settings(context, *args):
			await context.message.channel.send(notifications)
			await context.message.channel.send(time_interval)
			await context.message.channel.send(settings_updated)

		@self.command(name = 'new', pass_context=True, help = 'create new event')
		async def _new(context, *args):
			await context.message.channel.send(requestmanual)
			def check_manual(m):
				return m.content != ''			
			try:
				m = await client.wait_for(event='message', check=check_manual, timeout=60)
			except asyncio.TimeoutError:
				msg = await context.message.channel.send('You haven\'t reacted to the message within 30 seconds. Please restart')
			else:
				event_string = m.content
				self.df = append_event(event_string, self.df)
				await new_event(context, event_string)
			
		@self.command(name = 'setup', pass_context=True, help = 'setup or change preferences')
		async def _setup(context, *args):
			reactions = ['🎓','📅','🏠','⏹']
			body = link # import			
			msg = await context.message.channel.send(body)

			for react in reactions:
				await msg.add_reaction(str(react))

			def check(reaction, user):
				react = str(reaction.emoji)
				return react in reactions and user == context.message.author

			manual = False
			response = ""
			try:
				reaction, user = await self.wait_for(event='reaction_add', timeout=30, check=check)
			except asyncio.TimeoutError:
				msg = await context.message.channel.send('You haven\'t reacted to the message within 30 seconds. Please restart')
			else:
				response = str(reaction.emoji)
		