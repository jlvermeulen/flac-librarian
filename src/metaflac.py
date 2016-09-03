#! /usr/bin/env python3

import subprocess, os, os.path

def get_attribute(name, file):
    info = None
    if os.name == 'nt':
        info = subprocess.STARTUPINFO()
        info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        info.wShowWindow = subprocess.SW_HIDE

    process = subprocess.Popen(['metaflac', '--show-tag=' + name, file], stdout = subprocess.PIPE, startupinfo = info)
    result = process.communicate()[0]

    try:
        value = result.decode('utf-8')
    except:
        value = result.decode('iso-8859-1')

    assert process.returncode == 0
    assert value.lower().startswith(name + '=')

    return value[len(name) + 1:].rstrip()
