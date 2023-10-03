import discord
import os

intents = discord.Intents.all()
intents.typing = False
intents.presences = False

class MyClient(discord.Client):
    def __init__(self, intents=intents, **kwargs):
        super().__init__(intents=intents, **kwargs)

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        # Verifica se a mensagem foi enviada em um servidor (guild)
        if message.guild:
            if message.content == '!regras':
                await message.channel.send(f'{message.author.name} as regras do servidor são:{os.linesep}1- Respeite os amigos{os.linesep}'
                                           f'2- Não xingue no chat'
                                           )
            if message.content == '!github':
                await message.channel.send(f'{message.author.name} o GitHub do Thigas é: https://github.com/Thigasssdev')
            if message.content == '!thigasbot':
                await message.channel.send(f'{message.author.name} o thigasbot, é um projeto pessoal desenvolvido com o objetivo de aprimorar minhas habilidades de programação e explorar o mundo da criação de chatbots. O Bot de Chat com Comandos é uma aplicação Python que permite a comunicação com o usuário por meio de uma interface de linha de comando, respondendo a comandos específicos.')
        else:
            # Se a mensagem foi enviada em particular (DM), envie uma mensagem informando que o bot não responde em mensagens privadas
            await message.author.send("Desculpe, não respondo em mensagens privadas. Por favor, use este comando em um servidor.")
            print(f'Message received in DM from {message.author.name}')

client = MyClient()
client.run('MTE1ODQyNDgwODk5NzAxMTUyNw.GqQqL1.fHMqZ_TZvry7Y4NxaOePwjByI_CmDnib_iowNc')
