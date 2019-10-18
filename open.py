import subprocess
import re
import requests

import settings
import cmd

def open_full(link):
    print("opening...")
    subprocess.run([settings.BROWSER, link])

def open_flags(link):
    data = requests.get(link).text
    res = re.findall('<th>Flags affected</th>.*?<p>(.*?)</p>', data, re.DOTALL)
    print('Flags affected:')
    for i in res:
        print('\t', i)

def open_page(flags, link):
    if flags.is_set(cmd.cmd_flags.OPEN_ORIG):
        open_full(link)
    elif flags.is_set(cmd.cmd_flags.PRINT_FLAGS):
        open_flags(link)
