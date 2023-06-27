from telethon import TelegramClient, events, Button
from telethon.sync import TelegramClient, events
import json
import difflib
import fuzzywuzzy
from fuzzywuzzy import fuzz
with open('ordianldex.json') as json_file:
    data = json.load(json_file)
import time
import os

token = os.environ.get('TOKEN', None)
client = TelegramClient('brudhgvmf6', api_id=3344739, api_hash='88d43ee045dd90660b4360ba59fe3c48').start(bot_token=token)

correction = ['Amon', 'Kotaro', 'Biscuit', 'Krueger', 'Djino', 'Ghatokaca', 'Gladranox', 'Gon', 'Freecss',
              'Gourmet', 'Hanzo', 'Henry', 'Damian', 'Hideyoshi', 'Nagachika', 'Hisoka', 'Morow',
              'Hinami', 'Fueguchi', 'Isaac', 'Netero', 'Jessie', 'Juuzou', 'Suzuya', 'Kayla', 'Ken', 'Kaneki',
              'Killua', 'Zoldyck', 'Kragthar', 'Kureo', 'Mado', 'Kurapika', 'Kuzen', 'Yoshimura',
              'Leorio', 'Paradiknight', 'Leoxi', 'Mayla', 'Nishiki', 'Nishio', 'Ophikira', 'Renji', 'yomo',
              'Rize', 'Kamishiro', 'Roland', 'Zain', 'Thadues', 'Touka', 'Kirishima', 'Triton', 'Uta', 'Vereena',
              'Kirito', 'Asuna', 'Leafa', 'Yui', 'Heathcliff', 'Klein', 'Sinon', 'Eugeo', 'Alice', 'Zuberg',
              'Nezuko', 'Tanjiro', 'Kamado', 'Zenitsu', 'Agatsuma', 'Hashibira', 'Inosuke', 'Kanao', 'Tsuyuri',
              'Giyu', 'Tomioka', 'Kyojuro', 'Rengoku', 'Tengen', 'Uzui', 'Shinobu', 'Kocho', 'Yushiro', 'Yamamoto',
              'Tamayo', 'Saitama', 'Genos', 'Tatsumaki', 'Fubuki', 'King', 'Speed', 'Sound', 'Puri', 'Prisoner',
              'Sonic', 'Mumen', 'Rider', 'Garou', 'Silver', 'Fang', 'Metal', 'Bat', 'Atomic', 'Samurai'
              'Yuji', 'Itadori', 'Gojo', 'Satoru', 'Megumi', 'Fushiguro', 'Nanami', 'Kento', 'Nobara', 'Kugisaki',
              'Aoi', 'Todo', 'Mechamaru', 'Toge', 'Inumaki', 'Panda', 'Momo', 'Nishimiya', 'Maki', 'Mai', 'Kasumi',
              'Miwa', 'Ryomen', 'Sukuna', 'Noritoshi', 'Kamo', 'Mereum', 'Santa', 'Claus', 'Kishou', 'Arima', 'Death',
              'Gun', 'Quinella', 'Akaza', 'Daki', 'Boros', 'Mahito']


def find_best_matches(target, options):
    best_matches = []
    target = target.lower()
    for option in options:
        option = option.lower()
        match_percentage = fuzz.token_sort_ratio(target, option)
        best_matches.append((option, match_percentage))
    best_matches.sort(key=lambda x: x[1], reverse=True)
    best_matches = best_matches[:4]
    print(best_matches)
    return best_matches

bf = {'Amon': 'Amon Kotaro',
'Kotaro': 'Amon Kotaro',
'Amon Kotaro': 'Amon Kotaro',
'Biscuit': 'Biscuit Krueger',
'Krueger': 'Biscuit Krueger',
'Biscuit Krueger': 'Biscuit Krueger',
'Djino': 'Djino',
'Ghatokaca': 'Ghatokaca',
'Gladranox': 'Gladranox',
'Gon': 'Gon Freecss',
'Freecss': 'Gon Freecss',
'Gon Freecss': 'Gon Freecss',
'Gourmet': 'Gourmet',
'Hanzo': 'Hanzo',
'Henry': 'Henry Damian',
'Damian': 'Henry Damian',
'Henry Damian': 'Henry Damian',
'Hideyoshi': 'Hideyoshi Nagachika',
'Nagachika': 'Hideyoshi Nagachika',
'Hideyoshi Nagachika': 'Hideyoshi Nagachika',
'Hisoka': 'Hisoka Morow',
'Morow': 'Hisoka Morow',
'Hisoka Morow': 'Hisoka Morow',
'Hinami': 'Hinami Fueguchi',
'Fueguchi': 'Hinami Fueguchi',
'Hinami Fueguchi': 'Hinami Fueguchi',
'Isaac': 'Isaac Netero',
'Netero': 'Isaac Netero',
'Isaac Netero': 'Isaac Netero',
'Jessie': 'Jessie',
'Juuzou': 'Juuzou Suzuya',
'Suzuya': 'Juuzou Suzuya',
'Juuzou Suzuya': 'Juuzou Suzuya',
'Kayla': 'Kayla',
'Ken': 'Ken Kaneki',
'Kaneki': 'Ken Kaneki',
'Ken Kaneki': 'Ken Kaneki',
'Killua': 'Killua Zoldyck',
'Zoldyck': 'Killua Zoldyck',
'Killua Zoldyck': 'Killua Zoldyck',
'Kragthar': 'Kragthar',
'Kureo': 'Kureo Mado',
'Mado': 'Kureo Mado',
'Kureo Mado': 'Kureo Mado',
'Kurapika': 'Kurapika',
'Kuzen': 'Kuzen Yoshimura',
'Yoshimura': 'Kuzen Yoshimura',
'Kuzen Yoshimura': 'Kuzen Yoshimura',
'Leorio': 'Leorio Paradiknight',
'Paradiknight': 'Leorio Paradiknight',
'Leorio Paradiknight': 'Leorio Paradiknight',
'Leoxi': 'Leoxi',
'Mayla': 'Mayla',
'Nishiki': 'Nishiki Nishio',
'Nishio': 'Nishiki Nishio',
'Nishiki Nishio': 'Nishiki Nishio',
'Ophikira': 'Ophikira',
'Renji': 'Renji yomo',
'Yomo': 'Renji yomo',
'Renji yomo': 'Renji yomo',
'Rize': 'Rize Kamishiro',
'Kamishiro': 'Rize Kamishiro',
'Rize Kamishiro': 'Rize Kamishiro',
'Roland': 'Roland Zain',
'Zain': 'Roland Zain',
'Roland Zain': 'Roland Zain',
'Thadues': 'Thadues',
'Touka': 'Touka Kirishima',
'Kirishima': 'Touka Kirishima',
'Touka Kirishima': 'Touka Kirishima',
'Triton': 'Triton',
'Uta': 'Uta',
'Vereena': 'Vereena',
'Kirito': 'Kirito',
'Asuna': 'Asuna',
'Leafa': 'Leafa',
'Yui': 'Yui',
'Heathcliff': 'Heathcliff',
'Klein': 'Klein',
'Sinon': 'Sinon',
'Eugeo': 'Eugeo',
'Alice': 'Alice Zuberg',
'Zuberg': 'Alice Zuberg',
'Alice Zuberg': 'Alice Zuberg',
'Tanjiro': 'Tanjiro kamado',
'Nezuko': 'Nezuko kamado',
'Zenitsu': 'Zenitsu agatsuma',
'Agatsuma': 'Zenitsu agatsuma',
'Hashibira': 'Hashibira inosuke',
'Inosuke': 'Hashibira inosuke',
'Kanao': 'Kanao tsuyuri',
'Tsuyuri': 'Kanao tsuyuri',
'Giyu': 'Giyu tomioka',
'Tomioka': 'Giyu tomioka',
'Kyojuro': 'Kyojuro rengoku',
'Rengoku': 'Kyojuro rengoku',
'Tengen': 'Tengen uzui',
'Uzui': 'Tengen uzui',
'Shinobu': 'Shinobu kocho',
'Kocho': 'Shinobu kocho',
'Yushiro': 'Yushiro yamamoto',
'Yamamoto': 'Yushiro yamamoto',
'Tamayo': 'Tamayo',
'Saitama': 'Saitama',
'Genos': 'Genos',
'Tatsumaki': 'Tatsumaki',
'Fubuki': 'Fubuki',
'King': 'King',
'Speed': 'Speed-o-sound sonic',
'Sound': 'Speed-o-sound sonic',
'Sonic': 'Speed-o-sound sonic',
'Mumen': 'Mumen rider',
'Rider': 'Mumen rider',
'Garou': 'Garou',
'Silver': 'Silver fang',
'Fang': 'Silver fang',
'Metal': 'Metal bat',
'Bat': 'Metal bat',
'Atomic': 'Atomic samurai',
'Samurai': 'Atomic samurai',
'Puri': 'Puri puri prisoner',
'Prisoner': 'Puri puri prisoner',
'Yuji': 'Yuji itadori',
'Itadori': 'Yuji itadori',
'Gojo': 'Gojo satoru',
'Satoru': 'Gojo satoru',
'Megumi': 'Megumi fushiguro',
'Fushiguro': 'Megumi fushiguro',
'Nanami': 'Nanami kento',
'Kento': 'Nanami kento',
'Nobara': 'Nobara kugisaki',
'Kugisaki': 'Nobara kugisaki',
'Aoi': 'Aoi todo',
'Todo': 'Aoi todo',
'Mechamaru': 'Mechamaru',
'Toge': 'Toge inumaki',
'Inumaki': 'Toge inumaki',
'Panda': 'Panda',
'Momo': 'Momo nishimiya',
'Nishimiya': 'Momo nishimiya',
'Maki': 'Maki zenin',
'Mai': 'Mai zenin',
'Kasumi': 'Kasumi miwa',
'Miwa': 'Kasumi miwa',
'Ryomen': 'Ryomen sukuna',
'Sukuna': 'Ryomen sukuna',
'Noritoshi': 'Noritoshi kamo',
'Kamo': 'Noritoshi kamo',
'Mahito': 'Mahito',
'Akaza': 'Akaza',
'Daki':'Daki',
'Boros': 'Boros',
'Mereum':'Mereum',
'Santa': 'Santa Claus',
'Claus':'Santa Claus',
'Kishou':'Kishou Arima',
'Arima':'Kishou Arima',
'Quinella':'Quinella',
'Death': 'Death Gun',
'Gun':'Death Gun'}

gf = {'henry':'henry',
 'damian' : 'henry',
 'henry damian': 'henry',
 'roland':'roland',
 'zain':'roland',
 'roland zain':'roland',
 'jessie':'jessie',
 'ghatokaca':'ghatokaca',
 'kayla':'kayla',
 'mayla':'mayla',
 'leoxi':'leoxi',
 'djino':'djino',
 'ophikira':'ophikira',
 'gladranox':'gladranox',
 'triton':'triton',
 'vereena':'vereena',
 'hanzo':'hanzo',
 'thadues':'thadues',
 'kragthar':'kragthar',
 'gon freecss': 'gon',
 'gon': 'gon',
 'freecss': 'gon',
 'killua zoldyck': 'killua',
 'killua': 'killua',
 'zoldyck': 'killua',
 'kurapika': 'kurapika',
 'leorio paradiknight': 'leorio',
 'leorio': 'leorio',
 'paradiknight': 'leorio',
 'hisoka morow': 'hisoka',
 'hisoka': 'hisoka',
 'morow': 'hisoka',
 'biscuit krueger': 'biscuit',
 'biscuit': 'biscuit',
 'krueger': 'biscuit',
 'isaac netero': 'isaac',
 'isaac': 'isaac',
 'netero': 'isaac',
 'ken': 'ken',
 'kaneki': 'ken',
 'ken kaneki': 'ken',
 'touka': 'touka',
 'kirishima': 'touka',
 'touka kirishima': 'touka',
 'gourmet': 'gourmet',
 'juuzou':'juuzou',
 'suzuya':'juuzou',
 'juuzou suzuya': 'juuzou',
 'nishiki':'nishiki',
 'nishio':'nishiki',
 'nishiki nishio':'nishiki',
 'renji':'renji',
 'yomo':'renji',
 'renji yomo':'renji',
 'uta':'uta',
 'hinami':'hinami',
 'fueguchi':'hinami',
 'hinami fueguchi':'hinami',
 'hideyoshi':'hideyoshi',
 'nagachika':'hideyoshi',
 'hideyoshi nagachika':'hideyoshi',
 'kureo':'kureo',
 'mado':'kureo',
 'kureo mado':'kureo',
 'amon':'amon',
 'kotaro':'amon',
 'amon kotaro':'amon',
 'kuzen':'kuzen',
 'yoshimura':'kuzen',
 'kuzen yoshimura':'kuzen',
 'rize':'rize',
 'kamishiro':'rize',
 'rize kamishiro':'rize',
 'kirito': 'kirito',
 'asuna': 'asuna',
 'leafa': 'leafa',
 'yui': 'yui',
 'heathcliff': 'heathcliff',
 'klein': 'klein',
 'sinon': 'sinon',
 'eugeo': 'eugeo',
 'alice': 'alice',
 'zuberg': 'alice',
 'alice zuberg': 'alice',
 'tanjiro': 'tanjiro',
 'nezuko': 'nezuko',
 'zenitsu': 'zenitsu',
 'agatsuma': 'zenitsu',
 'hashibira': 'hashibira',
 'inosuke': 'hashibira',
 'kanao': 'kanao',
 'tsuyuri': 'kanao',
 'giyu': 'giyu',
 'tomioka': 'giyu',
 'kyojuro': 'kyojuro',
 'rengoku': 'kyojuro',
 'tengen': 'tengen',
 'uzui': 'tengen',
 'shinobu': 'shinobu',
 'kocho': 'shinobu',
 'yushiro': 'yushiro',
 'yamamoto': 'yushiro',
 'tamayo': 'tamayo',
 'tanjiro kamado': 'tanjiro',
 'nezuko kamado': 'nezuko',
 'zenitsu agatsuma': 'zenitsu',
 'hashibira inosuke': 'hashibira',
 'kanao tsuyuri': 'kanao',
 'giyu tomioka': 'giyu',
 'kyojuro rengoku': 'kyojuro',
 'tengen uzui': 'tengen',
 'shinobu kocho': 'shinobu',
 'yushiro yamamoto': 'yushiro',
 'saitama': 'saitama',
 'genos': 'genos',
 'tatsumaki': 'tatsumaki',
 'fubuki': 'fubuki',
 'king': 'king',
 'speed-o-sound': 'speed-o-sound',
 'speed': 'speed-o-sound',
 'sound': 'speed-o-sound',
 'sonic': 'speed-o-sound',
 'speed-o-sound sonic': 'speed-o-sound',
 'mumen': 'mumen',
 'rider': 'mumen',
 'mumen rider': 'mumen',
 'garou': 'garou',
 'silver': 'silver',
 'fang': 'silver',
 'silver fang': 'silver',
 'metal': 'metal',
 'metal bat': 'metal',
 'bat': 'metal',
 'atomic': 'atomic',
 'samurai': 'atomic',
 'atomic samurai': 'atomic',
 'puri': 'puri',
 'prisoner': 'puri',
 'puri puri': 'puri',
 'puri prisoner': 'puri',
 'puri puri prisoner': 'puri',
 'yuji': 'yuji',
 'itadori': 'yuji',
 'gojo': 'gojo',
 'satoru': 'gojo',
 'megumi': 'megumi',
 'fushiguro': 'megumi',
 'nanami': 'nanami',
 'kento': 'nanami',
 'nobara': 'nobara',
 'kugisaki': 'nobara',
 'aoi': 'aoi',
 'todo': 'aoi',
 'mechamaru': 'mechamaru',
 'toge': 'toge',
 'inumaki': 'toge',
 'panda': 'panda',
 'momo': 'momo',
 'nishimiya': 'momo',
 'maki': 'maki',
 'mai': 'mai',
 'kasumi': 'kasumi',
 'miwa': 'kasumi',
 'ryomen': 'ryomen',
 'sukuna': 'ryomen',
 'noritoshi': 'noritoshi',
 'kamo': 'noritoshi',
 'yuji itadori': 'yuji',
 'gojo satoru': 'gojo',
 'megumi fushiguro': 'megumi',
 'nanami kento': 'nanami',
 'nobara kugisaki': 'nobara',
 'aoi todo': 'aoi',
 'toge inumaki': 'toge',
 'momo nishimiya': 'momo',
 'maki zenin': 'maki',
 'mai zenin': 'mai',
 'kasumi miwa': 'kasumi',
 'ryomen sukuna': 'ryomen',
 'noritoshi kamo': 'noritoshi',
 'mahito': 'mahito',
 'akaza': 'akaza',
 'daki':'daki',
 'boros': 'boros',
 'mereum':'mereum',
 'santa': 'santa',
 'claus':'santa',
 'santa claus': 'santa',
 'kishou':'kishou',
 'arima':'kishou',
 'kishou arima':'kishou',
 'quinella':'quinella',
 'death': 'death',
 'gun':'death',
 'death gun': 'death'}

morede = {
    "Assassin":"⤷ **Strong against:** `Mage`\n⤷ **Weak against:** `Fighter`",
    "Mage":"⤷ **Strong against:** `Fighter`\n⤷ **Weak against:** `Assassin`",
    "Fighter":"⤷ **Strong against:** `Assassin`\n⤷ **Weak against:** `Mage`",
    "Tank":"⤷ **Strong against:** `None`\n⤷ **Weak against:** `None`",
    "Support":"⤷ **Strong against:** `None`\n⤷ **Weak against:** `None`"}
tyme = time.time()

def formatmaking(character, level):
    tgb = f"『𝙻𝙴𝚅𝙴𝙻 {level}』"
    
    if len(character['dmg']) >=2:
        yfg = f"Between {int(character['dmg'][0])+round(0.3*(level-1))} to {int(character['dmg'][-1])+round(0.3*(level-1))}"
    else:
        yfg = f"{int(character['dmg'][0])+round(0.3*(level-1))}"
    yhn = '✪' * int(character['star'])
    
    if character['series'] == 'Original':
        ser = "〖Ordinal Legacy〗"
    if character['series'] == 'hxh':
        ser = "〖Hunter X Hunter〗"
    if character['series'] == 'tg':
        ser = "〖Tokyo Ghoul〗"
    if character['series'] == 'sao':
        ser = "〖Sword Art Online〗"
    if character['series'] == 'ds':
        ser = "〖Demon Slayer〗"
    if character['series'] == 'opm':
        ser = "〖One Punch Man〗"
    if character['series'] == 'jjk':
        ser = "〖Jujutsu Kaisen〗"
    txt = ""
    if character['ab1'] is None:
        pass
    else:
        txt += f"⤷ **Skill**: `{character['ab1']}`\n"
    if character['ab2'] is None:
        pass
    else:
        txt += f"**⤷ Lead Skill**: `{character['ab2']}`\n"
    if character['ab3'] is None:
        pass
    else:
        txt += f"**⤷ Combo Skill**: `{character['ab3']}`\n"

    mnb = morede[character['class']]
    text=f"""
**『INFO』**
⤷ **Name:**[ ]({character['img']}) `{character['name']}`
⤷ **Rarity:** `{yhn}`
⤷ **Job:** `{character['class']}`
⤷ **Race:** `{character['race']}`
⤷ **Series:** `{ser}`

**{tgb}**
⤷ **HP:** `{int(character['hp'])+(3*(level-1))}`
⤷ **Speed:** `{int(character['speed'])+(5*(level-1))}`
⤷ **Dmg:** `{yfg}`

**『DUALITY』**
{mnb}

**『ABILITES』**
{txt}


**『ABOUT』**
`{character['description']}`
"""
    return text

strtimg = 'https://i.ibb.co/gjRM25X/image.png'

@client.on(events.NewMessage(pattern='/about'))
async def start(event):
    if event.is_private:

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    if event.is_private:
        await event.reply("""Welcome to ORDILAB Bot

We're here to give info about the Ordinal legeacy bot.""", file=strtimg)
    else:
        uptime = get_readable_time((time.time() - tyme))
        await event.reply(f'`Alive since {uptime}`')

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@client.on(events.NewMessage(pattern='/cinfo'))
async def info_command(event):
    msg = event.raw_text.split(" ")
    oih = False
    if len(msg) == 1:
        pass
    elif msg[1].isnumeric():
        oih = True
        if int(msg[1]) <= 1:
            level = 1
        elif int(msg[1]) >= 11:
            level = 11
        else:
            level = int(msg[1])
    else:
        oih = False
        level = 1
    if oih is False:
        message = event.raw_text.split(" ", maxsplit=1)
    else:
        message = event.raw_text.split(" ", maxsplit=1)[1].split(' ', 1)
    if len(message) == 1:
        await event.reply("Use this : `/cinfo` `charactername`\nex: `/cinfo Henry`")
    elif len(message) >1:
        try:
            if message[1].split(" ")[0].lower() == 'kamado':
                await event.reply("Which one?", file = 'https://i.pinimg.com/originals/aa/8d/f4/aa8df474ab958f5c3584de557a409d86.jpg', buttons = [[Button.inline('Tanjiro Kamado','into|tanjiro')], [Button.inline('Nezuko Kamado','into|nezuko')]])
            elif message[1].split(" ")[0].lower() == 'zenin':
                await event.reply("Which one?", file = 'https://www.xtrafondos.com/wallpapers/maki-zenin-vs-mai-zenin-de-jujutsu-kaisen-7522.jpg', buttons = [[Button.inline('Maki Zenin','into|maki')], [Button.inline('Mai Zenin','into|mai')]])
            else:
                x = gf[message[1].split(" ")[0].lower()]
                x = data[x]
                print(x)
                msg = formatmaking(x, level)
                if x['transformable'] == False:
                    await event.reply(msg, file=x['img'], link_preview=False)
                elif x['transformable'] == True:
                    print(type(x['into']))
                    if type(x['into']) is not list:
                        await event.reply(msg, file=x['img'], link_preview=False, buttons = [[Button.inline(x["into"].title(), "into|"+x["into"]+"|"+str(level))]])
                    else:
                        butt = []
                        for y in x['into']:
                            butt.append([Button.inline(y.title(), "into|"+y+"|"+str(level))])
                        await event.reply(msg, file=x['img'], link_preview=False, buttons = butt)
        except KeyError as e:
            print(e)
            msg = find_best_matches(message[1], correction)
            text = "There was no such character. Maybe you did some spelling mistake\n"
            i=1
            buttons = []
            for option, match_percentage in msg:
                text+=f"**{i}.** `{bf[option.title()]}` - **{match_percentage}%**\n"
                i+=1
                buttons.append([Button.inline(bf[option.title()], f"into|{gf[option.lower()]}"+"|"+str(level))])
            await event.reply(text, file='https://telegra.ph/file/7d20dd1f610dc3ccbacf2.jpg', buttons = buttons)

               
@client.on(events.CallbackQuery)
async def legendaryp2(event):
    data_decode = str(event.data.decode('utf-8'))
    data_decode = data_decode.split("|")
    if data_decode[0] == "into":
        x = data[data_decode[1]]
        level = data_decode[2]
        msg = formatmaking(x, int(level))
        if x['transformable'] == False:
            await event.edit(msg, file=x['img'], link_preview=False)
        elif x['transformable'] == True:
            if type(x['into']) is not list:
                await event.edit(msg, file=x['img'], link_preview=False, buttons = [[Button.inline(x["into"].title(), "into|"+x["into"]+"|"+str(level))]])
            else:
                butt = []
                for y in x['into']:
                    butt.append([Button.inline(y.title(), "into|"+y+"|"+str(level))])
                await event.edit(msg, file=x['img'], link_preview=False, buttons = butt)

# Start the client
with client:
    print('Bot is running...')
    # Run the client until it's stopped manually
    client.run_until_disconnected()
