from icecream import ic
ic.configureOutput(includeContext=True)
ic.configureOutput(prefix="ВЫВОДИМ СЛОВАРЬ:")
print = ic
import random as rnd


def createRndData():
    result = {}
    namesMale = ["Иван", "Петр", "Александр", "Алексей"]
    namesFemale = ["Кристина", "Екатерина", "Мария", "Дарья"]
    hobbies = ["Футбол", "Чтение книг", "Спортивная ходьба", "Стрельба из лука", "Плавание", "Поэзия"]
    cities = ["Москва", "Владивосток", "Воронеж", "Сочи", "Архангельск", "Анапа", "Мурманск", "Магнитогорск"]
    for name in namesMale:
        result[name] = {"возраст": rnd.randint(20, 60),
                          "хобби": rnd.choice(hobbies),
                          "пол": "М",
                          "город":rnd.choice(cities),
                          "любимое число": rnd.randint(1, 100)}
    for name in namesFemale:
        result[name] = {"возраст": rnd.randint(20, 60),
                        "хобби": rnd.choice(hobbies),
                        "пол": "Ж",
                        "город":rnd.choice(cities),
                        "любимое число": rnd.randint(1, 100)}
        print(result)


createRndData()