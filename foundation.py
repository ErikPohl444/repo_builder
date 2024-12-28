import os
import shutil
import argparse
import git
from datetime import date
from setup_logging import logger


def safe_copy(src, dest):
    if os.path.exists(dest):
        logger.info(f"adding a .resource to the file name so as not to overwrite existing file with same name")
        dest += '.resource'
    logger.info(f"copying {repo_resource_name.name} to {args.dest + repo_resource_name.name}")
    shutil.copyfile(src, dest)
    return True


def append_authors(dest_repo, repo_folder):
    logger.info("Appending author info if available from destination repo")
    with open(repo_folder+"AUTHORS.md", "wt") as authors_handle:
        authors_handle.write('Author name|Author Email|Entry date\n')
        authors_handle.write('-----------|------------|----------\n')
        try:
            first_commit = dest_repo.head.commit.author
            author_name = first_commit.name
            author_email = first_commit.email
            today = date.today()
            formatted_date = today.strftime("%d/%m/%Y")
            try:
                authors_handle.write(f"{author_name}|{author_email}|{formatted_date}\n")
            except IOError:
                logger.info("Couldn't write to authors file")
                return False
        except ValueError:
            print("couldn't access author info for destination repo because there is no commit history")
            return False
    return True


if __name__ == '__main__':
    logger.info("Attempting to build a foundation based on https://github.com/ErikPohl444/resources")
    logger.info("Getting destination folder from the command line arguments")
    parser = argparse.ArgumentParser(description="move foundation files")
    parser.add_argument('dest', type=str, help="the destination for the foundation")
    args = parser.parse_args()
    if not args:
        logger.info("No destination was specified, so not building a foundation")
        raise ValueError
    logger.info("Obtaining git repo info from the destination")
    try:
        dest_repo = git.Repo(os.curdir)
    except git.exc.GitCommandError:
        logger.info("No destination git repo")
    if not os.path.exists(args.dest):
        logger.info(f"{args.dest} does not exist, so we can't build the foundation")
        raise ValueError
    else:
        logger.info(f"{args.dest} exists, so we can build the foundation")
    ignore_files = ["foundation.py", "README.md"]
    logger.info(f"defined ignore file list [{ignore_files}] for files not to copy to destination")
    for repo_resource_name in dest_repo.tree().traverse():
        dest_file_name = args.dest + repo_resource_name.name
        logger.info(f"naming {dest_file_name} as the destination file and path")
        if repo_resource_name.name == 'readme_template.md':
            logger.info(f"converting readme template to readme: {repo_resource_name.name} to README.md")
            safe_copy('readme_template.md', args.dest + 'README.md')
        elif repo_resource_name.name in ignore_files:
            logger.info(f"ignoring {repo_resource_name.name} from copy to destination")
        else:
            safe_copy(repo_resource_name.name, dest_file_name)
            if repo_resource_name.name == "AUTHORS.md":
                append_authors(dest_repo, args.dest)
