from faker import Faker

fake = Faker("ru_RU")
print(fake.name_female())
print(fake.prefix_female())
print(fake.hostname())
