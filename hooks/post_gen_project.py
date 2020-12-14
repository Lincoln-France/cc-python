#!/usr/bin/env python
import os
import shutil
import sys

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_folder(folderpath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, folderpath), ignore_errors=True)


def fill_uid_gid_in_file(filepath: str, pattern='!!'):

    try:
        with open(filepath, 'r') as _file:
            data = _file.read()

        data = data.replace(pattern + 'PUID' + pattern, str(os.getuid()))
        data = data.replace(pattern + 'PGID' + pattern, str(os.getgid()))

        with open(filepath, 'w') as _file:
            _file.write(data)
    except Exception as err:
        print(str(err))
        sys.exit(1)


if __name__ == '__main__':

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.package_name }}', 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if '{{ cookiecutter.docker }}' == 'n':
        remove_file('Dockerfile')
        remove_file('docker-compose.yaml')
    else:
        fill_uid_gid_in_file(filepath='Dockerfile')
        fill_uid_gid_in_file(filepath='docker-compose.yaml')
        if '{{ cookiecutter.docker_compose }}' == 'n':
            remove_file('docker-compose.yaml')

    if '{{ cookiecutter.devcontainer }}' == 'n':
        remove_folder('.devcontainer')
        remove_file('docker-compose-dev.yaml')

    if '{{ cookiecutter.vscode_starter_settings }}' == 'n':
        remove_folder('.vscode')

    # Setting up conda environment
    print('Setting-up conda environment...')
    os.system("conda env create -f %s/environment.yml > /dev/null" % PROJECT_DIRECTORY)
