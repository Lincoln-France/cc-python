import os
import re
import sys

if __name__ == '__main__':

    MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

    package_name = '{{ cookiecutter.package_name }}'
    conda_env_name = '{{ cookiecutter.project_name.lower().replace(' ', '-') }}'

    if not re.match(MODULE_REGEX, package_name):
        print('ERROR: The package name (%s) is not a valid Python module name. Please do not use a - and use _ instead' % package_name)

        # Exit to cancel project
        sys.exit(1)

    # Look for conda
    if os.system('conda -V > /dev/null'):
        print('ERROR: Conda is not installed or your PATH is not defined correctly.')

        # Exit to cancel project
        sys.exit(1)

    # Look for conflict with existing conda environment
    env_clean = os.system("(conda env list | grep -c '^%s\\b' && echo 0) > /dev/null" % conda_env_name)
    if not env_clean:
        print('ERROR: There is already a conda envionment with name %s.' % conda_env_name)
