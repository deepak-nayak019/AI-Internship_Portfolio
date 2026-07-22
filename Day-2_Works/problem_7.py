# Dataset Class

class Dataset:
    # Constructor
    def __init__(self, numbers):
        self.numbers = numbers

    # Calculate Mean
    def mean(self):
        return sum(self.numbers) / len(self.numbers)

    # Find Maximum Value
    def max(self):
        return max(self.numbers)

    # Find Minimum Value
    def min(self):
        return min(self.numbers)

    # Print Summary
    def summary(self):
        print("------ Dataset Summary ------")
        print("Data       :", self.numbers)
        print("Mean       :", self.mean())
        print("Maximum    :", self.max())
        print("Minimum    :", self.min())


# -----------------------------
# Create Dataset Objects
# -----------------------------

dataset1 = Dataset([10, 20, 30, 40, 50])
dataset2 = Dataset([15, 8, 42, 60, 25, 18])

# -----------------------------
# Display Summary
# -----------------------------

print("Dataset 1")
dataset1.summary()

print("\nDataset 2")
dataset2.summary()