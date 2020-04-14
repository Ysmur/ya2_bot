'''
запрос статистики со стены сообщества с id = 17916162, метод stats_get(group_id, fields=reach)
'''
import vk_api
import datetime
from auth_data import VK_USER, VK_PASS
group_id = 157099657 #102417094

def main():
    login, password = VK_USER, VK_PASS
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()

    response = vk.stats.get(group_id=group_id, fields="reach")

    if response:
        for item in response[:1]:
            value = datetime.datetime.fromtimestamp(item['period_from'])
            print(value.strftime('%Y-%m-%d'))
            print(item['activity'])
            print(item['reach'])


if __name__ == '__main__':
    main()
