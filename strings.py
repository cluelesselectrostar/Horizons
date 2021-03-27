import discord
from discord.ext import commands


journeyEmbed = discord.Embed(
	title = "Details for your next journey",
	description = "Distance: 2.3mi",
	color = 0x93CEBA
)
journeyEmbed.add_field(
	name = "⏰ Time",
	value = "```08:20-08:45 (0h25m)```",
	inline = False
)
journeyEmbed.add_field(
	name = "🚶‍♂️ Directions ",
	value = """```1. 🚶‍♂️ Walk 5 mins to Brook Green (Stop H), across the street from St. Paul\'s Hotel 
2. 🚌 13 mins bus ride (9 or 23) to Royal Albert Hall (Stop RL)
3. 🚶‍♂️ Walk 7 mins to Imperial College EEE Building via Kensington Gore and Exhibition Road ```
""",
	inline = False
)
journeyEmbed.add_field(
	name = "💰 Fare",
	value = """```£1.5```""",
	inline = False
)
journeyEmbed.add_field(
	name = "🌡 Weather",
	value = """```Wear a raincoat 🌧```""",
	inline = False
)
journeyEmbed.add_field(
	name = "🚦 Chance of delay",
	value = """```Expect no more than a 0h10m delay at High Street Kensington.```""",
	inline = False
)
journeyEmbed.set_footer(
	text = "from Thyme"
)
journeyEmbed.set_author(
	name = "Requested by this nosy guy "
)
journeyEmbed.set_image(
	url = 'https://raw.githubusercontent.com/cluelesselectrostar/Horizons/master/images/journey_map.png'
)

# Detailed Journey
detailedEmbed = discord.Embed(
	title = "Detailed Directions",
	description = "2.3mi",
	color = 0x93CEBA
)
detailedEmbed.add_field(
	name = "1️⃣ Walk To Brook Green Bus Stop (Stop H) 🚶‍♂️ (0h4m, 0.2mi)",
	value = """```1. Head southeast on Brook Green
2. Turn right on Hammersmith Road (A315), across the street from St. Pauls Hotel```""",
	inline = False
)
detailedEmbed.add_field(
	name = "2️⃣ Bus 9 towards Aldwych or 23 towards Westbourne Park 🚌 (0h13m, 1.9mi)",
	value = """```Brook Green (Stop H) ↗️
...
Kensington Palace (Stop M)
Palace Gate (Stop RH)
Queens Gate (Stop RK) 
Royal Albert Hall (Stop RL) ↘️
 ```
""",
	inline = False
)
detailedEmbed.add_field(
	name = "3️⃣ Walk To Imperial College EEE Building 🚶‍♂️ (0h9m, 0.5mi) ",
	value = """```
1. Head west on Kensington Rd/Kensington Gore/A315
2. Turn left onto Kensington Gore
3. Turn left onto Prince Consort Rd
4. Slight right to stay on Prince Consort Rd
5. At the roundabout, take the 1st exit onto Exhibition Rd
6. Turn right onto Imperial College Rd
7. Turn right onto Unwin Rd
8. Unwin Rd turns left and becomes Ayrton Rd
Destination will be on the right
```""",
	inline = False
)
detailedEmbed.set_footer(
	text = "from Thyme"
)
detailedEmbed.set_author(
	name = "Requested by this nosy guy "
)



home = """

**Welcome home. It's thyme to grab your time back!**

To perform the actions below, react to a button.

⏭ Details for your next journey
📕 Your summary for the day

💡 Create a new event 
🛠 Notification Settings

🪑 Perform initial setup (again)

⏹ Exit Thyme
"""

tmrschedule = """

10mins+ commute  to be made on this day:
(1) 08:20-08:45 Brook Green to Imperial College
(2) 18:00-18:25 Imperial College to Brook Green

Anything else?
⏭ Details for your next journey

💡 Create an event
📝  Modify or delete an event

🏠 Thyme Home
⏹ Exit Thyme.
"""

link = """
You can save a lot more thyme if you link me with your calendar and reminder lists. 

Which calendar or list would you like me to link with?
🎓 Your Imperial College calendar
📅 Your personal calendar
💡 Create an event manually

🏠 Thyme Home
⏹ Exit Thyme
"""

linked = """

Hooray! You have successfully linked your calendar to Thyme! 🎉

How would you like me to notify you?
📞 Active notifications (Phone calls plus texts)
💬 Semi-active notifications (Text messages)
📲 Passive notifications (App notifications and banners) 
📵 No notifications
"""

requestmanual = """

Enter your event date/time, name and place, each surrounded with "double quotation marks" and seperated with a space. 💡
"""

deletedone = """

Your event has been deleted. 🚮 

Anything else?
🏠 Thyme Home
⏹ Exit Thyme
"""

notifications = """

You are now in notification preferences. 
How would you like me to notify you?
📞 Active notifications (Phone calls plus texts)
💬 Semi-active notifications (Text messages)
📲 Passive notifications (App notifications and banners)
📵 No notifications

🏠 Thyme Home
⏹ Exit Thyme
"""

time_interval = """

Your notifications has been updated.

When would you like me to call you in advance of your departure?
1️⃣ 5 minutes
2️⃣ 30 minutes
3️⃣ 1 hour.
4️⃣ All of the above.

🏠 Thyme Home
⏹ Exit Thyme
"""

settings_updated = """

Notification settings updated ❗️ 

🏠 Thyme Home
⏹ Exit Thyme
"""

requestmodify = """
Enter the number of the event you would like to modify. ✍️
"""

modifyerror = """
You have input an incorrect number.

How would you like to proceed?
⏭ Details for your next journe.
📝  Modify or delete an event

🏠 Thyme Home
⏹ Exit Thyme
"""

modifyoptions = """
What would you like to modify the event?

⏱ Modify event time
🔏 Modify event name
📌 Modify event location
🗺 Modify event directions
🗑 Delete event

🏠 Thyme Home
⏹ Exit Thyme
"""

modifylimit = """
Sorry, you cannot modify an event right now 😅. You can however delete an event and create a new one. Hopefully this will be implemented sometime later!

🏠 Thyme Home
⏹ Exit Thyme
"""

anything_else = """
Anything else?
🏠 Thyme Home
⏹ Exit Thyme
"""

requestdetail = """
Anything else?
📖 Detailed journey directions

🏠 Thyme Home
⏹ Exit Thyme
"""




