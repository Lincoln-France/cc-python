Usage
=====

Installation
------------

L'usage d'un template cookiecutter nécessite l'installation de l'utilitaire Cookiecutter_. 

Exemple pour linux (debian)

.. code-block:: bash

    $ python3 -m pip install --user cookiecutter
    $ cookiecutter --version
    Cookiecutter 1.7.2


Générer un projet
-----------------

L'utilitaire *cookiecutter* installé, pour générer un nouveau projet à partir du template *cc-python* de Lincoln:

1. se placer dans le repertoire parent du projet
2. lancer la création avec la commande suivante:

.. code-block:: bash

    $ cookiecutter https://github.com/Lincoln-France/cc-python -c cc-base

Remarques

    - L'argument ``-c/--checkout`` permet de passer d'une branche à l'autre. Par défaut la branche ``cc-base`` est utilisée.
    - Pour générer un template *datascience* par exemple, il faut utiliser l'argument ``-c cc-datascience``. 


Paramètres
----------

Lors de la génération d'un nouveau projet, une série de question est posée pour paramètrer le projet.


========================== ==================================== ======================================= ======= ==============
Paramètre                  Description                          Défaut                                  cc-base cc-datascience
========================== ==================================== ======================================= ======= ==============
organisation               Nom de l'organisation                Lincoln                                  ✓       ✓
lead_dev                   Nom du dev principal                 Lincoln Innovation                       ✓       ✓
email                      Email du dev principal               labinnovation@mel.lincoln.fr             ✓       ✓
github_username            Identifiant github du projet         Lincoln_France                           ✓       ✓
project_name               Nom du projet                        Python Boilerplate                       ✓       ✓
project_slug               Nom du projet version informatique   python-boilerplate                       ✓       ✓
package_name               Nom du package python                pythonboilerplate                        ✓       ✓
project_short_description  Description courte du projet         Projet *project_name* de *organisation*  ✓       ✓
version                    Version du projet                    0.1.0                                    ✓       ✓
use_pytest                 Pytest ou unittest (test framework)  n                                        ✓       ✓
command_line_interface     Framework de CLI                     Click (mais privilégier Argparse)        ✓       ✓
github_actions             Usage des GH Actions                 y                                        ✓       ✓
docker                     Création d'un Dockerfile de prod     n                                        ✓       ✓
docker_compose             Création d'un docker-compose de prod *docker*                                 ✓       ✓
devcontainer               Création d'un conteneur de dev       y                                        ✓       ✓
ssh_server_container       Serveur SSH dans le conteneur de dev n                                        ✓       ✓
open_source_license        Choix de la license                  Not open source                          ✓       ✓
========================== ==================================== ======================================= ======= ==============

Voici quelques détails:

use_pytest
""""""""""
Permet de créer un répertoire ``tests`` à la racine avec un module de test avec le framework choisi. Par défaut, est unittest_, un framework de base de python.

command_line_interface
""""""""""""""""""""""
Permet de créer un module ``cli.py`` d'interface en ligne de commande (CLI) dans le package. Par défaut le framework est Click_, mais nous privilégions Argparse, le framework natif de python.

github_actions
""""""""""""""
Permet de créer une arborescence pour les pipelines Github ``.github/workflows``. Le pipeline de tests et de documentation sont ajoutées.

docker
""""""
Génère un fichier squelette ``Dockerfile`` de production à la racine du projet. 

docker_compose
""""""""""""""
Génère un fichier squelette ``docker-compose.yaml`` de production à la racine du projet.

Remarques
    les ``!!PUID!!`` et ``!!PGID!!`` sont remplacées à la volée à la génération.

devcontainer
""""""""""""
Génère trois fichiers docker de dev afin de pouvoir développer dans un conteneur

- ``.devcontainer/Dockerfile-dev`` 
- ``./docker-compose-dev.yaml``
- ``.devcontainer/devcontainer.json`` fichier de configuration pour le `remote dev <https://code.visualstudio.com/docs/remote/containers>`_ de VScode

ssh_server_container
""""""""""""""""""""
Permet de créer un serveur SSH à l'intérieur d'un conteneur de dev. Cette fonctionnalité légèrement étrange peut être utile si on souhaite développer en remote dans un conteneur sur une VM.



Aller plus loin
---------------

Cookiecutter_ est pleins de ressources: `advanced usage <https://cookiecutter.readthedocs.io/en/latest/advanced/index.html>`_


.. _Cookiecutter: https://cookiecutter.readthedocs.io/en/latest/installation.html
.. _unittest: https://docs.python.org/fr/3.8/library/unittest.html
.. _Click: https://click.palletsprojects.com/en/7.x/
.. _Argparse: https://docs.python.org/fr/3/howto/argparse.html
