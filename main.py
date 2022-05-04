import discord
import datetime
from discord.ext import commands
import json
from lib.embed import lang_embed
bot = commands.Bot(command_prefix='dp?',
                   help_command=None,
                   allowed_mentions=discord.AllowedMentions(everyone=True, users=True, roles=True, replied_user=True))
@bot.command(aliases=["lang"])
async def lang_change(ctx,lang):
    """
    Botの言語を変える
    例:
    dp?lang 1
    """
    if lang == "1":
        guild_id == ctx.guild.id
        with open(f'bot_data/guild/{guild_id}.json', mode='w') as f:
            df = json.load(f)
            data = {
                    "guild_Id": guild_id,
                    "version": "0.1.0",
                    "date_written": datetime.datetime.now(),
                    "guild_lang_Id": 1
                    }
            json.dump(data,df,indent=2)
            await ctx.send(embed=lang_embed("Language has been changed.","Changed from Japanese to English."))
    elif lang == "0":
        guild_id == ctx.guild.id
        with open(f'bot_data/guild/{guild_id}.json', mode='w') as f:
            df = json.load(f)
            data = {
                    "guild_Id": guild_id,
                    "version": "0.1.0",
                    "date_written": datetime.datetime.now(),
                    "guild_lang_Id": 1
                    }
            json.dump(data,df,indent=2)
        await ctx.send(embed=lang_embed("言語が変更されました。","英語から日本語に変更されました。"))