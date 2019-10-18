import sys
import subprocess
import requests
import os
import re

import reload
import load_data
import open
import cmd

def multiple_choice(flags, variants):
    print_menu(variants)
    flag = True
    pos = 0
    while flag:
        flag = False            
        try:
            s = input("enter number or press enter for [E]").strip()
            if not s: 
                pos = 0
            elif int(s) < len(pages): 
                pos = int(s)
            else:
                raise IndexError
        except EOFError:
            print()
            exit()
        except:
            flag = True
    open.open_page(flags, pages[pos][1])

def print_menu(variants):
    print("[E]", pages[0][0])
    for i, record in enumerate(pages[1:]):
        print("[{}] {}".format(i+1, record[0]))

flags, instruction = cmd.parse_cmd_args(sys.argv)
pages = load_data.find_page(instruction, flags)

if len(pages) == 0:
    print("noting found")
elif len(pages) == 1:
    open.open_page(flags, pages[0][1])
else:
    multiple_choice(flags, pages)
