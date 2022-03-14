from vk_api import VkApi 
from vk_api.bot_longpoll import VkBotLongPoll
import settings

connection = VkApi(token=settings.VK_API_KEY)
print (connection._check_token())
api = connection.get_api()
longpoll = VkBotLongPoll(api, settings.GROUP_ID)
