# test_assignment_only_digital

Автотест написан на Python c использованием фреймворков pytest, selenium и библиотеки requests и проверяет:
- Доступность сайта (200)
- Наличие футера
- Наличие телефона +7 в футере
- Наличие ссылок на соцсети в футере

Запуск:
pip install selenium webdriver-manager pytest requests
pytest test_only_digital.py -v
