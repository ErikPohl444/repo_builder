import os
import shutil
import argparse
import git

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
        print(item.name, args.dest)
        if item.name == 'readme_template.md':
            print(f"converting readme template to readme: {item.name} to README.md")
            shutil.copyfile('readme_template.md', args.dest + 'README.md')
        elif item.name in ignore_files:
            print(f"ignore {item.name}")
        else:
            print(f"copying {item.name} to {args.dest+item.name}")
            shutil.copyfile(item.name, args.dest+item.name)
