'''
получим пять сообщений со стены сообщества с id = 84297351, начиная с первого, то есть обратимся к методу wall.get API
'''
import vk_api
import datetime
from auth_data import VK_USER, VK_PASS

def main():
    login, password = VK_USER, VK_PASS
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    # Используем метод wall.get
    response = vk.wall.get(count=5, offset=0, owner_id=-84297351)
    if response['items']:
        for i in response['items']:
            value = datetime.datetime.fromtimestamp(i['date'])
            print(value.strftime('%Y-%m-%d'))
            print(i['text'])


if __name__ == '__main__':
    main()
