#! /usr/bin/env python3

import subprocess

def get_attribute(name, file):
    result = subprocess.run(['metaflac', '--show-tag=' + name, file], stdout = subprocess.PIPE)
    value  = result.stdout.decode('utf-8')

    assert value.startswith(name + '=')
    return value[len(name) + 1:].rstrip()