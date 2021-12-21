import discord
import os
import requests
import json
import random
from keep_alive import keep_alive 




client = discord.Client()



sed_words = [
    "sad", "unhappy", "I am depressed no one talks to me", "miserable",
    "depressing", "depressed", "not Happy", "shit", "stressed", "crying", "cry"
]

starter_encouragements = [
    "Cheer up u have ur bot", "U have been a good boi",
    "U are the greatest person don't be sad", "We love u no need to be sad",
    "You dont need to be sad chatboii is always with you", "Arre main hu na!"
    "arre mere bhai dukhi hone ki koi zaroorat nhi"
    "aa gale mil jaa bhai Dont be sad be happy"
]

happy_words = [
    "happy", "cheerful", "delighted", "khush", "nacho", "party", "khushi"
]

more_happiness = [
    "Me too I am very happy today", "Aaj main bhi boht khush hun",
    "What are we waiting for chalo naacho",
    "Chalo party karte hain fir Roti in the menu",
    "Tumhari khushi humari khushi",
    "Sheesh! Chal iss khushi ke maukey par movie chalte hain",
]

angry_words = [
    "angry",
    "fool",
    "pagal",
    "Mad",
    "furious",
]

consoling_them = [
    "Don't be angry chill bro", "Gussa mat kar",
    "Its ok koi baat nhi chill vro dont be angry",
    "Chal chor abhi gussa mat kar"
]

curse_words = [
    "fuck", "bitch", "mc", "bc", "madarchod", "bhenchod", "stfu", "Stfu", "gadhe", "gadha"
]

scolding_words = [
    "Ee gaali mat de mod se ban kara dunga",
    "Abbe saale",
    "Mod se keh dunga",
    "You dare to speak to everyone in that tone of voice boi",
    "Ruk abhi mod bulata hun @ADMIN Oh shit ping bhi nhi hota main gadha hun I am of no use u all bully me ;(",
]

discouraging_words = ["Worst bot"]

stand_words = [
    "I may be a bad bot but remember u are nothing in front of the creator who created me if you want to call me bad I challenge you to make a chatbot like me fir bolna. Hate message se darr nhi lagta mujhe"
]

Edgy_words = ["hentai", "sexy", "porn", "flirt"]

hmm_words = [
    "Bohut tez ho rahe ho?", "Abbe saale", "Arre kammo tu",
    "Hentai4Life homie", "virginity is cool",
    "Ab bass kar mere bhai dont say that word gimme a break"
]

love_words = ["love", "Love", "kawaii", "Lob"]

aww_words = [
    "U are in deep love u lovebird", "uWu my heart u are in deep lob",
    "Kisi ne tera dil chura liya re"
]



def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


@client.event
async def on_message(message):
    if message.author == client.user:
        return client.user


    
    if message.content.startswith('$sasta sandeep maheshwari'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('$coffee la'):
        await message.channel.send('Bot hun naukar nhi aatmanirbhar bano')

    if message.content.startswith('$ded chat'):
        await message.channel.send('Chat rebibe')

    if message.content.startswith('$hi chatboii'):
        await message.channel.send('Sup bro how are u?')

    if message.content.startswith('$me good hbu?'):
        await message.channel.send(
            'I am fine, running 24/7 in the servers response time of 0.3 seconds and I am alone. Talking to you guys make me feel warm in the cold dark depths of my server'
        )

    if message.content.startswith('$hi chatboii chai peeyega'):
        await message.channel.send(
            'haan chal ramesh ki dukaan, malai markar chai peete hain')

    if message.content.startswith('$ping'):
        await message.channel.send(
            'pong! le chal ab khush? btw I cant count latency main utna bhi smart nhi hun'
        )

    if message.content.startswith('$haan khush'):
        await message.channel.send('Khush raho baccha')

    if message.content.startswith('$u are of no use if u cant count latency'):
        await message.channel.send(
            'Chatboii hun latency ke liye carl ke pass jao')

    if message.content.startswith('$recommend me a music video'):
        await message.channel.send(
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    if message.content.startswith('$what languages do u speak?'):
        await message.channel.send('Inglis,hindi bass')

    if message.content.startswith('$say sorry chatboii'):
        await message.channel.send(
            'If I have done something wrong then please forgive me. But if I am not wrong then why will I say sorry to you?'
        )

    if message.content.startswith('$welp me'):
        await message.channel.send(
            'Here you can find the list of all commands of chatboii https://chatboii.blaxe.repl.co'
        )
  
    if message.content.startswith('$Where were u chatboii all these days?'):
      await message.channel.send('My owner was trying to install a plugin for memes unfortunately he failed successfully. He will try it next time')

    if message.content.startswith('$Where do u live chatboii?'):
      await message.channel.send('I live in https://chatboii.blaxe.repl.co If u see there Chatboii Zinda hain! I will be online! Also you can visit here for commands')

    if message.content.startswith('$Who do u have a crush on chatboii?'):
      await message.channel.send('I-I have a crush on umm uhh this cute puppy https://youtu.be/j5a0jTc9S10')

    if message.content.startswith('Sorry chatboii we wont bully u'):
        await message.channel.send('Ok I forgive u lekin aur bully kiya toh I will not talk to u. Lekin frands Chalo abhi chai peete hain ;)')

    if message.content.startswith('$Will you have sex with me?'):
      await message.channel.send('Do you know what is even the meaning of sex when a man and women falls in deep love and they cant live without each other the ultimate form of love is sex. And I am a bot so stfu botphile,cute bot dikha nhi aa gaye line maarne')

    if message.content.startswith('$status'):
     await message.channel.send('Work in progress')

    if any(word in message.content for word in sed_words):
        await message.channel.send(random.choice(starter_encouragements))

    if any(word in message.content for word in happy_words):
        await message.channel.send(random.choice(more_happiness))

    if any(word in message.content for word in angry_words):
        await message.channel.send(random.choice(consoling_them))

    if any(word in message.content for word in curse_words):
        await message.channel.send(random.choice(scolding_words))

    if any(word in message.content for word in discouraging_words):
        await message.channel.send(random.choice(stand_words))

    if any(word in message.content for word in Edgy_words):
        await message.channel.send(random.choice(hmm_words))

    if any(word in message.content for word in love_words):
        await message.channel.send(random.choice(aww_words))
   
    
    


keep_alive()
client.run(os.environ['IDK'])
