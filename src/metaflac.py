#! /usr/bin/env python3

import subprocess, os.path

def get_attribute(name, file):
    result = subprocess.run(['metaflac', '--show-tag=' + name, file], stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE, shell = True)

    try:
        value = result.stdout.decode('utf-8')
    except:
        value = result.stdout.decode('iso-8859-1')

    assert result.returncode == 0
    assert value.lower().startswith(name + '=')

    return value[len(name) + 1:].rstrip()