Repo checklist:

* [ ] Run foundation.py with the destination project folder as a command line argument.  This will copy all important files to your project, renaming at least one.  Don't worry.  It won't overwrite existing files with the same names there.
* [ ] Use .gitignore_instructions.md to create a .gitignore file for your OS and project type, or leave it as-is and manually add it it.
* [ ] Follow AUTHORS_instructions to populate AUTHORS.md.  AUTHORS.md will be populated with the first commit author if Foundation can find an author. 
* [ ] [sponsor button](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/displaying-a-sponsor-button-in-your-repository)
* [ ] [social media image](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)
* [ ] [topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
* [ ] Populate ACKNOWLEDGEMENTS.md.
* [ ] Delete the current LICENSE if you don't want the MIT license.  You can select one with LICENSE_instructions if needed.
* [ ] Delete the current CODE_OF_CONDUCT.md if you don't want the recommended code of conduct.  You can select one with CODE_OF_CONDUCT_instructions if needed.
* [ ] Add to CODEOWNERS.md using CODEOWNERS_instructions.md.
* [ ] Follow CITATIONS_instructions.md to describe how to cite the code.
* [ ] Update README.md
* [ ] Edit Dockerfile.
* [ ] This is a parent checkbox for all Python-specific items:
  * [ ] Populate requirements.txt and keep it populated through pip freeze > requirements.txt
  * [ ] Confirm tests are in /tests
  * [ ] Confirm source code is in /source
  * [ ] Confirm docs are in /docs
  * [ ] Create Setup.py
