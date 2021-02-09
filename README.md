# Tornado Motor ModelView

Uma série de classes que ajudam a escrever API's utilizando views baseadas em classes  para projetos com Tornado + MongoDB.

## Hello, world
-------------------------------------------------------

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

Documentação e links de recursos adicionais estão disponíveis em [not defined yet]().