import os
import tkinter as tk
from tkinter import filedialog

def generate_java_files(nodes, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for node in nodes:
        filename = os.path.join(output_dir, f"{node}.java")
        with open(filename, 'w') as file:
            file.write(f"public class {node} {{\n")
            file.write("    // Add properties and methods relevant to {node} here\n\n")
            file.write("    public void exampleMethod() {\n")
            file.write("        // Implementation here\n")
            file.write("    }\n")
            file.write("}\n")

    print(f"Java files generated in {output_dir}")

def browse_directory():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        output_dir.set(folder_selected)

def generate_files():
    nodes = node_names.get().split(',')
    output_dir_path = output_dir.get()
    generate_java_files(nodes, output_dir_path)

app = tk.Tk()
app.title('Java File Generator')

tk.Label(app, text="Node Names (comma-separated):").pack()
node_names = tk.Entry(app)
node_names.pack()

tk.Label(app, text="Output Directory:").pack()
output_dir = tk.StringVar()
tk.Entry(app, textvariable=output_dir).pack()
tk.Button(app, text="Browse", command=browse_directory).pack()

tk.Button(app, text="Generate Files", command=generate_files).pack()

app.mainloop()
