from Algorithm.passwordGenerator.password_generator import PasswordGenerator

if __name__ == "__main__":
    generator = PasswordGenerator()
    password_set = generator.execute_algorithm()
    print(password_set)
