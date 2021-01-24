# MotorModelView

Uma série de classes que ajudam a escrever view baseadas em classes de forma mais facil para projetos com Tornado + MongoDB.

#### Using Motor Model class

Utilize a classe MotorModel, essa classe herda do Model do schematics.

```
from contrib.base.models import MotorModel
from contrib.base.fields import StringType
class Person(MotorModel):
    name = StringType()
    class Meta:
        collection_name = 'persons'
```


# Model Manager


# ModelView

