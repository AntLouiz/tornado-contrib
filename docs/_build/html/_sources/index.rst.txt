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
------------------

* Introduction
* Installation
* Quickstart

-------------------
Criando o Model
-------------------
    .. _schematics.modes.Model: https://schematics.readthedocs.io/en/latest/usage/models.html

    Para criar um model utilize a classe MotorModel.
        * Todos os models tem como base de herança o `schematics.modes.Model`_.
        * Cada attributo constitui de um campo no banco de dados.
        * A classe interna **Meta** informa qual collection este modelo pertence.

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

        db.persons.insertOne({"first_name": "", "last_name": ""})


-------------------
Criando o ModelView
-------------------

----------------------
Utilizando com Tornado
----------------------