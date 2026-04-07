import subprocess, time

files = [f"data/file{i}.in" for i in range(1, 11)]
sizes = [25, 50, 100, 200, 300, 400, 500, 600, 800, 1000]
results = []

for file, size in zip(files, sizes):
    with open(file, "r") as f:
        data = f.read()

    start = time.perf_counter()
    proc = subprocess.run(
        ["python", "main.py"],
        input=data,
        capture_output=True,
        text=True
    )
    end = time.perf_counter()

    elapsed_ms = (end - start) * 1000
    results.append((size, elapsed_ms))
    print(f"n={size}: {elapsed_ms / 1000:.4f} s")

with open("data/runtime_results.txt", "w") as f:
    f.write("size,ms\n")
    for size, ms in results:
        f.write(f"{size},{ms:.4f}\n")