.. tornado_contrib documentation master file, created by
   sphinx-quickstart on Mon Feb  8 08:37:25 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to tornado_contrib's documentation!
===========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



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

Criando o ModelView
===================

Criando o modelview

Utilizando com Tornado
======================

Exemplos