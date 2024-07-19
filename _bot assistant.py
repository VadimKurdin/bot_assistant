import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='@', description=description, intents=intents)


litter=['Помёт', 20]
food=['Пища', 21]
n_clothes=['Натур_одежда', 364]
books=['Книги', 728]
dice=['Кости', 2366]
firewood=['Дрова', 2912]
iron_jars=['Железные_банки', 3640]
s_clothes=['Синтетическая_одежда', 12775]
tin_cans=['жестиные_банки', 32850]
foil=['Фольга', 36400]
plastic=['Пластик', 36400]
rubber=['Резина', 36400]
tires=['Покрышки', 47320]
polyethelene=['Полиэтилен', 54600]
sponges=['Губка', 72800]
diapers=['Подгузник', 182000]
aluminum_containers=['Алюминиевые_контейнеры', 182000]
glass=['Стекло', 364000]
objects=[litter, food, n_clothes, books, dice, firewood, iron_jars, s_clothes, tin_cans, foil, plastic, rubber, tires, polyethelene, sponges, diapers, aluminum_containers, glass]

@bot.command()
async def rastvor(ctx, left: int, right: int):
    for i in range(len(objects)):
        stroge_duration='ОБЪЕКТ НЕ НАЙДЕН'
        num_name=''
        years=0
        month=0
        week=0
        if objects[i][1]>=left and objects[i][1]<=right:
            if objects[i][1]>=364:
                stroge_duration=int(objects[i][1]/364)
                years=int(objects[i][1]/364)
                month=int(objects[i][1]/30)
                week=int(objects[i][1]/7)
                num_name=' years'
            elif objects[i][1]>=30:
                stroge_duration=int(objects[i][1]/30)
                years=int(objects[i][1]/364)
                month=int(objects[i][1]/30)
                week=int(objects[i][1]/7)
                num_name=' month'
            elif objects[i][1]>=7:
                stroge_duration=int(objects[i][1]/7)
                years=int(objects[i][1]/364)
                month=int(objects[i][1]/30)
                week=int(objects[i][1]/7)
                num_name=' week'
            
            await ctx.send(objects[i][0]+'- '+str(stroge_duration)+num_name)
            await ctx.send(objects[i][0]+'- '+str(years)+'г'+'/'+str(month)+'м'+'/'+str(week)+'н'+'/'+str(objects[i][1])+'д')
            await ctx.send('_______________')
    await ctx.send('[Сроки разложения вещей может отличаться в зависимости от природных условий и других факторов]')
