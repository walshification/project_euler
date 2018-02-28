import os

from sniffer.api import file_validator, runnable
import termstyle


pass_fg_color = termstyle.green
pass_bg_color = termstyle.bg_default
fail_fg_color = termstyle.red
fail_bg_color = termstyle.bg_default

watch_paths = ['solutions/', 'tests/', './scent.py']


@file_validator
def py_files(filename):
    return (filename.endswith('.py') and
            not os.path.basename(filename).startswith('.'))


@runnable
def execute_manage_test(*args):
    import os
    os.system('env/bin/coverage erase')
    exit_code = os.system(
        'env/bin/coverage run --rcfile=setup.cfg -m unittest discover'
    )
    os.system('env/bin/coverage report --rcfile=setup.cfg')
    os.system('env/bin/coverage html --rcfile=setup.cfg; touch htmlcov')
    return exit_code == 0
