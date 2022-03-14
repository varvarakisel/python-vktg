from vk_api.bot_longpoll import VkBotEvent, VkBotEventType


def events_handler(events: [VkBotEvent]):
    for event in events:
        if event.type == VkBotEventType.WALL_POST_NEW:
            print(event.raw)
