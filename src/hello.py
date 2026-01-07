from pathlib import Path

output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

with open(output_dir / "hello.txt", "w") as f:
    f.write("Hello ran successfully.")

print("Hello initialized successfully.")