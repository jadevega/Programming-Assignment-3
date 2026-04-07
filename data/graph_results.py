import matplotlib.pyplot as plt

sizes, times = [], []
with open("data/runtime_results.txt") as f:
    next(f)
    for line in f:
        s, t = line.strip().split(",")
        sizes.append(int(s))
        times.append(float(t) / 1000)

plt.figure(figsize=(8, 5))
plt.plot(sizes, times, marker='o', color='black', linewidth=2)
plt.xlabel("Input Size (n = m)")
plt.ylabel("Runtime in seconds")
plt.title("HVLCS Runtime vs Input Size")
plt.grid(True)
plt.tight_layout()
plt.savefig("data/runtime_graph.png")
plt.show()