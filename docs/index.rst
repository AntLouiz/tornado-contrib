.. tornado_contrib documentation master file, created by
   sphinx-quickstart on Mon Feb  8 08:37:25 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to tornado_contrib's documentation!
===========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


modules


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


User's Guide
============

* Introduction
* Installation
* Quickstart


Criando o Model
===============
.. _schematics.modes.Model: https://schematics.readthedocs.io/en/latest/usage/models.html
.. _schematics.models.BaseType: https://schematics.readthedocs.io/en/latest/usage/models.html
.. _Types: https://schematics.readthedocs.io/en/latest/usage/types.html
.. _`schematics.models.ModelType`: https://schematics.readthedocs.io/en/latest/usage/models.html
.. _`MotorCollection`: https://schematics.readthedocs.io/en/latest/usage/models.html
.. _`ModelManager`: https://schematics.readthedocs.io/en/latest/usage/models.html
.. _`MotorDatabase`: https://schematics.readthedocs.io/en/latest/usage/models.html
.. _`ModelAPIView`: https://schematics.readthedocs.io/en/latest/usage/models.html
.. _`MotorModel`: https://schematics.readthedocs.io/en/latest/usage/models.html
.. _`Paginator`: https://schematics.readthedocs.io/en/latest/usage/models.html
.. _`BaseAuthentication`: https://schematics.readthedocs.io/en/latest/usage/models.html
.. _`BasePermission`: https://schematics.readthedocs.io/en/latest/usage/models.html
.. _`Schematics roles`: https://schematics.readthedocs.io/en/latest/usage/models.html

Para criar um model utilize a classe MotorModel.
    * Todos os models tem como base de herança o `schematics.modes.Model`_.
    * Cada attributo constitui de um campo no banco de dados.
    * A classe interna **Meta** informa qual collection este modelo pertence.

Quick Example
-------------

O código abaixo mostra um exemplo de modelo utilizando o **MotorModel**.

.. code-block:: python

    from contrib.base.models import MotorModel

    class Person(MotorModel):
        first_name = StringType()
        last_name = StringType()

        class Meta:
            collection = 'persons'

**first_name** e **last_name** são campos do modelo, já a classe interna **Meta** é responsável por informar
qual collection do banco de dados será preenchida com os dados do modelo.

O modelo **Person** acima criará um documento da forma abaixo:

.. code-block::

    {"first_name": "", "last_name": ""}


Fields
------

Os campos utilizam as classes que herdam de `schematics.models.BaseType`_.
Tome cautela para não criar campos que conflitam com o nome do objeto **manager** do Model.


Example:

.. code-block:: python

    from contrib.base.models import MotorModel
    from contrib.base import fields

    class Musician(MotorModel):
        _id = fields.ObjectId()
        first_name = fields.StringType(max_length=50)
        last_name = fields.StringType(max_length=50)
        instrument = fields.StringType(max_length=100)
        age = fields.IntType()

    class Album(MotorModel):
        _id = fields.ObjectId()
        artist = fields.ModelType(Musician)
        name = fields.StringType(max_length=100)
        release_date = fields.DateType()
        num_stars = fields.IntegerType()


Fields Types
------------

Cada campo no modelo deve ser uma instância de `schematics.models.BaseType`_.
Para mais detalhes sobre os tipos de campos e seus argumentos visite `Types`_.


Relationships
-------------

Many-to-one relationships
^^^^^^^^^^^^^^^^^^^^^^^^^

Para definir uma relação de many-to-one utilize o campo `schematics.models.ModelType`_.

Este campo precisa de um **MotorModel** como argumento obrigatório para fazer o relacionamento.

Por exemplo, se um **Order** tem um **User**, quer dizer que um usuário pode fazer vários
pedidos mas cada pedido só pode ter um **User**, verifique o exemplo abaixo:

.. code-block:: python
    :emphasize-lines: 8

    from contrib.base.models import MotorModel

    class User(MotorModel):
        username = fields.StringType()

    class Order(MotorModel):
        price = fields.IntegerType()
        user = fields.ModelType(User)

O doumento **Order** ficará dessa forma:

.. code-block:: python

    {"user": {"username": "John"}, "price": 1200}

Many-to-many relationships
^^^^^^^^^^^^^^^^^^^^^^^^^^

Para definir relações many-to-many é necessário fazer a junção de dois campos. No MongoDB relações
many-to-many são constituidos de listas de documentos.

Por exemplo, se uma **Pizza** contém multiplos documentos **Topping**, assim um documento **Topping**
pode está em diversas pizzas e cada **Pizza** pode conter diversos **Topping**, abaixo mostra como
representamos isso:

.. code-block:: python

    from contrib.base.models import MotorModel
    from contrib.base import fields

    class Topping(MotorModel):
        name = fields.StringType()

    class Pizza(MotorModel):
        toppings = fields.ListType(ModelType(Topping))

O resultado desse relacionamento criará um documento dessa forma:

.. code-block:: python

    {"pizza": [{"name": "Hot sauce"}, {"name": "Tomato sauce"}]}


Classe interna **Meta**
-----------------------

Esta classe é obrigatória no momento da construção do model, pois adiciona metadados para que
se possa definir qual collection o model irá lidar. O campo **collection_name** é responsável
por informar a descrição da collection do model no banco de dados MongodBD.

Example:

.. code-block:: python
    :emphasize-lines: 7,8

    from contrib.base.models import MotorModel
    from contrib.base import fields

    class Car(MotorModel):
        name = fields.StringType()

        class Meta:
            collection_name = 'cars'


Attributos do **Model**
-----------------------

**manager**
^^^^^^^^^^^

O atributo mais importante do model é o `ModelManager`_. O manager é uma interface responsável
por fazer as operações de banco de dados.


**collection**
^^^^^^^^^^^^^^

Um objeto `MotorCollection`_.


Parâmetros do **Model**
-----------------------

O model necessita como parâmetro obrigatório uma instância de um `MotorDatabase`_ para que
seja possível a comunicação com o banco de dados.

Como geralmente os models são utilizados dentro de handlers, de acordo com a utilização
do Motor com o Tornado, faça da seguinte forma:

.. code-block:: python
    :emphasize-lines: 9,10

    class Car(MotorModel):
        name = fields.StringType()

        class Meta:
            collection_name = 'cars'

    class CarsHandler(tornado.web.RequestHandler):
        def get(self):
            db = self.settings['db']
            model = Car(db)



Criando o ModelAPIView
======================


Esta biblioteca possibilita a criação de API's REST baseados em classes, utilizando modelos definidos
com a classe `MotorModel`_.

Todas os handlers, herdam da classe `ModelAPIView`_, todas as requisições são roteadas
para os seus respectivos métodos, por exemplo, uma requisição do tipo POST, será roteada para o método
**.post()**.

O método HTTP GET se divide em dois métodos, o **.list()** e o **.retrieve()**.
O método **.list()** faz uma listagem paginada de todos os dados no banco, já o retrieve
recebe como argumento o id do objeto para a pesquisa no banco de dados.

Os handlers `ModelAPIView`_ recebem um importante attributo denomidado **model**.

Por exemplo:

.. code-block:: python

    from contrib.handlers import ModelAPIView

    class PersonAPIHandler(ModelAPIView):
        model = Person

O ModelAPIView já implementa todos os métodos de uma API REST, tornando muito mais rápido e fácil
criar endpoints de um modelo.
Para customizar algum método por exemplo, o método de listagem, faça o seguinte:

.. code-block:: python

    from contrib.handlers import ModelAPIView

    class PersonAPIHandler(ModelAPIView):
        model = Person

        def list(self, *args, **kwargs):
            queryset = await self.get_queryset()
            response = self.process_response(queryset)
            response = self.paginate_response(queryset)
            return response


Attributos do ModelAPIView
--------------------------

.model
^^^^^^
É um atributo que informa qual o modelo que essa view está manipulando, para que
possa fazer a serialização e queries no banco de dados.

.lookup_field
^^^^^^^^^^^^^

É um atributo que informa qual a campo do modelo o manager irá buscar no banco de dados como chave de busca,
por padrão o campo é o **_id**.

.lookup_url_kwarg
^^^^^^^^^^^^^^^^^

É um atributo que informa o nome do argumento que será roteado da url para os métodos da view.
Por padrão o campo é o **id**.

.page_size
^^^^^^^^^^
É um atributo que informa qual a quantidades de objetos que o método de paginação irá paginar. Por
padrão a quantidade é de 50 objetos.

.pagination_class
^^^^^^^^^^^^^^^^^

É um atributo que informa a classe de Paginação, todas as classes de paginação devem herdar de `Paginator`_.


.authentication_class
^^^^^^^^^^^^^^^^^^^^^

É um atributo que informa a classe de autenticação, todas as classes de autenticação devem herdar de `BaseAuthentication`_.

.permissions_classes
^^^^^^^^^^^^^^^^^^^^

É um atributo que informa a classe de permissões, todas as classes de permissões devem herdar de `BasePermission`_.

.search_fields
^^^^^^^^^^^^^^

É um atributo que informa quais campos serão adicionados na query de pesquisa geral, comumente utilizado com o query parameter
**?search=**.

.view_role
^^^^^^^^^^

É um atributo que informa qual a role que os modelos serão serializados, para mais informações de roles, visite `Schematics roles`_


Métodos do ModelAPIView
-----------------------

**pass**


Utilizando com Tornado
======================

**pass**