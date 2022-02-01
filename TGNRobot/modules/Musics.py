from pyrogram import filters
from TGNRobot import pbot as bot, musicbot
import pytgcalls

calls = pytgcalls.GroupCallFactory(musicbot).get_group_call()


@bot.on_message(filters.command('play'))
async def play(_, message):
    try:
        await musicbot.start()
    except:
        pass
    reply = message.reply_to_message
    if reply:
        fk = await message.reply('Downloading....')
        path = await reply.download()
        await calls.join(message.chat.id)
        await calls.start_audio(path, repeat=False)
        await fk.edit('playing...')


@bot.on_message(filters.command('vplay'))
async def vplay(_, message):
    try:
        await musicbot.start()
    except:
        pass
    reply = message.reply_to_message
    if reply:
        path = await reply.download()
        await calls.join(message.chat.id)
        await calls.start_video(path, repeat=False)
        await fk.edit('playing...')


@bot.on_message(filters.command('end'))
async def leavevc(_, message):
    await calls.stop()
    await calls.leave_current_group_call()


@bot.on_message(filters.command('pause'))
async def pause(_, message):
    await calls.pause_stream()

@bot.on_message(filters.command('resume'))
async def resume(_, message):
    await calls.resume_stream()
