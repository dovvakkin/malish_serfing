from threading import Thread

from Main import bot_life
from db_manager import get_bot, amount_of_bots

VK_LOGIN = '89258396534'
VK_PASSWORD = 'k0zhepnin@'

log = '89104696981'
pas = 'cherep/'

i = 1
amount = amount_of_bots()
while i <= amount:
    bot = get_bot(i)
    Thread(target=bot_life, args=(bot[1], bot[2])).start()
    i += 1

