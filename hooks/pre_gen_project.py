import os
import re
import sys

if __name__ == '__main__':

    MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

    package_name = '{{ cookiecutter.package_name }}'

    if not re.match(MODULE_REGEX, package_name):
        print('ERROR: The package name (%s) is not a valid Python module name. Please do not use a - and use _ instead' % package_name)

        # Exit to cancel project
        sys.exit(1)

    # Look for conda
    if os.system('conda -V'):
        print('ERROR: Conda is not installed or your PATH is not defined correctly.')

        # Exit to cancel project
        sys.exit(1)