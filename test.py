import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random numbers from uniform distribution (0 to 1)
data = np.random.uniform(0, 1, 1000)

# Plot histogram
plt.figure()
plt.hist(data, bins=30)

# Labels and title
plt.title("Uniform Distribution (1000 Random Numbers)")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Show plot
plt.show()