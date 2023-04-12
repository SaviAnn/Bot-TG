# Телеграм-бот для транслитерации ФИО с кириллицы на латиницу


Что нужно сделать, чтобы все работало:

1) Скачайте все файлы из текущего репозитория
2) Убедитесь, что у Вас установлен **docker**
3) Откройте файл **dockerfile** и замените в строке `TOKEN='your token'` на токен своего тг-бота (если у Вас его нет, попросите у BotFather, 
но не забывайте делать это с уважением)
4) Запустите **docker** 
5) Введите `docker build .` в терминале
6) С помощью команды 'doker images' выберите из списка самый свежий image ID
7) Запустите бот посредством команды  `docker run -d -p 80:80 {номер image ID}`
9) Наслаждайтесь работой бота, а если ваше имя или фамилия латиницей получились длиной больше, чем на 2 символа, считайте, что выиграли бинго!
10) Не забывайте о золотом правиле "уходя гасите свет" и отключите бота в два шага: после запуска `docker ps` Вы увидите container ID. 
Его нужно добавить в строку `docker stop {container ID}`

* все команды вводите в строку терминала без кавычек
