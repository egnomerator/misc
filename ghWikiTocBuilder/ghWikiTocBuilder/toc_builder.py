import os
import constants
import fs_walker

def mdify_toc_entry(entry_name, depth):
    indent = constants.space * depth * 2
    if depth < 1:
        return constants.toc_home_entry_fmt.format(constants.bullet, entry_name, constants.lsqrBrkt, constants.rsqrBrkt, constants.lparen, constants.rparen, constants.newline)
    return constants.toc_entry_fmt.format(indent, constants.bullet, entry_name, constants.lsqrBrkt, constants.rsqrBrkt, constants.newline)

def traverse_convert_lvl_to_toc_entries(lvls, toc_str, depth, parent_dir):
    drlvls = lvls[depth]
    parent = ""

    for drlvl in drlvls:

        depth = drlvl.depth
        dirs = drlvl.directories
        files = drlvl.files

        # skip if in a drlvl at this level but not within this parent
        if parent_dir != "":
            pdnp = os.path.normpath(drlvl.parent)
            parent = pdnp.split(os.sep)[-1:][0]
            if parent_dir != parent:
                continue

        dirs.sort()
        for d in dirs:
            toc_str += mdify_toc_entry(d, depth)
            toc_str = traverse_convert_lvl_to_toc_entries(lvls, toc_str, depth+1, d)

        files[:] = [f for f in files if f not in dirs]  # skip any files that match dirs (this wiki page already accounted for via dir)
        files.sort()
        for f in files:
            if f == constants.sidebar:
                return toc_str
            toc_str += mdify_toc_entry(f, depth)

    return toc_str


def construct_toc_from_wiki_tree(lvls):
    toc_str = ""
    toc_str = traverse_convert_lvl_to_toc_entries(lvls, "", 0, "")
    return toc_str

def lvls(input_path):
    return fs_walker.walk_path_get_lvl_info(input_path)

