import sys

import reload
import settings
import cmd
import os

def find_page(for_search, flags):
    data = read_data(flags, settings.DATA_FILE)
    res = [record for record in data if record[0].upper().startswith(for_search)]
    res.sort()
    return res

def read_data(flags, data_file):
    check_data(flags, data_file)
    try:
        f = open(data_file, 'r')
    except:
        print("can't open file with instructions data")
        print("exit...")
        sys.exit(-1)
    data = [s.split() for s in f.readlines()]
    f.close()
    return data

def check_data(flags, data_file):
    if (not flags.is_set(cmd.cmd_flags.RELOAD)) and os.path.exists(data_file) and os.path.isfile(data_file):
        return
    print("reload")
    reload.reload(data_file)

