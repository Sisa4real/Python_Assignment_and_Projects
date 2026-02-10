# =========================
# LEVEL 1: Statistics Class
# =========================
from collections import Counter
import math

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def mode(self):
        counter = Counter(self.data)
        max_count = max(counter.values())
        mode_values = [k for k, v in counter.items() if v == max_count]
        return (mode_values[0], max_count)

    def var(self):
        mean_val = self.mean()
        return sum((x - mean_val) ** 2 for x in self.data) / self.count()

    def std(self):
        return math.sqrt(self.var())

    def freq_dist(self):
        counter = Counter(self.data)
        total_count = self.count()
        freq_list = [(round(v / total_count * 100, 1), k) for k, v in counter.items()]
        # Sort by frequency descending
        return sorted(freq_list, reverse=True)

    def describe(self):
        return {
            "Count": self.count(),
            "Sum": self.sum(),
            "Min": self.min(),
            "Max": self.max(),
            "Range": self.range(),
            "Mean": self.mean(),
            "Median": self.median(),
            "Mode": self.mode(),
            "Variance": self.var(),
            "Standard Deviation": self.std(),
            "Frequency Distribution": self.freq_dist()
        }

# Example usage:
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print("Count:", data.count())
print("Sum:", data.sum())
print("Min:", data.min())
print("Max:", data.max())
print("Range:", data.range())
print("Mean:", data.mean())
print("Median:", data.median())
print("Mode:", data.mode())
print("Variance:", data.var())
print("Standard Deviation:", data.std())
print("Frequency Distribution:", data.freq_dist())
print("Full Description:", data.describe())


# =========================
# LEVEL 2: PersonAccount Class
# =========================
class PersonAccount:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.incomes = []   # list of tuples (amount, description)
        self.expenses = []  # list of tuples (amount, description)

    def total_income(self):
        return sum(amount for amount, desc in self.incomes)

    def total_expense(self):
        return sum(amount for amount, desc in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def add_income(self, amount, description=""):
        self.incomes.append((amount, description))

    def add_expense(self, amount, description=""):
        self.expenses.append((amount, description))

    def account_info(self):
        info = f"Account holder: {self.first_name} {self.last_name}\n"
        info += f"Total Income: {self.total_income()}\n"
        info += f"Total Expense: {self.total_expense()}\n"
        info += f"Account Balance: {self.account_balance()}\n"
        return info

# Example usage:
person = PersonAccount("John", "Doe")
person.add_income(5000, "Salary")
person.add_income(200, "Freelance")
person.add_expense(1500, "Rent")
person.add_expense(300, "Groceries")

print("\nPerson Account Info:\n", person.account_info())
