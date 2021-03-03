Lincoln: cookiecutter-datascience
=================================

Contexte
--------

cookiecutter-datascience ou *cc-datascience* est le template destiné au projet orienté datascience. Il est basé sur *cc-base* avec quelques modifications:

- Ajout de répértoires ``notebooks`` et ``data``
- Usage de conda

*Remarques*
    - Le projet contiente encore plusieurs coquilles et nous les corrigeons à l'usage. Ouvrer une issue pour nous avertir d'erreur.
    - La documentation est en cours de construction.
    - Nous souhaitons développer les fonctionnalités dans des tutoriels.
    - Ce temple est aussi inspiré du célèbre template cookiecutter-datascience_.
    - L'installation de l'utiliaire conda est requis.

Nous présentons les fonctionnalités ajoutées par rapport à *cc-base*.

Structure
---------

Le template hérite de l'arborescence de *cc-base**. Par défaut, la structure est la suivante:

.. code-block:: bash

    .
    ├── {{ cookiecutter.project_slug }}/            # répertoire du projet
    |   .                                           # arborescence
    |   .                                           # similaire 
    |   .                                           # à cc-base
    │   ├── data/                                   # répertoire de données
    │   │   ├── external                            # données externes
    │   │   ├── interim                             # données temporaires
    │   │   ├── processed                           # données finales
    │   │   ├── raw                                 # données bruts
    │   ├── notebooks/                              # répertoire des notebooks
    │   ├── environnement.yml                       # fichier d'environnement conda


Fonctionnement
--------------

Ce template hérite de *cc-base*, on retrouve l'ensemble des fonctionnalités. Voici celles qui ont été ajoutées.


conda
"""""
Conda_ est un système de gestion d'environnement. Il est largement utilisé dans la communauté scientifique car il permet de gérer facilement les environnements et les dépendances de package. 

Par défaut, un environnement conda nommé *project_name* (e.g. python-boilerplate) à la création du projet. L'environnement est ajouté aux kernels de jupyer qui est installé à la création également.


data
""""
Des répertoires pour sauvegarder les données:


- ``data/exteral``: données externes.
- ``data/interim``: données temporaires, issus d'étapes intermédiaire.
- ``data/processed``: données finales.
- ``data/raw``: données bruts.

*Remarque*
    - ce n'est qu'un exemple, la structure est libre. 


notebooks
"""""""""
nous utilisons un répertoire pour sauvegarder les jupyer notebooks.
Comme pour les scripts du répertoire ``scripts``, ces notebooks ne doivent pas comporter de définition de fonction ou de classes. Ces dernières doivent être définies dans le package.

.. _cookiecutter-datascience: https://github.com/drivendata/cookiecutter-data-science
.. _Conda: https://docs.conda.io/en/latest/
