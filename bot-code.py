import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print("Ich habe mich eingeloggt. Beep bop. ")

    #Wenn eine Nachricht gepostet wird
    async def on_message(self, message):
        print("Nachricht von " + str(message.author) + " enthält " + message.content)
        if message.author == client.user:
            return

        if message.content.startswith("hey bot"):
            await message.channel.send("Hallo!!!111!1")

        if message.content.startswith("test"):
            await message.channel.send("123, test, test")

        if message.content.startswith("pi"):
            await message.channel.send("ist 3,1415926535 8979323846 2643383279 5028841971 6939937510 ...")


client = MyClient()
client.run("YOUR_CLIENT_ID_HERE")
