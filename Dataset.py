import os

# 1 & #2. Variables & File Handling, & Error handling 

def read_numeric_file(filename):
    data = []
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError("File does not exist.")

        with open(filename, "r") as f:
            lines = f.readlines()

        if not lines:
            raise ValueError("File is empty.")

        for line in lines:
            try:
                value = float(line.strip())
                data.append(value)
            except ValueError:
                raise ValueError("File contains invalid (non-numeric) values.")

        return data

    except FileNotFoundError as e:
        print("Error:", e)
        return []
    except ValueError as e:
        print("Error:", e)
        return []


def read_categorical_file(filename):
    categories = set()
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError("File does not exist.")

        with open(filename, "r") as f:
            lines = f.readlines()

        if not lines:
            raise ValueError("File is empty.")

        for line in lines:
            categories.add(line.strip())

        return categories

    except FileNotFoundError as e:
        print("Error:", e)
        return set()
    except ValueError as e:
        print("Error:", e)
        return set()


#3 #4 #5 #6. Functions, Operators & Loops, Conditional Statements, Sets

def calculate_total(data):
    total = 0
    for value in data:
        total += value
    return total

def calculate_average(data):
    if len(data) == 0:
        return 0
    return calculate_total(data) / len(data)

def calculate_minimum(data):
    if len(data) == 0:
        return None
    minimum = data[0]
    for value in data:
        if value < minimum:
            minimum = value
    return minimum

def calculate_maximum(data):
    if len(data) == 0:
        return None
    maximum = data[0]
    for value in data:
        if value > maximum:
            maximum = value
    return maximum


# 7. Object-Oriented Programming

class DataSet:
    def __init__(self, numeric_file, categorical_file, threshold=50):
        self.numeric_file = numeric_file
        self.categorical_file = categorical_file
        self.data = []
        self.categories = set()
        self.threshold = threshold
        self.statistics = {}

    def load_data(self):
        self.data = read_numeric_file(self.numeric_file)
        self.categories = read_categorical_file(self.categorical_file)

    def calculate_statistics(self):
        if not self.data:
            self.statistics = {}
            return

        total = calculate_total(self.data)
        avg = calculate_average(self.data)
        minimum = calculate_minimum(self.data)
        maximum = calculate_maximum(self.data)

        performance = "High Performance" if avg > self.threshold else "Needs Improvement"

        self.statistics = {
            "Total": total,
            "Average": avg,
            "Minimum": minimum,
            "Maximum": maximum,
            "Performance": performance,
            "Unique Categories": len(self.categories)
        }

    def display_results(self):
        if not self.statistics:
            print("No statistics available.")
            return
        print("\n--- Analysis Report ---")
        for key, value in self.statistics.items():
            print(f"{key}: {value}")

    def save_results(self, report_file="report.txt"):
        try:
            with open(report_file, "w") as f:
                f.write("--- Analysis Report ---\n")
                for key, value in self.statistics.items():
                    f.write(f"{key}: {value}\n")
            print(f"\nReport saved successfully to {report_file}")
        except Exception as e:
            print("Error saving report:", e)


# 8. Main Program Execution

if __name__ == "__main__":
    numeric_file = "numeric_data.csv"      # file with numbers
    categorical_file = "categories.txt"    # file with categories

    dataset = DataSet(numeric_file, categorical_file, threshold=60)
    dataset.load_data()
    dataset.calculate_statistics()
    dataset.display_results()
    dataset.save_results("analysis_report.txt")