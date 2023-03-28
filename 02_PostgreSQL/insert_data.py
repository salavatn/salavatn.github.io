# INSERT INTO JOB(TITLE, COMPANY_ID) VALUES ('Software Engineer', 1);
import random
import faker

fake = faker.Faker()

count = 1
while count <= 100:
    company_ids = random.randint(1, 10)
    print(f"INSERT INTO JOB(TITLE, COMPANY_ID) VALUES ('{fake.job()}', {company_ids});")
    count += 1

