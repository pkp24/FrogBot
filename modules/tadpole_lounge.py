# modules/tadpole_lounge.py

from datetime import datetime, timedelta
import disnake  # Use `import discord` if you are using discord.py

async def add_role(member, role, channel):
    try:
        await member.add_roles(role)
        await channel.send(f"Hello {member.mention}, welcome to {member.guild.name}! You have been assigned the {role.mention} role. Please read the rules and enjoy your stay! You will gain full server access in a little while.")
    except Exception as e:
        print(f"Error adding role {role.name} to member {member.name}: {e}")

async def on_member_join(member):
    try:
        role = disnake.utils.get(member.guild.roles, name="tadpole")  # Use `discord.utils.get` for discord.py
        channel = disnake.utils.get(member.guild.channels, name="tadpole-lounge")  # Same as above
        if datetime.utcnow() - member.created_at < timedelta(days=2):
            await add_role(member, role, channel)
    except Exception as e:
        print(f"Error in on_member_join: {e}")

def setup(bot):
    bot.add_listener(on_member_join, "on_member_join")