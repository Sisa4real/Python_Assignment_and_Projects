# =========================
# MODULE: RANDOM, STRING
# =========================
import random
import string

# 1️⃣ Generate a random 6-character user ID
def random_user_id():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

# Example
print("Random User ID:", random_user_id())

# 2️⃣ User-defined random ID generator
def user_id_gen_by_user():
    # Take inputs
    num_chars = int(input("Enter number of characters for each ID: "))
    num_ids = int(input("Enter number of IDs to generate: "))
    ids = []
    chars = string.ascii_letters + string.digits
    for _ in range(num_ids):
        ids.append(''.join(random.choice(chars) for _ in range(num_chars)))
    return ids

# Example
# print(user_id_gen_by_user())


# 3️⃣ Generate a random RGB color
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

# Example
print("Random RGB Color:", rgb_color_gen())


# =========================
# LEVEL 2: Generate colors
# =========================

# 4️⃣ Generate list of hexadecimal colors
def list_of_hexa_colors(n=1):
    colors = []
    for _ in range(n):
        hex_color = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
        colors.append(hex_color)
    return colors

# 5️⃣ Generate list of RGB colors
def list_of_rgb_colors(n=1):
    return [rgb_color_gen() for _ in range(n)]

# 6️⃣ General function to generate colors
def generate_colors(color_type='hexa', n=1):
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(n)
    else:
        raise ValueError("color_type must be 'hexa' or 'rgb'")

# Example usage
print("Generate 3 hexa colors:", generate_colors('hexa', 3))
print("Generate 1 hexa color:", generate_colors('hexa', 1))
print("Generate 3 RGB colors:", generate_colors('rgb', 3))
print("Generate 1 RGB color:", generate_colors('rgb', 1))


# =========================
# LEVEL 3: List operations & random numbers
# =========================

# 7️⃣ Shuffle a list
def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled

# Example
example_list = [1,2,3,4,5]
print("Original list:", example_list)
print("Shuffled list:", shuffle_list(example_list))


# 8️⃣ Generate 7 unique random numbers in range 0-9
def seven_unique_numbers():
    return random.sample(range(10), 7)

# Example
print("Seven unique random numbers:", seven_unique_numbers())


# =========================
# VIRTUAL ENVIRONMENT (Concept)
# =========================
"""
Steps to create and activate a virtual environment:

1. Navigate to your project directory:
   $ cd path/to/project

2. Create a virtual environment:
   $ python -m venv .venv

3. Activate the virtual environment:
   Windows (PowerShell):  .\.venv\Scripts\Activate.ps1
   Windows (CMD):        .\.venv\Scripts\activate.bat
   Mac/Linux:            source .venv/bin/activate

4. Install dependencies:
   (.venv) $ pip install numpy pandas matplotlib seaborn requests

5. Deactivate when done:
   (.venv) $ deactivate
"""
