from random import choice, randint
import string

first_names = ["Aren", "Arez", "Arman", "Bryan", "Bryce", "Bryden",
         "Darn", "Darrach", "Darragh", "Darrel", "Dan", "Darren",
         "Taliesin", "Talon", "Talorcan", "Tamar", "Tamiem", "Tammam",
         "Zubayr", "Zuriel"]

last_names = ['Abbott', 'Acevedo', 'Acosta', 'Adams', 'Adkins', 'Aguilar', 'Black', 'Blackburn', 'Blackwell', 'Blair',
              'Blake', 'Blanchard', 'Blankenship', 'Blevins',  'Fox', 'Francis', 'Franco', 'Frank', 'Franklin',
              'Franks']

courses = ['math', 'biology', 'english', 'chemistry', 'football', 'basketball', 'astronomy', 'geometry', 'algebra']


def create_random_groups(number=10):
        letters = string.ascii_lowercase
        groups = []
        for i in range(number):
                groups.append(f'{choice(letters)}{choice(letters)}-{randint(10, 99)}')
        return groups


groups = create_random_groups()

course_description = ['Good course', 'Easy course', 'Hard course', 'Very hard course']
