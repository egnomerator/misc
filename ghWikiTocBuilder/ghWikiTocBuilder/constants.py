import os

wiki_root_folder_name_ending = ".wiki"
path_prompt = "Enter root path (ending with \"{0}\"):"
path_prompt_msg = path_prompt.format(wiki_root_folder_name_ending)

valid_path_request_msg = "Double-check your path and try again."
processing_msg = "Constructing TOC from wiki directory structure ..."
complete_msg = "Done! Sidebar file updated with TOC."
view_toc_or_quit_msg = "Enter \"toc\" to view result or any other key to quit."
quit_msg = "Enter any key to quit."
closing_msg = "Goodbye"

sidebar = "_Sidebar"
sidebar_file_name = "_Sidebar.md"
excludes = set([".git", "Images"])

bullet = "* "
space = " "
lsqrBrkt = "["
rsqrBrkt = "]"
newline = "\n"
lparen = "("
rparen = ")"

toc_home_entry_fmt = "{0}{2}{1}{3}{4}{1}{5}{6}"
toc_entry_fmt = "{0}{1}{3}{3}{2}{4}{4}{5}"

