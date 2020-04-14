'''
пример загрузки изображения и создания сообщения с ним на стену
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
    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo_wall(['1-1.jpg']
                              )

    vk_photo_id = f"photo{photo[0]['owner_id']}_{photo[0]['id']}"

    print(photo, vk_photo_id, sep="\n")
    vk = vk_session.get_api()
    vk.wall.post(message="Test", attachments=[vk_photo_id])




if __name__ == '__main__':
    main()
