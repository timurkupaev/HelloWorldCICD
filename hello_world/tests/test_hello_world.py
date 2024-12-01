import sys
import os

# Добавляем путь к папке src в sys.path, чтобы Python мог найти модули
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Теперь Python может найти модуль hello_world
from hello_world.src.hello_world import hello

def test_hello():
    assert hello() == "Hello, World!"
