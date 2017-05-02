import os
import toc_builder
import constants


def replace_sidebar_file_with_updated_sidbar_file(top_dr, toc_md):
    sidebar_path = os.path.join(top_dr,constants.sidebar_file_name)
    with open(sidebar_path, "w") as f:
        print(toc_md, end="", file=f)

    return


def apply_toc(input_path):

    tree = toc_builder.lvls(input_path)
    toc_md_formatted_str = toc_builder.construct_toc_from_wiki_tree(tree)
    replace_sidebar_file_with_updated_sidbar_file(input_path, toc_md_formatted_str)
    return toc_md_formatted_str

