from typing import List

import openai


class ChatMessage:
    """Базовый класс для сообщений в чате."""
    def __init__(self, content: str, role: str):
        self.content = content
        self.role = role

    @property
    def as_dict(self):
        """Возвращает представление сообщения в виде словаря."""
        return {"role": self.role, "content": self.content}


class SystemMessage(ChatMessage):
    """Класс для системных сообщений."""
    def __init__(self, content: str):
        super().__init__(content, "system")


class AssistantMessage(ChatMessage):
    """Класс для сообщений, отправляемых помощником."""
    def __init__(self, content: str):
        super().__init__(content, "assistant")


class UserMessage(ChatMessage):
    """Класс для сообщений, отправляемых пользователем."""
    def __init__(self, content: str):
        super().__init__(content, "user")


class ChatClient:
    """Класс для взаимодействия с API ChatGPT."""
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo",
                 history_max_depth: int = 100):
        self.api_key = api_key
        self.model = model
        self.history_max_depth = history_max_depth
        self.history: List[ChatMessage] = []
        openai.api_key = self.api_key

    def add_to_history(self, message: ChatMessage):
        """Добавляет сообщение в историю."""
        if len(self.history) >= self.history_max_depth:
            self.history = self.history[1:]
        self.history.append(message)

    def send(self, prompt: str) -> str:
        """Отправляет сообщение в ChatGPT, и возвращает ответ."""
        self.add_to_history(UserMessage(prompt))
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[message.as_dict for message in self.history],
            temperature=0.7,
            max_tokens=1000
        )
        response_text = response.choices[0].message.content
        self.add_to_history(AssistantMessage(response_text))
        return response_text


class InvalidChatMessage(Exception):
    """Исключение для некорректного сообщения."""
    pass
