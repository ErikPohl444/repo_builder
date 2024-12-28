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
            if os.path.exists(args.dest+item.name):
                print(f"adding a .donotuse to the file name so as not to overwrite existing file with same name")
                print(f"copying {item.name} to {args.dest + item.name}")
                shutil.copyfile(item.name, args.dest+item.name+".donotuse")
            else:
                print(f"copying {item.name} to {args.dest + item.name}")
                shutil.copyfile(item.name, args.dest+item.name)
                if item.name == "AUTHORS.md":
                    with open(args.dest+item.name, "wt") as authors_handle:
                        authors_handle.write('Author name|Author Email|Entry date\n')
                        authors_handle.write('-----------|------------|----------\n')
                        try:
                            dest_repo = git.Repo(args.dest)
                            first_commit = dest_repo.head.commit.author
                            author_name = first_commit.name
                            author_email = first_commit.email
                            authors_handle.write(f"{author_name}|{author_email}|12/27/24\n")
                        except:
                            print("couldn't access author info for destination repo because there is no commit history")
                


