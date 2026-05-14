from pathlib import Path
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

OUTPUT_FOLDER = Path("outputs/eda")


class MacroinvertebrateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Macroinvertebrate Image Analysis System")
        self.root.geometry("1100x750")
        self.root.configure(bg="#f2f2f2")

        self.current_image = None

        title_label = tk.Label(
            root,
            text="Macroinvertebrate Image Analysis System",
            font=("Arial", 24, "bold"),
            bg="#f2f2f2"
        )
        title_label.pack(pady=20)

        description_label = tk.Label(
            root,
            text="Use the buttons below to explore the macroinvertebrate dataset.",
            font=("Arial", 14),
            bg="#f2f2f2"
        )
        description_label.pack(pady=5)

        button_frame = tk.Frame(root, bg="#f2f2f2")
        button_frame.pack(pady=15)

        tk.Button(
            button_frame,
            text="Load Dataset",
            width=28,
            height=2,
            command=self.load_dataset
        ).grid(row=0, column=0, padx=8, pady=5)

        tk.Button(
            button_frame,
            text="Show EDA Findings",
            width=28,
            height=2,
            command=self.show_eda_findings
        ).grid(row=0, column=1, padx=8, pady=5)

        tk.Button(
            button_frame,
            text="View Class Distribution Chart",
            width=28,
            height=2,
            command=lambda: self.show_image("class_distribution.png")
        ).grid(row=1, column=0, padx=8, pady=5)

        tk.Button(
            button_frame,
            text="View Sample Images",
            width=28,
            height=2,
            command=lambda: self.show_image("sample_images_grid.png")
        ).grid(row=1, column=1, padx=8, pady=5)

        tk.Button(
            button_frame,
            text="Exit",
            width=28,
            height=2,
            command=root.destroy
        ).grid(row=2, column=0, columnspan=2, pady=5)

        self.output_text = tk.Text(
            root,
            height=8,
            width=120,
            wrap="word",
            font=("Arial", 11)
        )
        self.output_text.pack(pady=10)

        self.image_label = tk.Label(root, bg="#f2f2f2")
        self.image_label.pack(pady=10)

    def clear_display(self):
        self.output_text.delete("1.0", tk.END)
        self.image_label.config(image="")
        self.current_image = None

    def load_dataset(self):
        self.clear_display()

        if not OUTPUT_FOLDER.exists():
            messagebox.showerror(
                "Missing Folder",
                "The outputs/eda folder does not exist. Run main.py first."
            )
            return

        files = sorted([file.name for file in OUTPUT_FOLDER.iterdir()])

        self.output_text.insert(
            tk.END,
            "EDA output folder found successfully.\n\nFiles found:\n"
        )

        for file_name in files:
            self.output_text.insert(tk.END, f"- {file_name}\n")

    def show_eda_findings(self):
        self.clear_display()

        findings_path = OUTPUT_FOLDER / "eda_findings.txt"

        if not findings_path.exists():
            messagebox.showerror(
                "Missing File",
                "eda_findings.txt was not found. Run main.py first."
            )
            return

        with open(findings_path, "r", encoding="utf-8") as file:
            findings = file.read()

        self.output_text.insert(tk.END, findings)

    def show_image(self, image_name):
        self.clear_display()

        image_path = OUTPUT_FOLDER / image_name

        if not image_path.exists():
            messagebox.showerror(
                "Missing File",
                f"{image_name} was not found. Run main.py first."
            )
            return

        image = Image.open(image_path)

        max_width = 950
        max_height = 430

        image.thumbnail((max_width, max_height))

        self.current_image = ImageTk.PhotoImage(image)

        self.image_label.config(image=self.current_image)

        self.output_text.insert(
            tk.END,
            f"Displaying: {image_name}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = MacroinvertebrateApp(root)
    root.mainloop()
