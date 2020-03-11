# profi-ru_updater
The main goal of this script is to save some time on checking profi.ru and trying to find relevant request.

Script logs in to profi.ru account using selenium, gets all page requests and checks if there is needed key words.
When key word is foind - emails is sent.
It should run constuntly to update info every minute and send new emails to you.

Основная цель скрипта - сокращение времение на постоянное обновление профи.ру с целью найти интересный заказ.

Скрипт логинится в ваш аккаунт используя модуль selenuim, считывает страницу и ищет среди заказов нужные ключевые слова
Когда ключевое слово найдено - отправляется письмо.
Скрипт должен работать непрерывно, обновляя каждую минуту страницу и отправляя новое письмо, если появляется новый заказ.
