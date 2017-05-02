import os
import constants

def validate_input(p):
    # github wiki root folder name ends with ".wiki"
    if p[-5:] != constants.wiki_root_folder_name_ending:
        return False
    return True
