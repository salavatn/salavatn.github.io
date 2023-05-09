'''
# DotEnv Library

Overview
--------
* [What is DotEnv?](#what-is-dotenv)
* [How to install](#how-to-install)
* [Step-by-step guide](#step-by-step-guide)
* [Project Architecture](#project-architecture)


## What is DotEnv?
> DotEnv is a Python library that allows you to read key-value pairs from a `.env` file and set them as environment variables.


## How to install
```sh
pip install python-dotenv
```



## Step-by-step guide

* 1.Create a new file (by default name is `.env`) in your project directory and add the following lines:

```sh
touch .env
```

* 2. Open the `.env` file in a text editor and add the following lines:

```log
MySQL_ADDR="172.30.0.100"
MySQL_USER="root"
MySQL_PSWD="Pa$$_123!"
```

* 3. Install the `python-dotenv` library using the following command:
```sh
pip install python-dotenv
```

* 4. Create a new file called `main.py` in your project directory and add the following code:
```python
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

ipaddress = os.getenv("MySQL_ADDR")
username  = os.getenv("MySQL_USER")
password  = os.getenv("MySQL_PSWD")

print(f"MySQL IP address: {ipaddress}")
print(f"MySQL Username:   {username}")
print(f"MySQL Password:   {password}")
```

**Result:**
```
MySQL IP address:  172.30.0.100
MySQL Username:    root
MySQL Password:    Pa$$_123!
```

## Project Architecture
```
PROJECT
    ├── .env
    ├── main.py
    └── README.md
```


'''