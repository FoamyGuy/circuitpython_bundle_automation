
## To setup for automation tasks:
1. Clone the Library Bundle and update submodules. `clone_bundle.py` convenience script will do both
2. edit `automation_files/run_on_each.py` to do whatever you want. When it executes it will run in the root of each library in the bundle. You can use `os` to run commands with `os.system` or use python git API library. The `gh` CLI tool can be quite helpful for some things as well. You can test this by manually copying the file into the root of a library and running it.
3. copy `automation_files/` and `copy_automation_files.py` into the root of the bundle `Adafruit_CircuitPython_Bundle/`
4. `cd Adafruit_CircuitPython_Bundle` to get a terminal in the root of the bundle and execute the scripts with the following command.

To execute the automation tasks:
```shell
git submodule foreach "python ../../../copy_automation_files.py;python run_on_each.py"
```


## To execute against a subset of the bundle for testing (or any purpose):
1. copy `list_submodules.py` into the root of the bundle and run it with `python list_submodules.py`
2. it will create `helpers.txt` and `drivers.txt` files
3. open these files and edit them as desired. Leave any libraries that you want to be (temporarily) removed from the bundle for the task execution. Delete any libraries from these files that you want the task to execute on. i.e. if you want to test your task on two libraries, one of each type then you would delete the first line of each file.
4. copy `remove_submodules.py` into the root of the bundle and run it with `python remove_submodules.py` it will remove all libraries that are listed in each of the text files (leaving alone any that you deleted from the txt file in the previous step)
5. at this point you can use the instructions above to execute your automation task and it will now execute against only the subset that remains after the removal. 




## Some examples of previous automation tasks:
These may provide ideas or inspiration about ways to interact with the repos via python, git, and gh CLI tools.
- https://github.com/FoamyGuy/bundle_change_discord_badge
- https://github.com/FoamyGuy/missing_type_issue_maker
- https://github.com/FoamyGuy/readme_docs_links