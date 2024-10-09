# Console-Application
Test Case.
Консольное приложение на языке программирования Python, которое позволяет 
пользователю вводить произвольные запросы в консоль, отправлять их в нейронную сеть 
(например, ChatGPT) и выводить полученные ответы обратно в консоль.
# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/goldenlion52rus/Console-Application
cd Console-Application
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас Windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Создать API ключ:

```
Зарегистрируйтесь на сайте OpenAI.
Создайте API ключ и скопируйте его.
```

Заменить API ключ:

```
В файле .env в строке OPENAI_API_KEY вставьте ваш API ключ.
API ключи OpenAI нужно хранить в секрете, так как они дают доступ к вашей учетной записи OpenAI. 
Не рекомендуется публиковать API ключи в открытом доступе.
```

Запустите файл main.py:

```
python main.py
```
Как запустить тесты:

```
Запустите тесты в командной строке: python tests.py.

Если тесты пройдут успешно, вы увидите сообщение OK.
Если возникнут ошибки, вы получите описание ошибки и ее местоположение.
```
Над проектом работал: 
https://github.com/goldenlion52rus