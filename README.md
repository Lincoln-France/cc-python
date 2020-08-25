README
======

> Template de base pour générer un projet python

## Installation

Ce projet est crée grâce à [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)

```bash
pip install -U cookiecutter
```

Générer un package python aux normes Lincoln:

```bash
cookiecutter http://factory.lincoln.cloud/git/Innovation/base-python-project
```

Plusieurs questions pour parametrer le projet seront posées.


## Paramètres

Lorsque vous générer un nouveau projet, plusieurs questions sont posées:

1. Le nom de l'organisation concernant le projet (défaut: Lincoln Innovation)
2. Le dev principal du projet (défaut: Innovation Squad)
3. Le mail du dev principal (défaut: innovationsquad@mel.lincoln.fr)
4. Le username gitea associé au projet (défaut: Innovation)
5. Nom du projet (défaut: Python Boilerplate)
6. Slug du projet, ou le nom du dossier du projet (défaut: python-boilerplate)
7. Nom du package (défaut: pythonboilerplate)
8. Description du projet (défaut: Encore un nouveau projet du Lab Innovation qui va cartonner !)
9. Version (défaut: 0.1.0)
10. Framework pytest pour les tests unitaires (défaut: n)
11. Framework CLI (défaut: Click)
12. Usage de docker (défaut: y)
13. Usage de docker-compose (défaut: y)
14. License (défaut: Not Open Source)


## Un projet, mais aussi un package !

Il faut savoir que le projet que vous créer aura la chance d'être aussi un package python.

Le + d'un package python (si si, ca peut être chouette):

* Portabilité
* Versionning
* Installation simple
* Dépendences contrôlées
* Documentation
* Testables

Le - d'un package python (soyons lucide):

* Coûteux en temps au début (apprentissage du cycle de developpement)
* Documentation (oui, c'est aussi un point négatif)


## Architecture

### Les répertoires

```bash
.
├── {{ cookiecutter.project_name }}       # module principal
├── requirements/       # dossier contenant les requirements python
├── tests/              # dossier contenant les tests du package
├── logs/               # dossier contenant les logs : dev specific
├── scripts/            # dossier contenant les scripts utilisant le package
├── docs/               # documentations générées par sphinx
├── .github/            # template PR, Issues sur github, gitea, ...
```

### Les fichiers importants

```bash
.
├── {{ cookiecutter.project_name }}
│   ├── __init__.py                 # topc level package
├── README.md                       # this file
├── HISTORY.md                      # historique des version et les modifications
├── CONTRIBUTING.md                 # comment contribuer au projet
├── LICENSE                         # license si besoin
├── Makefile                        # Makefile: aide à la compilation
├── .gitignore                      # Liste des éléments que git doit ignorer lors du commit
├── requirements.txt                # Contient les dépendances (=packages) pyhton du projet
├── setup.cfg                       # aide au setup.py
├── setup.py                        # setup.py pour créer un package python
├── tox.ini                         # aide pour les tests
├── docker-compose.yaml             # docker-compose du projet (optionnel)
├── Dockerfile                      # construction de l'image (optionnel)
├── .env                            # variable d'environnement (optionnel)
```

## Contribuer

Faites un tour sur la documentation de cookiecutter, vous trouverez des astuces pour améliorer l'expérience.
Il est aussi possible de faire évoluer ce projet en créant une issue et/ou une pull request :) !
