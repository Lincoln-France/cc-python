Généralités
===========


Cookiecutter_ est un CLI (command line interface) permettant de générer un projet à partir d'un template.

L'idée est parfaite pour initier un projet rapidement prêt à l'emploi ! Plus besoin de copier d'ancien projet et de bidouiller pour avoir un projet clean :) !

Chez Lincoln nous avons adopté cette nouvelle pratique pour nos projets python. Nous nous sommes basés sur l'excellent template cookiecutter-pypackage_ de Audrey Roy Greenfeld. 

Nos pratiques nous ont amené à forker le template et ajouter nos propres modifications. Il existe d'ailleurs plusieurs templates python sur l'internet pour différentes tâches, n'hésitez pas à vous en inspirer.

En tout cas, ce projet est notre template. Il évolue au fur et à mesure des nos besoins et expériences. Cette documentation est en cours de construction et a pour objectif de vous livrer un maximum d'information pour pouvoir utiliser ce template, voire même l'améliorer !

Pour tout vous dire, nous développons déjà deux templates python et quelques-un sont en carton:

- :doc:`cc-base</cc-base>`: template python de base, c'est une base commune aux autres
- :doc:`cc-datascience</cc-datascience>`: template python pour nos projets datascience
- :doc:`cc-lite</cc-lite>`: template python simplifié pour des projets rapides sans complexité *(en construction)*
- :doc:`cc-api</cc-api>`: template python pour des api simples *(en construction)*


Voici un avant-goût de son usage. Imaginons qu'un projet datascience commence:


Il est nécessaire d'installer le CLI *cookiecutter*:

.. code-block:: bash
    
    $ cookiecutter --version
    Cookiecutter 1.7.2

La commande pour générer le projet. Une série de question pour générer le projet adequat.

.. code-block:: bash

    $ cookiecutter https://github.com/Lincoln-France/cc-python.git -c cc-datascience
    Do you want to re-use the existing version? [yes]: yes
    organisation [Lincoln Innovation]:
    lead_dev [Innovation Squad]:
    email [innovationsquad@mel.lincoln.fr]:
    github_username [Lincoln_France]:
    project_name [Python Boilerplate]:
    project_slug [python-boilerplate]:
    package_name [pythonboilerplate]:
    project_short_description [Encore un nouveau projet du Lab Innovation qui va cartonner !]:
    version [0.1.0]:
    use_pytest [n]:
    Select command_line_interface:
    1 - Click
    2 - Argparse
    3 - No command-line interface
    Choose from 1, 2, 3 [1]: 2
    github_actions [y]:
    docker [y]:
    docker_compose [y]:
    devcontainer [y]:
    ssh_server_container [n]:
    Select open_source_license:
    1 - Not open source
    2 - MIT license
    3 - BSD license
    4 - ISC license
    5 - Apache Software License 2.0
    6 - GNU General Public License v3
    Choose from 1, 2, 3, 4, 5, 6 [1]: 2
    Setting-up conda environment...
    Installing kernel for jupyter notebooks...
    Installed kernelspec python-boilerplate in /home/lincoln/.local/share/jupyter/kernels/python-boilerplate

Un environment conda est créé et le repertoire du projet:

.. code-block:: bash

    $ cd python-boilerplate
    $ ls -lrth 
    -rw-r--r-- 1 lincoln lincoln 1,9K févr. 25 18:15 setup.py
    -rw-r--r-- 1 lincoln lincoln 2,6K févr. 25 18:15 Makefile
    -rw-r--r-- 1 lincoln lincoln  136 févr. 25 18:15 AUTHORS.md
    -rw-r--r-- 1 lincoln lincoln   50 févr. 25 18:15 HISTORY.md
    -rw-r--r-- 1 lincoln lincoln  472 févr. 25 18:15 setup.cfg
    -rw-r--r-- 1 lincoln lincoln 1,1K févr. 25 18:15 LICENSE
    -rw-r--r-- 1 lincoln lincoln 2,8K févr. 25 18:15 README.md
    -rw-r--r-- 1 lincoln lincoln  120 févr. 25 18:15 environment.yml
    -rw-r--r-- 1 lincoln lincoln  291 févr. 25 18:15 MANIFEST.in
    -rw-r--r-- 1 lincoln lincoln   26 févr. 25 18:15 CONTRIBUTING.md
    -rw-r--r-- 1 lincoln lincoln  298 févr. 25 18:15 tox.ini
    drwxr-xr-x 2 lincoln lincoln 4,0K févr. 25 18:15 models
    drwxr-xr-x 2 lincoln lincoln 4,0K févr. 25 18:15 scripts
    drwxr-xr-x 2 lincoln lincoln 4,0K févr. 25 18:15 requirements
    drwxr-xr-x 2 lincoln lincoln 4,0K févr. 25 18:15 notebooks
    drwxr-xr-x 6 lincoln lincoln 4,0K févr. 25 18:15 data
    drwxr-xr-x 2 lincoln lincoln 4,0K févr. 25 18:15 logs
    drwxr-xr-x 2 lincoln lincoln 4,0K févr. 25 18:15 docs
    drwxr-xr-x 2 lincoln lincoln 4,0K févr. 25 18:15 pythonboilerplate
    drwxr-xr-x 2 lincoln lincoln 4,0K févr. 25 18:15 tests
    -rw-r--r-- 1 lincoln lincoln  670 févr. 25 18:16 Dockerfile
    -rw-r--r-- 1 lincoln lincoln  385 févr. 25 18:16 docker-compose.yaml
    -rw-r--r-- 1 lincoln lincoln 2,0K févr. 25 18:16 docker-compose-dev.yaml
    drwxr-xr-x 2 lincoln lincoln 4,0K févr. 25 18:16 pythonboilerplate.egg-info


.. _Cookiecutter: https://cookiecutter.readthedocs.io/en/latest/
.. _cookiecutter-pypackage: https://github.com/audreyfeldroy/cookiecutter-pypackage

