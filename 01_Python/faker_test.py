from faker import Faker

fake = Faker()

print(fake.chrome()) # Mozilla/5.0 (Linux; Android 4.2) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/26.0.898.0 Safari/534.1
print(fake.city())  # Williamston
print(fake.color()) # #39ddd8
print(fake.company())   # Powell Ltd
print(fake.credit_card_number()) # 4773904006800585
print(fake.date())  # 1996-06-10
print(fake.date_time()) # 1993-02-01 19:19:14
print(fake.emoji())     # 🧑‍🚀
print(fake.first_name())    # Christine
print(fake.free_email())  # sullivanamanda@gmail.com
print(fake.ipv4())  # 103.19.125.13
print(fake.ipv4_private())  # 172.26.238.74
print(fake.ipv4_public())   # 148.21.52.81
print(fake.last_name()) # Monroe
print(fake.name())  # Katherine Richardson
print(fake.password()) # +xV0yTHrA*