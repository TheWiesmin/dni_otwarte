import discord
from captcha.image import ImageCaptcha
import random
import string
from asyncio import sleep

image = ImageCaptcha(fonts=['./lato.ttf'])
codes = []
verified = []


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.lower().startswith('!kod'):
            msg = message.content.lower()[-4:]
            if [message.author.id, msg] in codes:
                await message.channel.send("Zweryfikowano pomyślnie")
                print(message.author.id)
                verified.append([message.author.id])
                print("verified: ".join(str(e) for e in verified))
            else:
                await message.channel.send("Spróbuj jeszcze raz.")

        if message.content.lower().startswith('!wycisz'):
            if message.author.roles.pop().name == "Admin":
                if message.author.voice.channel is not None:
                    role = message.guild.get_role(717479176403288155)
                    await message.author.voice.channel.set_permissions(role, speak=False)

        if message.content.lower().startswith('!pytania'):
            if message.author.roles.pop().name == "Admin":
                if message.author.voice.channel is not None:
                    role = message.guild.get_role(717479176403288155)
                    await message.author.voice.channel.set_permissions(role, speak=True)

    async def on_voice_state_update(self, member, before, after):
        print(after.channel)
        if after.channel is not None:
            if after.channel.id == 718209251322888303:
                print(1)
                channel = client.get_channel(718158054079594528)
                await member.move_to(channel)
                text = client.get_channel(718174125906198599)
                await text.send("Witaj na Dniach Otwartych Zespołu Szkół Łączonści!")
                await captcha(self, member)
                await sleep(30)
                print(member.id)
                if member.id not in verified:
                    await text.send("**NIE UMIESZ PISAĆ** *(kick)*")
                else:
                    await text.send("Zaczekaj na rozpoczęcie dni otwartych...")


async def captcha(self, member):
    e = discord.Embed(title="Test", description="Wpisz !<kod z obrazka>", color=0x00ff00)
    channel = client.get_channel(718174125906198599)
    code = random_string()
    image.write(code, 'out.png')
    print(code)
    await channel.send(file=discord.File('out.png'))
    await channel.send("aby orzpocząć wpisz *!kod <numer z obrazka>* \n *np. !kod 1234*")
    codes.append([member.id, code])
    print("codes: ".join(str(e) for e in codes))


def random_string():
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(4))


client = MyClient()
client.run('NzE4MTUzNTMzNjg5NjkyMzMz.XtqXZA.DmfMI3EHhQOhJE4PU5y1Ndf8etg')
