import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логикаh
        # Функция может ничего не возвращать
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Authorization': 'OAuth ' + token}
        params = {'path': '/fotosintes.jpg'}
        resp = requests.get(url, headers=headers, params = params).json()
        #print(resp)
        url1 = resp['href']
        with open(file_path, 'rb') as f:
            resp2 = requests.put(url1, files={'file': f}, headers=headers, params = params)
        #return resp2.status_code

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "C:\\Margarita\\fotosintes.jpg"
    token = open("token").read()
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)