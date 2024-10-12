# program.py

from app.ai.ai_request import AIRequest  # Предполагается, что класс AIAnalysis находится в файле ai_analysis.py


def main():
    # Инициализация AIAnalysis
    ai = AIRequest("./models/")  # Если модель находится не в текущей директории, укажите путь: AIAnalysis("path/to/model")
    
    # Чтение запроса из файла
    with open("ai/promts/request_groups.txt", "r", encoding="utf-8") as file:
        request = file.read().strip()

    print("Запрос:")
    print(request)
    print("\nОбработка запроса...\n")

    # Вызов метода analyze
    result = ai.analyze(request)

    print("\nРезультат анализа:")
    print(result)


if __name__ == "__main__":
    main()