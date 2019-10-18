import sys

def usage():
    print(
'''USAGE: parse.py <flags> <instruction>
    flags:
    -f    print only info about processor flags
    -r    reloads information about instructions from https://c9x.me/x86/
''')

class cmd_flags:
    def __init__(self):
        self.value = 0

    def add_flag(self, flag):
        self.value |= flag

    def add_flag_cmd(self, str):
        self.value |= cmd_flags.flags[str] 

    def is_set(self, flag):
        return self.value & flag

    PRINT_FLAGS = 0x01
    OPEN_ORIG   = 0x80
    RELOAD      = 0x40
    flags = {
        '-f':PRINT_FLAGS,
        '-r':RELOAD,
    }

def is_flag(str):
    return str in cmd_flags.flags.keys()

def parse_cmd_args(args):
    args = args[1:]
    flags = cmd_flags()
    display_all = True
    for arg in args.copy():
        if is_flag(arg):
            flags.add_flag_cmd(arg)
            if arg == '-f':
                display_all = False
            args.remove(arg)
    if display_all:
        flags.add_flag(cmd_flags.OPEN_ORIG)
    if len(args) == 1:
        instruction = args[0]
    else:
        usage()
        sys.exit()
    instruction = instruction.strip().upper()
    return flags,instruction

