## Fly With Me 

Hello BU MET CS673 classmates!

I've created this quick flask demo for you to check out. These directions were written for OSX (Mac). **If you have the correct instructions for windows, please update the document with the directions for a windows setup.** I have included a template for such instructions below.

I've used the [very accessible tutorial by Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database) as a base for this project. We can create a new project if we want, but I wanted you to have something to work with for now.

You'll notice that I'm putting `python3 -m` before many of these commands. This is to ensure that we use the package python to install any requirements.

### How to get started (on windows) (EDIT ME)

1. Install [Python 3](https://www.python.org/downloads/).

2. Clone the [repo](https://github.com/katdob/FlyWithMe.git) by running `git clone https://github.com/katdob/FlyWithMe.git`.

3. run `cd FlyWithMe` to enter the project directory

4. set up the virtual environment by running `python3 -m venv venv` and `source venv/bin/activate` to enter the virtual environment (you can leave the virtual environment with `deactivate`) 

5. run `python3 -m pip install -r requirements` to install all of the required packages for the project

6. run `export FLASK_APP=app` in your terminal to tell flask where to find the app

7. run `flask db init` to initialize the database

8. run `flask db upgrade` to run the very first database migration

9. run `python3 seed_db.py` to populate the database with data as defined in seed_db.py 

### How to get started (on osx)

1. Install [Python 3](https://www.python.org/downloads/).

2. Clone the [repo](https://github.com/katdob/FlyWithMe.git) by running `git clone https://github.com/katdob/FlyWithMe.git`.

3. run `cd FlyWithMe` to enter the project directory

4. set up the virtual environment by running `python3 -m venv venv` and `source venv/bin/activate` to enter the virtual environment (you can leave the virtual environment with `deactivate`)

5. `python3 -m pip install -r requirements.txt` to install all of the required packages for the project.

6. run `export FLASK_APP=app` in your terminal to tell flask where to find the app

7. run `flask db init` to initialize the database

8. run `flask db upgrade` to run the very first database migration

9. run `python3 seed_db.py` to populate the database with data as defined in seed_db.py


### General Conventions

You must run linters and test before committing your code or QA will wag their finger at you and make you fix it! More details on how to do this coming.

Do not add .pyc files to your commit. You can ask git to ignore certain files by altering the `.gitignore` file.

### Linters & Testing

When you create a Pull Request automatic checks will be run. These checks currently include linters on all code in the project. In the future tests will be run automatically as well.

Your code will need to pass QA before it can be merged into main. 

To run [pylint](https://pylint.org/) on a file, you only need to run `pylint path/to/file`. 

To run a [python unittest](https://docs.python.org/3/library/unittest.html#module-unittest) you only need to run `python3 -m unittest path/to/file --verbose`. The `--verbose` flag gives you more information on the tests that you ran, and is helpful for debugging. 