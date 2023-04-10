# Comics publisher

Документация на английском здесь <a href='README_EN.md'>EN</a>

Автоматизированная загрузка в паблик ВК случайно скачанного комикса

## Публикация комиксов

Скрипт публикует в VK случайные комиксы, скачивая их с этого [сайта](https://xkcd.com/).
После завершения программы в Вашей группе появится случайный коммикс с смешной подписью.

### Как установить

1. Python3 должен быть уже установлен.

2. Клонируйте данный репозиторий и перейдите с директорию с проектом

```
    git clone https://github.com/wezbicka/Comics-publisher.git
```

3. Создайте и активируйте виртуальное окружение

```Bash
    python -m venv venv
    source ./venv/Scripts/activate  #для Windows
    source ./venv/bin/activate      #для Linux и macOS
```

4. Установите требуемые зависимости

```
    pip install -r requirements.txt
```

5. Создайте приложение в VK ([ссылка](https://vk.com/apps?act=manage)) и получите его ID. Затем получите [access_token](https://vk.com/dev/implicit_flow_user) со следующими правами: `photos, groups, wall, offline`. Также создайте своё сообщество в VK и [узнайте его ID](https://regvk.com/id/).

6. Cоздайте файл с названием .env и добавьте всё, что Вы получили выше. Вот пример:

```
    CLIENT_ID=0000000
    GROUP_ID=0000001
    VK_TOKEN=vk1.a.vk_access_token
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
