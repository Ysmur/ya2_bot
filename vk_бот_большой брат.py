import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from auth_data import VK_TOKEN, VK_club


def main():
    vk_session = vk_api.VkApi(
        token=VK_TOKEN)

    longpoll = VkBotLongPoll(vk_session, VK_club)
    print('999')
    for event in longpoll.listen():
        print(event)

        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            vk = vk_session.get_api()
            name = vk.users.get(user_id=event.obj.message['from_id'])[0]['first_name']
            try:
                city = vk.users.get(user_id=event.obj.message['from_id'], fields=['city'])[0]['city']['title']
            except Exception:
                city = ''

            if not city:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Привет, {name}",
                                 random_id=random.randint(0, 2 ** 64))
            else:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Привет, {name}\nКак поживает {city}?",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()