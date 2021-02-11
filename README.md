# Tornado Motor ModelView

Uma série de classes que ajudam a escrever API's utilizando views baseadas em classes  para projetos com Tornado + MongoDB.

Este projeto é constitui principalmente das seguintes libs:
* [Tornado](https://github.com/tornadoweb/tornado): is a Python web framework and asynchronous networking library, originally developed at FriendFeed.
* [Motor](https://github.com/mongodb/motor): presents a coroutine-based API for non-blocking access to MongoDB.
* [Schematics](https://github.com/schematics/schematics): is a Python library to combine types into structures, validate them, and transform the shapes of your data based on simple descriptions.

## Hello, world

Aqui um simples "Hello, world" com o Tornado + Motor:

```python
import tornado.ioloop
import tornado.web
from contrib.base.models import MotorModel
from contrib.base.fields import StringType
from contrib.base.handlers import ModelAPIView

class Person(MotorModel):
    name = StringType()
    class Meta:
        collection_name = 'persons'

class PersonModelAPIView(ModelAPIView):
    model = Person

def make_app():
    return tornado.web.Application([
        (r"/persons/(?P<id>[0-9a-fA-F]{24})/", PersonModelAPIView),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```


# Documentation

Documentação e links de recursos adicionais estão disponíveis em [Documentation](https://tornado-contrib.readthedocs.io/en/docs/).