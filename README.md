# FD Crawling PoC Project
[Project Description Here] 

# Requirement
- python >= 3.12.4
- CPU >= 4 Core
- Memory >= 8 GB

# Installation
```bash
$ git clone https://github.com/de-eng-de-eng/FD_Crawling_PoC.git
$ python -m pip install pipenv # install pipenv package
$ pipenv install # install library for crawling with Pipfile
or
$ pipenv install --dev # install library for crawling with Pipfile Dev Environment
```
## Installation on air-gapped env for Streamlit Application with venv
```bash
$ python -v venv fd_crawling_venv
$ source ./fd_crawling_venv/bin/activate
$ pip install --no-index --find-index=wheelhouse -r requirements_for_app.txt
```


# Crawling Code
## Run Crawling ()
```bash
Instructions for running code
```

## Test Code
```bash
$ pipenv shell # Spawns a shell within the virtualenv
$ (FD_Crawling_PoC) $ python ./test.py # check result csv on data directory
```

# Run Application with Streamlit
## On Local machine with Network
```bash
$ pipenv shell # Spawns a shell within the virtualenv
$ (FD_Crawling_PoC) $ streamlit run application/app.py # Access URL: http://localhost:8501
```
## On Workstation without Network
```bash
$ source ./fd_crawling_venv/bin/activate
$ (fd_crawling_venv) $ streamlit run application/app.py --server.port 30100 # Access URL: http://<server_ip>:30100
```
