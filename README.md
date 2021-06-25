# foodgram 
foodgram
 
![Readme](https://github.com/pyp18/foodgram-project/actions/workflows/main.yml/badge.svg) 
 
Данный проект является прототипом социальной сети состоящий из: базы данных postgresSQL(12.4), сервера ngnix(1.19.3) и самой социальной сети написанной на Django(3.0.5). Все это уже настроено и собрано в трех образах и объединено в файле docler-compose.yaml, Вам останется лишь завершить настройку для своего устройства.  

Для запуска данного проекта вам потребуется настроить сервер и установить на него все необходимые компоненты.


Настройка сервера
1) Создайте виртуальную машину, для данного проекта использовалась ВМ из яндекс облака https://console.cloud.yandex.ru/.
2) Подключился к серву ssh ЛОГИН@IP
3) Сохраните fingerprint
4) Выполните команду sudo apt update 
5) Выполните команду sudo apt upgrade -y 
6) Выполните команду sudo apt install python3-pip python3-venv git -y 

После того как сервер будет настроен вам понадобится установить на него Docker

Настройка докера
1) Выполните команду sudo apt-get update
2) Выполните команду sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
3) Выполните команду curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
4) Выполните команду echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
5) Выполните команду sudo apt-get update
6) Выполните команду sudo apt-get install docker-ce docker-ce-cli containerd.io
7) Выполните команду sudo docker run hello-world
Докер установлен

После установки докера выполните дополнительные команды для настройки окружения.

Post Install Docker
1) Выполните команду sudo groupadd docker - groupadd: group 'docker' already exists
2) Выполните команду sudo usermod -aG docker $USER
3) Выполните команду sudo usermod -aG docker $pyp18
4) Выполните команду docker run hello-world

Так же потребуется установить Docker-compose на сервер

Установка docker-compose up на сервер
1) Выполните команду sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
2) Выполните команду sudo chmod +x /usr/local/bin/docker-compose


Последние шаги.
Эти файлы нужно создать на сервере.
1) Создайте файл default.conf (скопируйте содержимое из репозитория) для nginx и пропишите к нему путь в docker-compose.yml
2) Создайте файл docker-compose.yml (скопируйте содержимое из репозитория)
2) Создате файл .env 

Вставьте в него данные:

DEBUG=TRUE
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД 


Команды для запуска проекта:  
  
1) Когда Вы будете запускать эту программу первый раз, для сборки используйте команду "docker-compose up -d".  
  
Когда сервер будет запущен перейдите к следующему пункту.  
  
2) После этого нужно будет провести миграции, нахожясь на сервере укажите название приложения явно "docker-compose exec web python manage.py makemigrations 'название приложения' "  
  
3) "docker-compose exec web python manage.py migrate --noinput"  
  
4) Создайте суперпользователя "docker-compose exec web python manage.py createsuperuser"  
  
5) Соберите статику "docker-compose exec web python manage.py collectstatic --no-input"  
