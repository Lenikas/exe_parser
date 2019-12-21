Задача - разбор формата exe

Автор - Сагалов Леонид

Запуск:
- python main.py -dos "path\to\file.exe" (поля DOS заголовка)
- python main.py -сoff "path\to\file.exe" (поля COFF заголовка)
- python main.py -standart_coff "path\to\file.exe" (поля STANDART COFF FIELDS заголовка)
- python main.py -windows_spec "path\to\file.exe" (поля WINDOWS SPECIFIC FIELDS заголовка)
- python main.py -all_headers "path\to\file.exe" (поля всех доступных заголовков)

Есть тестовый файл в директории с проектом, можно запустить через python main.py -dos test_file.exe