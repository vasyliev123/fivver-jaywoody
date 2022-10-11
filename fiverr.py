from telethon import TelegramClient
import time
import schedule

api_id = 9257340
api_hash = '83f3a9c114640d847a72457b5e4ef724'
client1 = TelegramClient('anon1', api_id, api_hash)
client2 = TelegramClient('anon2', api_id, api_hash)
client3 = TelegramClient('anon3', api_id, api_hash)
client4 = TelegramClient('anon4', api_id, api_hash)
client5 = TelegramClient('anon5', api_id, api_hash)
client6 = TelegramClient('anon6', api_id, api_hash)
client7= TelegramClient('anon7', api_id, api_hash)
async def main1():

    #FIVERR001
    groups = []
    async for dialog in client1.iter_dialogs():
        if(dialog.id < 0):
                print(dialog.name)
                groups.append(dialog.id)
    print(groups)      
    for group in groups:
        try:
            await client1.send_file(group, 'pic1.jpg')
            print("message sent to group" + str(group))
        except Exception as er:
            print(er)

async def main2():
    #FIVERR002
    groups = []
    async for dialog in client2.iter_dialogs():
        if(dialog.id < 0):
                print(dialog.name)
                groups.append(dialog.id)
    print(groups)      
    for group in groups:
        try:
            await client2.send_message(group, '!!UNBAN ANY INSTAGRAM ACCOUNT!!\n'+
            '\n'+
            '-Recover any account within 0-60 minutes✅\n'+
            "-Only need your @ 🙏\n"+
            '-All types of ban reasons except perm bans 🔨\n'+
            '-100% vetted and guaranteed to work💖\n'+
            '-Any account size🔥\n'+
            '-MM accepted❕\n'+
            '\n'+
            '-Plenty of testimonials and proof of work Just message me for more info🙌')
            print("message sent to group" + str(group))
            time.sleep(1)
        except Exception as er:
            print(er)

async def main3():    
    #FIVERR003
    groups = []
    async for dialog in client3.iter_dialogs():
        if(dialog.id < 0):
                print(dialog.name)
                groups.append(dialog.id)
    print(groups)      
    for group in groups:
        try:
            await client3.send_file(group,'pic3.jpg',caption=
            'DM me now to book🥰\n'+
            "-quality fans🔥\n"+
            '-never spam with shoutouts or s4s🔥✅\n'+
            '80k fans❤️‍🔥')
            print("message sent to group" + str(group))
            time.sleep(1)
        except Exception as er:
            print(er)

async def main4():
    #FIVERR004
    groups = []
    async for dialog in client4.iter_dialogs():
        if(dialog.id < 0):
                print(dialog.name)
                groups.append(dialog.id)
    print(groups)      
    for group in groups:
        try:
            await client4.send_message(group, '!!UNBAN ANY INSTAGRAM ACCOUNT!!\n'+
            '\n'+
            '-Recover any account within 0-60 minutes✅\n'+
            "-Only need your @ 🙏\n"+
            '-All types of ban reasons except perm bans 🔨\n'+
            '-100% vetted and guaranteed to work💖\n'+
            '-Any account size🔥\n'+
            '-MM accepted❕\n'+
            '\n'+
            '-Plenty of testimonials and proof of work Just message me for more info🙌')
            print("message sent to group" + str(group))
            time.sleep(1)
        except Exception as er:
            print(er)


async def main6():
    #FIVERR006
    groups = []
    async for dialog in client6.iter_dialogs():
        if(dialog.id < 0):
                print(dialog.name + " "+ str(dialog.id))
                groups.append(dialog.id)
    print(groups)      
    for group in groups:
        try:
            if group != -1001859762702:
                await client6.send_file(group, 'pic6.jpg',caption = '!!UNBAN ANY INSTAGRAM ACCOUNT!!\n'+
                '\n'+
                '-Recover any account within 0-60 minutes✅\n'+
                "-Only need your @ 🙏\n"+
                '-All types of ban reasons except perm bans 🔨\n'+
                '-Negotiable prices💰\n'+
                'Send me a message\n'+
                '@baddiprincess❤️‍🔥\n'+
                '@baddiprincess❤️‍🔥')
                print("message sent to group" + str(group))
                time.sleep(1)
        except Exception as er:
            print(er)

async def main5():
    #FIVERR005
    groups = []
    a = 1
    async for dialog in client5.iter_dialogs():
        if(dialog.id < 0):
                print(dialog.name)
                groups.append(dialog.id)
    print(groups)      
    for group in groups:
        try:
            await client5.send_file(group,'pic5.jpg',caption='!!UNBAN ANY INSTAGRAM ACCOUNT!!\n'+
            '\n'+
            '-Recover any account within 0-60 minutes✅\n'+
            "-Only need your @ 🙏\n"+
            '-All types of ban reasons except perm bans 🔨\n'+
            'Send me a message\n'+
            '@tashababe69❤️‍🔥\n'+
            '@tashababe69❤️‍🔥\n'+
            '@tashababe69❤️‍🔥')
            print("message sent to group" + str(group))
            time.sleep(60)
            a = a +1
        except Exception as er:
            print(er)


async def main7():
    #FIVERR007
    
    groups = []
    async for dialog in client7.iter_dialogs():
        if(dialog.id < 0):
                print(dialog.name)
                groups.append(dialog.id)
    print(groups)      
    for group in groups:
        try:
            await client7.send_file(group,'pic7.jpg', caption =  '-If you are looking for someone to manage and grow your page please DM me 🙏\n'+
            '\n'+
            '-We have been working with top models for 2 years now and are a quality agency ✅\n'+
            "-Only focus on a few pages at a time to maximize your PPV/earnings/ and fans. Proof of work can be shown and can start right away🔥")
            print("message sent to group" + str(group))
            time.sleep(60)
        except Exception as er:
    
            print(er)
       

def init():   
    with client1:
        client1.loop.run_until_complete(main1())
    with client2:
        client2.loop.run_until_complete(main2())
    with client3:
        client3.loop.run_until_complete(main3())
    with client4:
        client4.loop.run_until_complete(main4())
    
    with client6:
        client6.loop.run_until_complete(main6())
    
def init1():
    with client5:
        client5.loop.run_until_complete(main5())
    with client7:
        client7.loop.run_until_complete(main7())

schedule.every().hour.do(init)
schedule.every(15).minutes.do(init1)
while True:
    try:
        schedule.run_pending()
    except Exception as er:
        print(er)
    
    time.sleep(1)