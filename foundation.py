import os
import shutil
import argparse
import git
from datetime import date


def safe_copy(src, dest):
    if os.path.exists(dest):
        print(f"adding a .resource to the file name so as not to overwrite existing file with same name")
        dest += '.resource'
    print(f"copying {item.name} to {args.dest + item.name}")
    shutil.copyfile(src, dest)
    return True


def append_authors(dest, repo_folder):
    with open(dest, "wt") as authors_handle:
        authors_handle.write('Author name|Author Email|Entry date\n')
        authors_handle.write('-----------|------------|----------\n')
        try:
            dest_repo = git.Repo(repo_folder)
            first_commit = dest_repo.head.commit.author
            author_name = first_commit.name
            author_email = first_commit.email
            today = date.today()
            formatted_date = today.strftime("%d/%m/%Y")
            authors_handle.write(f"{author_name}|{author_email}|{formatted_date}\n")
        except ValueError:
            print("couldn't access author info for destination repo because there is no commit history")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="move foundation files")
    parser.add_argument('dest', type=str, help="the destination for the foundation")
    args = parser.parse_args()
    x = git.Repo(os.curdir)
    if not os.path.exists(args.dest):
        print(f"{args.dest} does not exist")
        raise ValueError
    else:
        print(f"{args.dest} exists")

    ignore_files = ["foundation.py", "README.md"]

    for item in x.tree().traverse():
        dest_file_name = args.dest + item.name
        print(f"naming {dest_file_name} as the destination file and path")
        if item.name == 'readme_template.md':
            print(f"converting readme template to readme: {item.name} to README.md")
            safe_copy('readme_template.md', args.dest + 'README.md')
        elif item.name in ignore_files:
            print(f"ignoring {item.name}")
        else:
            safe_copy(item.name, dest_file_name)
            if item.name == "AUTHORS.md":
                append_authors(dest_file_name, args.dest)
