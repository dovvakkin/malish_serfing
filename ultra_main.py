from threading import Thread

from Main import bot_life

VK_LOGIN = '89258396534'
VK_PASSWORD = 'k0zhepnin@'

log = '89104696981'
pas = 'cherep/'

Thread(target=bot_life, args=(log, pas)).start()
Thread(target=bot_life, args=(VK_LOGIN, VK_PASSWORD)).start()
