import discord
from discord.ext import commands
from lib.embed import lang_embed
bot = commands.Bot(command_prefix='dp?',
                   help_command=None,
                   allowed_mentions=discord.AllowedMentions(everyone=True, users=True, roles=True, replied_user=True))

@bot.command(aliases=["lang"])
async def lang_change(ctx,lang):
    """
    Botの言語を変える

    例

    dp?lang 1
    """
    if lang == "1":
        await ctx.send(embed=lang_embed("Language has been changed.","Changed from Japanese to English."))
    elif lang == "0":
        await ctx.send(embed=lang_embed("言語が変更されました。","英語から日本語に変更されました。"))