from faker import Faker

faker = Faker()


def random_valid_dns_name() -> str:
    return faker.domain_word()


def random_valid_dns_ttl() -> int:
    return faker.random_int(min=1, max=604800)
