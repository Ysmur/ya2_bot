import vk_api
import datetime


def main():
    login, password = 'valenka82@mail.ru', '15KYt247'
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    # Используем метод wall.get
    response = vk.wall.get(count=5, offset=0)
    if response['items']:
        for i in response['items']:
            value = datetime.datetime.fromtimestamp(i['date'])
            print(value.strftime('%Y-%m-%d'))
            print(i['text'])


if __name__ == '__main__':
    main()