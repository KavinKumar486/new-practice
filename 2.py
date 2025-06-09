import random
import string

def generate_random_string(length=8):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def create_user_list(num_users=10):
    """Create a list of users with random names and ages."""
    users = []
    for _ in range(num_users):
        name = generate_random_string(random.randint(5, 10))
        age = random.randint(18, 60)
        users.append({'name': name, 'age': age})
    return users

def filter_adults(users):
    """Filter users who are 21 or older."""
    return [user for user in users if user['age'] >= 21]

def sort_users_by_age(users):
    """Sort users by age."""
    return sorted(users, key=lambda x: x['age'])

def print_users(users):
    """Print user details."""
    for user in users:
        print(f"Name: {user['name']}, Age: {user['age']}")

if __name__ == "__main__":
    users = create_user_list(15)
    print("All Users:")
    print_users(users)
    adults = filter_adults(users)
    print("\nAdults (21+):")
    print_users(sort_users_by_age(adults))
print("\nSorted Users by Age:")
print(''.join(f"{user['name']} ({user['age']})" for user in sort_users_by_age(users)))