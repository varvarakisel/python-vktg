from vk.api import longpoll
from vk.events import events_handler

def main():
    for events in longpoll.listen():
        events_handler(events)

if __name__ == '__main__':
    main()