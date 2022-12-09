from telethon import TelegramClient
import time
import sched
# import schedule
import threading

api_id = 9257340
api_hash = '83f3a9c114640d847a72457b5e4ef724'

client7783209995 = TelegramClient('client7783209995', api_id, api_hash)  # 6
client7168156028 = TelegramClient('client7168156028', api_id, api_hash)  # 5

client6048617357 = TelegramClient('client6048617357', api_id, api_hash)  # 4
client6164693954 = TelegramClient('client6164693954', api_id, api_hash)

client3237391651 = TelegramClient('client3237391651', api_id, api_hash)  # 14
client7373203283 = TelegramClient('client7373203283', api_id, api_hash)  # 13
print("1")
client7783209995.start()
print("2")
client7168156028.start()
print("3")
client6048617357.start()
print("4")
client6164693954.start()
print("5")
client3237391651.start()
print("6")
client7373203283.start()


async def main4():
    # FIVERR004
    groups = []
    print("CLIENT 4 IS RUNNING")
    async for dialog in client6048617357.iter_dialogs():
        if (dialog.id < 0):
            print(dialog.name)
            groups.append(dialog.id)
    print(groups)
    for group in groups:
        try:
            await client6048617357.send_file(group, 'pic4.png', caption=
            "Please dm me if interested‼️\n" +
            "-unban quick⏩\n" +
            "-just need your @ and screen record of you logging in👇\n" +
            "-cheapest unban services 💰")
            print("CLIENT 4 message sent to group" + str(group))
            time.sleep(1)
        except Exception as er:
            print(er)


async def main5():
    # FIVERR005
    print("CLIENT 5 RUNNING")
    groups = []
    a = 1
    async for dialog in client7168156028.iter_dialogs():
        if (dialog.id < 0):
            print(dialog.name)
            groups.append(dialog.id)
    print(groups)
    for group in groups:
        try:
            await client7168156028.send_message(group, '!!UNBAN ANY INSTAGRAM ACCOUNT!!\n' +
                                                '\n' +
                                                '-Recover any account within 0-60 minutes✅\n' +
                                                "-Only need your @ 🙏\n" +
                                                '-All types of ban reasons except perm bans 🔨\n' +
                                                'Send me a message\n' +
                                                '@tashababe69❤️‍🔥\n' +
                                                '@tashababe69❤️‍🔥\n' +
                                                '@tashababe69❤️‍🔥')
            print("CLIENT 5 message sent to group" + str(group))
            time.sleep(1)
            a = a + 1
        except Exception as er:
            print(er)


async def main6():
    # FIVERR006
    print("CLIENT 6 IS RUNNING")
    groups = []
    async for dialog in client7783209995.iter_dialogs():
        if (dialog.id < 0):
            print(dialog.name + " " + str(dialog.id))
            groups.append(dialog.id)
    print(groups)
    for group in groups:
        time.sleep(1)
        try:

            if group != -1001859762702 and group != -1001783222691:
                await client7783209995.send_file(group, 'pic3.jpg')
                print("CLIENT 6 message sent to group" + str(group))

        except Exception as er:
            print(er)


async def main13():
    # FIVERR012

    print("CLIENT13 IS RUNNING")
    groups = []
    async for dialog in client7373203283.iter_dialogs():
        if (dialog.id < 0):
            print(dialog.name)
            groups.append(dialog.id)
    print(groups)
    for group in groups:
        time.sleep(1)
        try:
            await client7373203283.send_message(group, "REDDIT ADVERTISING COURSE AVAILABLE FOR ONLY $20🔥📈\n" +
                                                "\n" +
                                                "We have used reddit advertising for years with many models who started from scratch and others in the top 1%. Reddit is an easy and effective way to gain quality fans because they are SPENDERS and constantly looking 💰\n" +
                                                "\n" +
                                                "There are hundreds of subreddits to post in which gives any girl from thick to thin the ability to gain attention 💕\n" +
                                                "\n" +
                                                "You can implement the strategies right away and start gaining fans within the first week. PLEASE DM me for more details! ⚡️")
            print("CLIENT 13 message sent to group" + str(group))

        except Exception as er:

            print(er)


async def main14():
    # FIVERR014

    print("CLIENT14 IS RUNNING")
    groups = []
    async for dialog in client3237391651.iter_dialogs():
        if (dialog.id < 0):
            print(dialog.name)
            groups.append(dialog.id)
    print(groups)
    for group in groups:
        time.sleep(1)
        try:
            await client3237391651.send_file(group, 'pic3.jpg')
            print("CLIENT 14 message sent to group" + str(group))

        except Exception as er:
            print(er)


def execute():
    with client7783209995:
        client7783209995.loop.run_until_complete(main6())
    with client7168156028:
        client7168156028.loop.run_until_complete(main5())
    with client6048617357:
        client6048617357.loop.run_until_complete(main4())
    with client7373203283:
        client7373203283.loop.run_until_complete(main13())
    with client3237391651:
        client3237391651.loop.run_until_complete(main14())


scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(3600, 1, execute)
scheduler.run()
# 4  604 861 7357
# 5  716 815 6028
# 6  778 320 9995
# 9  716 815 6028
# 10 213 486 3565
# 11 616 314 2053
# 12 702 605 8825
# 13 737 320 3283
# 14 323 739 1651

# 1  778 788 0215
# 2  236 877 4531
# 3  617 469 3954
# 4  604 861 7357
# 5  716 815 6028
# 6  778 320 9995
# 7  605 846 9310
# 8  276 258 9713
# 9  716 815 6028
# 10 213 486 3565
# 11 616 314 2053
# 12 702 605 8825
# 13 737 320 3283
# 14 323 739 1651
