import os
import unittest
from unittest.mock import MagicMock, patch

from chat_client import ChatClient, ChatMessage, SystemMessage, UserMessage


class TestChatClient(unittest.TestCase):
    def setUp(self):
        """Настройка тестовой среды перед каждым тестом."""
        self.api_key = os.getenv('OPENAI_API_KEY', 'OPENAI_API_KEY')
        self.client = ChatClient(api_key=self.api_key)

    @patch("openai.ChatCompletion.create")
    def test_send_message(self, mock_create):
        """Проверка отправки сообщения и получения ответа."""
        mock_create.return_value = MagicMock(
            choices=[
                MagicMock(message=MagicMock(content="Тестовый ответ"))
            ]
        )
        prompt = "Тестовый запрос"
        expected_response = "Тестовый ответ"
        response = self.client.send(prompt)
        self.assertEqual(response, expected_response)

    @patch("openai.ChatCompletion.create")
    def test_send_message_with_history(self, mock_create):
        """Проверка отправки сообщения с историей."""
        mock_create.return_value = MagicMock(
            choices=[
                MagicMock(message=MagicMock(
                    content="Тестовый ответ с историей"))
            ]
        )
        self.client.add_to_history(SystemMessage(
            "Тестовое системное сообщение"))
        self.client.add_to_history(UserMessage(
            "Тестовый запрос с историей"))
        prompt = "Дополнительный тестовый запрос"
        expected_response = "Тестовый ответ с историей"
        response = self.client.send(prompt)
        self.assertEqual(response, expected_response)

    def test_add_to_history(self):
        """Проверка добавления сообщений в историю."""
        system_message = SystemMessage("Тестовое системное сообщение")
        user_message = UserMessage("Тестовый запрос")
        self.client.add_to_history(system_message)
        self.client.add_to_history(user_message)
        self.assertIn(system_message, self.client.history)
        self.assertIn(user_message, self.client.history)

    def test_add_to_history_with_limit(self):
        """Проверка ограничения истории."""
        self.client.history_max_depth = 2
        system_message = SystemMessage("Тестовое системное сообщение 1")
        user_message = UserMessage("Тестовый запрос 1")
        self.client.add_to_history(system_message)
        self.client.add_to_history(user_message)
        self.client.add_to_history(SystemMessage(
            "Тестовое системное сообщение 2"))
        self.client.add_to_history(UserMessage("Тестовый запрос 2"))
        self.assertNotIn(system_message, self.client.history)
        self.assertIn(user_message, self.client.history)

    def test_chat_message_as_dict(self):
        """Проверка преобразования сообщения в словарь."""
        message = ChatMessage("Тестовое сообщение", "user")
        expected_dict = {"role": "user", "content": "Тестовое сообщение"}
        self.assertEqual(message.as_dict, expected_dict)


if __name__ == "__main__":
    unittest.main()
