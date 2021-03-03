Lincoln: cookiecutter-base
==========================

Contexte
--------

cookiecutter-base ou *cc-base* est le template racine des autres template. Il se situe sur la branche ``cc-base`` du dépôt.
L'usage de ce template est très général, il s'emploie dans l'ensemble des projets python. 

*Remarques*
    - Le projet contiente encore plusieurs coquilles et nous les corrigeons à l'usage. Ouvrer une issue pour nous avertir d'erreur.
    - La documentation est en cours de construction.
    - Nous souhaitons développer les fonctionnalités dans des tutoriels.

Structure
---------

Le template est très riche dans son arborescence pour couvrir un ensemble d'usage. Par défaut, la structure est la suivante:

.. code-block:: bash

    .
    ├── {{ cookiecutter.project_slug }}/            # répertoire du projet
    │   ├── .devcontainer/                          # répertoire du remote dev (optionnel)
    │   │   ├── devcontainer.json                   # fichier de configuration vscode pour le remote dev
    │   │   ├── Dockerfile-dev                      # dockerfile de dev
    │   ├── .github/                                # répertoire spécifique à github (optionnel)
    │   │   ├── workflows/                          # répertoire spécifique aux actions github
    │   │   │   ├── documentation-actions.yml       # action par défaut de documentation
    │   │   │   ├── testing-actions.yml             # action par défaut de tests
    │   ├── docs/                                   # répertoire de la documentation du package
    │   │   ├── conf.py                             # configuration de la documentation sphinx
    │   │   ├── index.rst                           # index de la documentation par défaut
    │   │   ├── installation.rst                    # documentation d'installation du package par défaut
    │   │   ├── make.bat                            # makefile windows
    │   │   ├── Makefile                            # Makefile
    │   │   ├── usage.rst                           # documentation de l'usage du package par défaut
    │   ├── logs/                                   # répertoire de la log
    │   ├── {{ cookiecutter.package_name }}/        # répertoire du package python
    │   │   ├── __init__.py                         # fichier init python
    │   │   ├── cli.py                              # fichier interface de commande par défaut
    │   │   ├── {{ cookiecutter.package_name }}.py  # module principal exemple
    │   ├── requirements/                           # répertoire pour définir les dépendances du package
    │   │   ├── dev.txt                             # dépendances de développement
    │   │   ├── prod.txt                            # dépendances de production
    │   ├── scripts/                                # répertoire des scripts utilisant le package
    │   ├── test/                                   # répertoire des tests unitaires
    │   ├── .gitignore                              # liste des éléments que git doit ignorer lors du commit
    │   ├── AUTHORS.md                              # référence les auteurs
    │   ├── CONTRIBUTING.md                         # comment contribuer au projet
    │   ├── docker-compose-dev.yaml                 # docker-compose de dev du projet (optionnel)
    │   ├── docker-compose.yaml                     # docker-compose du projet (optionnel)
    │   ├── Dockerfile                              # dockerfile de prod du projet (optionnel)
    │   ├── HISTORY.md                              # historique des versions et les modifications
    │   ├── Makefile                                # Makefile: aide à la compilation
    │   ├── MANIFEST.in                             # liste les fichiers à inclure dans le package
    │   ├── README.md                               # présentation technique du projet
    │   ├── requirements.txt                        # fichier de dépendances (=packages) python du projet
    │   ├── setup.cfg                               # configure des fonctionnalités python dans l'environnement
    │   ├── setup.py                                # setup.py pour créer un package python
    │   ├── tox.ini                                 # aide pour les tests
    │   ├── LICENSE                                 # license si besoin


Fonctionnement
--------------

Ce template étant un fork du cookiecutter-pypackage_, on retrouve l'ensemble des features_ disponibles. Quelques évolutions ont été apportées.


Makefile
""""""""
Le ``./Makefile`` à la racine du projet est un fichier décrivant plusieurs tâches liées au projet. Chaque commande est un ensemble de ligne de commande pour effectuer une tâche.
Voici quelques exemples:

.. code-block:: bash

    $ make help        # affiche les différentes tâches
    $ make clean       # nettoie le projet des fichiers temporaires
    $ make docs        # génère la documentation
    $ make install-dev # installe le package en mode développement
    $ make test-all    # test le package avec tox


Sphinx
""""""
L'usage de sphinx_ comme outil de documentation est intégré. La documentation se trouve dans le répertoire ``./docs``.
Pusieurs tâches ``make`` permettent de générer de la documentation:

.. code-block:: bash

    $ make docs
    $ make servedocs


Tox
"""
L'usage de l'utiliaire tox_ est conseillé pour les tests unitaires.

.. code-block:: bash

    $ make test-all
    $ tox
    $ tox -e flake8 # test linting

Il est possible de tester le package avec la commande ``make test`` sans passer par tox.


Package
"""""""
Le projet crée par le template est un package qui peut être installé. Un package permet de pouvoir appeler les modules python dans n'importe quel script python: le package est dans le chemin de recherche des modules python.

..  code-block:: bash

    $ make install

Alors, si *package.package_name* est *pythonboilerplate*

>>> import pythonboilerplate
>>> pythonboilerplate.__author__
Lincoln
>>> pythonboilerplate.__version__
0.1.0

En cas de développement, il est préférable d'installer le package en mode développement pour actualiser en temps réel les modules.

.. code-block:: bash

    $ make install-dev


Scripts
"""""""
Nous conseillons de développer des fonctions et classes (génériques) dans des modules du package et d'écrire des scripts executables dans ``./scripts`` qui importent ces fonctions/classes dans un cadre d'execution précis.

La limite n'est jamais franche entre du code ré-utilisable et une application précise dans un cas d'usage, cela dit. Chaque cas est différent, mais l'idée est de faire évoluer ses pratiques vers des codes les plus génériques possibles dans le package.


Docker en dev
"""""""""""""
L'usage d'un conteneur docker en développement est une bonne idée pour isoler entièrement l'environnement du projet. Cette fonctionnalité est possible en utilisant le paramètre ``devcontainer: y`` à la création du projet.

Le dockerfile ``.devcontainer/Dockerfile-dev`` est créé et installe les dépendances spécifiées dans ``requirements/dev.txt``. Les bonnes pratiques docker impliquent de créer un user différent du ``root`` dans le conteneur. Par défaut le username est ``lincoln``. Le ``uid`` et ``gid`` sont calculés à la volée pour générer un user dans le conteneur capable de lire et écrire sur volumes montés. Par défaut le dossier du projet est montée dans le répertoire ``$WORKDIR=/package``

Pour faciliter le build, le montage de volume et l'ajout d'image docker dépendantes au projet, un fichier docker-compose_ ``docker-compose-dev.yaml`` est créé. 

Enfin, l'IDE vscode_ met à disposition une extension `remote - Containers <https://code.visualstudio.com/docs/remote/containers>`_ pour développer à l'intérieur d'un conteneur. Cette extension est paramétrable à l'aide du fichier ``.devcontainer/devcontainer.json``. Plusieurs configurations sont possibles, mais nous utilisons celle qui se base sur un docker-compose déjà existant: cela limite la dépendance à l'extension.


**Remarques**
    - Cette fonctionnalité n'a pas été testé pour Windows. Le système de uid/gid devrait être bloquant.
    - L'image de base est ``python:3.7-buster``. A modifier en fonction des besoins.
    - La command lancée avec le docker-compose permet de garder en vie le conteneur afin de développer.
    - En ajoutant la ligne ``ENV PYTHONPATH=$PYTHONPATH:/usr/lib/python3/dist-packages`` dans le dockerfile, les packages compilés de debian sont également dans le path python.


Docker en prod
""""""""""""""
Le paramètre ``docker: y`` à la création du projet permet de créer un template ``Dockerfile`` similaire au dockerfile de dev.
Idem pour la paramètre ``docker-compose: y``.


.. _cookiecutter-pypackage: https://github.com/audreyfeldroy/cookiecutter-pypackage
.. _features: https://cookiecutter-pypackage.readthedocs.io/en/latest/readme.html#features
.. _sphinx: https://www.sphinx-doc.org/en/master/
.. _tox: https://tox.readthedocs.io/en/latest/
.. _docker-compose: https://docs.docker.com/compose/
.. _vscode: https://code.visualstudio.com/