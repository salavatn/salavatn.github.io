from faker import Faker

fake = Faker()

def search_fake(keyword):
    for attribute in dir(fake):
        if keyword in attribute:
            print(attribute)

search = "country"
search_fake(search)


'''
# Faker Library

Overview
--------
* [What is DotEnv?](#what-is-dotenv)
* [How to install](#how-to-install)
* [Step-by-step guide](#step-by-step-guide)
* [Project Architecture](#project-architecture)

> The Faker library in Python is a tool for generating fake data such as names, addresses, phone numbers, and more. Here are some steps to use Faker library in Python:


## How to use

### Install the Faker library using pip:
```sh
pip install Faker
```

### Simple example
```python
from faker import Faker

fake = Faker()

name  = fake.name()
email = fake.email()
city  = fake.city()

print(f"Hello {name}, your email is {email} and you live in {city}")
```

**Result:**
```
Hello John Cohen, your email is michael82@example.com and you live in Lanemouth

Hello William Ellis, your email is lpollard@example.com and you live in South Connie

Hello Garrett Jones, your email is smithryan@example.com and you live in Morrowton
```

## Search available fake keywords:
> To search for available Faker methods related to a specific keyword, define a function that iterates through the available attributes of the Faker instance and prints the ones that contain the keyword:

```python
from faker import Faker

fake = Faker()

def search_fake(keyword):
    for attribute in dir(fake):
        if keyword in attribute:
            print(attribute)

search = "country"
search_fake(search)
```

**Result:**
```
country
country_calling_code
country_code
country_code_long
country_name
country_object
country_of_birth
country_of_residence
```
## Popular examples:
```python
from faker import Faker

fake = Faker()

print(fake.city())          # Williamston
print(fake.color())         # #39ddd8
print(fake.company())       # Powell Ltd
print(fake.credit_card_number()) # 4773904006800585
print(fake.date())          # 1996-06-10
print(fake.date_time())     # 1993-02-01 19:19:14
print(fake.emoji())         # 🧑‍🚀
print(fake.first_name())    # Christine
print(fake.free_email())    # sullivanamanda@gmail.com
print(fake.ipv4())          # 103.19.125.13
print(fake.ipv4_private())  # 172.26.238.74
print(fake.ipv4_public())   # 148.21.52.81
print(fake.last_name())     # Monroe
print(fake.name())          # Katherine Richardson
print(fake.password())      # +xV0yTHrA*
```

## Project Architecture
```
PROJECT
    ├── .env
    ├── main.py
    └── README.md
```


'''