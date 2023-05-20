pip install requests

# For pip3:
pip3 install requests


import requests



class YaUploader:
    def __init__(self, _token: str):
        self.token = _token

    def upload(self, file_path):
        """Метод загружает файл file_path на Яндекс.Диск"""
        upload_url = "https://disk.yandex.ru/client/disk/test"
        filename = file_path.split('/', )[-1]
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": f"Загрузки/{filename}", "overwrite": "true"}
        _response = requests.get(upload_url, headers=headers, params=params).json()
        href = _response.get("href", "")
        responce = requests.put(href, data=open(file_path, 'rb'))
        responce.raise_for_status()
        if responce.status_code == 201:
            return 'Успешно'
        else:
            return f"Ошибка загрузки! Код ошибки: {responce.status_code}"


if __name__ == '__main__':
    path_to_file = r'C:\Users\benin\Desktop\яндекс диск\new file.txt'   # ЗДесь пишем путь к файлу!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    token = 'y0_AgAAAAAC1YjnAADLWwAAAADjm9Sx-IAqMjGXQJGmH89UvCU07jPVPiQ'  #  Здесь Вводим номер ТОКЕНА!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    uploader = YaUploader(token)
    # Загружаем файл на диск
    print(f"Загружаем файл {path_to_file.split('/', )[-1]} на Яндекс.Диск")
    result = uploader.upload(path_to_file)
    print(result)