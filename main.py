import os

from chat_client import ChatClient, InvalidChatMessage


def main():
    """Основная функция."""
    api_key = os.getenv('OPENAI_API_KEY', 'OPENAI_API_KEY')
    client = ChatClient(api_key)

    while True:
        prompt = input("Введите ваш запрос: ")
        if prompt.strip() == "exit":
            break
        try:
            response = client.send(prompt)
            print(f"\nОтвет: {response}")
        except InvalidChatMessage as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
