import sys
import os

# Указываем полный путь к директории вашего проекта
sys.path.insert(0, '/var/www/html/maxmontaj67')

# Добавляем путь к виртуальному окружению для использования его библиотек
virtual_env = '/var/www/html/maxmontaj67/maxmontaj67_env/lib/python3.12/site-packages'
sys.path.insert(0, virtual_env)

# Добавляем текущую директорию
sys.path.insert(0, os.path.dirname(__file__))

# Импортируем приложение
from app import app as application

