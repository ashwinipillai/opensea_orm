OpenSea ETL
===================

These are the major functions of OpenSea ETL as a service:

1. Service that allows ETL on demand via api
2. Service that has a command that can be stored as a CRONTAB

## Getting started
---
### Environment Setup

### Step 1: Setup local repository


Clone the repo

```bash
git clone [ENTERREPOLINKHERE]  #TODO: Enter repolink here
```

### Step 2: Setup In your local instead of DOCKER (This is in case docker is not required.)

Install Python 3.9 on your machine.

> Recommended to install [pyenv](https://github.com/pyenv/pyenv) and then install Python 3.9 using pyenv.

#### Linux:

Use your favourite package manager:

Ubuntu:
```bash
sudo apt install python3
```

Fedora:
```bash
sudo dnf install python3
```

RHEL/Centos:
```sh
sudo yum install python3
```

#### Windows:

Recommended to use a package manager like [chocolatey](https://chocolatey.org/) or [winget](https://github.com/microsoft/winget-cli)

OR

Directly [download Python](https://www.python.org/downloads/)

#### Mac

```bash
brew install python
```

>If you are a PyCharm user, run export LC_CTYPE=en_US.UTF-8 to avoid codec errors.
>Add it to your .bash_profile to set it automatically whenever you login


### Step 4: Install dependencies


```bash
pip install -r requirements.txt
```

> Problems installing typed_ast or psycopg2? Get prebuilt binaries from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/).

In case of M1 Mac, [install postgres using homebrew](https://formulae.brew.sh/formula/postgresql)

### Step 5: Running the Django server

#### 5.1 Start Postgres

Prior to running the server, please ensure that you have your postgres server up and running. 

#### 5.2 Create Database opensea_etl  [This needs to be done ONLY  if DB doesn't exist]
Ensure there is a DB called "opensea_etl" created in your local postgres server.
```bash
psql -U your_admin_username -d your_default_database -c "CREATE DATABASE opensea_etl WITH OWNER postgres IF NOT EXISTS;"
```

#### 5.3 Set DB creds  [This needs to be done ONLY  if DB doesn't exist]
* Go to opensea_etl/settings.py
* Update the DATABASES json to your local credentials for postgres.

#### 5.4 Start the server

Run ETL in a Django application.
To run the django server,


ETL API Testing: 
===========


### Trigger the ETL

- Endpoint: `GET /run_etl_with_limit/`
- Param: `Limit = 1 means load 1 record from the api;`
- Response: HTTP 200 for successful run


ETL Setup the CronJob: 
===========

2. **Navigate to Project Directory**: Change to the directory of your Django project.

    ```bash
    cd <project-directory>
    ```

3. **Open the Cron Tab for Editing**: Open the cron tab for the user account under which you want to run the cron job. Use the following command:

    ```bash
    crontab -e
    ```

4. **Add Cron Job Entry**: Add an entry to the cron tab to trigger the ETL process at the desired schedule. For example, to run the ETL process every day at 3:00 AM and load 1 record from the API, add the following line:

    ```bash
    0 3 * * * /path/to/python /path/to/manage.py run_etl_with_limit --limit=1
    ```

    Replace `/path/to/python` with the path to your Python interpreter and `/path/to/manage.py` with the path to your Django project's `manage.py` file.

5. **Save and Exit**: Save the changes and exit the editor.

6. **Verify Cron Job**: Once you've saved the cron job, it will be automatically scheduled to run at the specified time. You can verify it by running:

    ```bash
    crontab -l
    ```

    This command lists all the cron jobs associated with your user account.