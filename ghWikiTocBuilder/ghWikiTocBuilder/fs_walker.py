import os
import constants

class Dir_level:
    depth = 0
    parent = ""
    directories = set()
    files= set()

def get_depth(top_dr,root):
    tdnp = os.path.normpath(top_dr)
    rdnp = os.path.normpath(root)
    td_depth = len(tdnp.split(os.sep))
    rd_depth = len(rdnp.split(os.sep))
    return rd_depth - td_depth

def print_lvl_info(depth,lvl):
    print(depth)
    print(lvl.parent)
    print(lvl.directories)
    print(lvl.files)

def walk_path_get_lvl_info(input_path):
    lvls = dict()
    for root, dirs, fls in os.walk(input_path):
    
        dirs[:] = [d for d in dirs if d not in constants.excludes]      # skip any dirs in excludes
        fls[:] = [f[:-3] for f in fls]                                  # remove .md ext from filenames

        dpth = get_depth(input_path,root)
    
        if not dpth in lvls.keys():
            lvls[dpth] = []
        dl = Dir_level()
        dl.depth = dpth
        dl.parent = root
        dl.directories = set(dirs)
        dl.files = set(fls)
    
        lvls[dpth].append(dl)
    
        #print(root)
        #print(dirs)
        #print(fls)
    return lvls

