import requests

if __name__ == '__main__':
    # выполняем POST-запрос на сервер по эндпоинту add с параметром json
    zipcode = int(input('Введите zipcode: '))
    sqft = float(input('Введите sqft: '))
    propertyType = (input('Введите тип объекта: '))
    lotsize = float(input('Введите площадь участка: '))
    stories = float(input('Введите этажность дома: '))
    schools_count = float(input('Введите количество школ возле дома: '))
    remodeling_yes = input('была ли реконструкция дома?: ')

    r = requests.post('http://localhost:5000/predict', json=[zipcode, sqft, propertyType,
                                                             lotsize, stories, schools_count, remodeling_yes])
    # выводим статус запроса
    print('Status code: {}'.format(r.status_code))
    # реализуем обработку результата
    if r.status_code == 200:
        # если запрос выполнен успешно (код обработки=200),
        # выводим результат на экран
        print('Prediction: {}'.format(r.json()['prediction']))
    else:
        # если запрос завершён с кодом, отличным от 200,
        # выводим содержимое ответа
        print(r.text)