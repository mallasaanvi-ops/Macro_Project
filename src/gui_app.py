import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class MacroinvertebrateGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Macroinvertebrate Image Analysis System")
        self.root.geometry("1000x750")

        self.output_folder = os.path.join("outputs", "eda")
        self.current_image = None

        self.create_layout()

    def create_layout(self):
        tk.Label(
            self.root,
            text="Macroinvertebrate Image Analysis System",
            font=("Arial", 18, "bold")
        ).pack(pady=15)

        tk.Label(
            self.root,
            text="Use the buttons below to explore the macroinvertebrate dataset.",
            font=("Arial", 12)
        ).pack(pady=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=15)

        tk.Button(button_frame, text="Load Dataset", width=35, command=self.load_dataset).pack(pady=5)
        tk.Button(button_frame, text="Show EDA Findings", width=35, command=self.show_findings).pack(pady=5)
        tk.Button(button_frame, text="View Class Distribution Chart", width=35, command=self.view_class_chart).pack(pady=5)
        tk.Button(button_frame, text="View Sample Images", width=35, command=self.view_sample_images).pack(pady=5)
        tk.Button(button_frame, text="Exit", width=35, command=self.root.quit).pack(pady=5)

        self.output_label = tk.Label(
            self.root,
            text="Status: Waiting for user action.",
            font=("Arial", 12),
            wraplength=900,
            justify="center"
        )
        self.output_label.pack(pady=15)

        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

    def find_file(self, possible_names):
        for name in possible_names:
            path = os.path.join(self.output_folder, name)
            if os.path.exists(path):
                return path
        return None

    def load_dataset(self):
        if os.path.exists(self.output_folder):
            files = os.listdir(self.output_folder)
            self.clear_image()
            self.output_label.config(
                text="EDA output folder found. Files available: " + ", ".join(files)
            )
            messagebox.showinfo("Dataset", "EDA output folder found successfully.")
        else:
            self.output_label.config(text="outputs/eda folder was not found.")
            messagebox.showerror("Missing Folder", "The outputs/eda folder was not found.")

    def show_findings(self):
        findings_path = self.find_file([
            "eda_findings.txt",
            "dataset_summary.txt",
            "summary.txt"
        ])

        if findings_path is None:
            self.clear_image()
            self.output_label.config(
                text="No findings text file found in outputs/eda."
            )
            return

        with open(findings_path, "r", encoding="utf-8") as file:
            findings = file.read()

        self.clear_image()
        self.output_label.config(text=findings)

    def view_class_chart(self):
        chart_path = self.find_file([
            "class_distribution.png",
            "top_10_classes.png"
        ])

        if chart_path is None:
            self.clear_image()
            self.output_label.config(
                text="No class distribution chart found in outputs/eda."
            )
            return

        self.display_image(chart_path, "Class distribution chart")

    def view_sample_images(self):
        sample_path = self.find_file([
            "sample_images_grid.png",
            "sample_images.png"
        ])

        if sample_path is None:
            self.clear_image()
            self.output_label.config(
                text="No sample image grid found in outputs/eda."
            )
            return

        self.display_image(sample_path, "Sample macroinvertebrate images")

    def display_image(self, image_path, image_name):
        image = Image.open(image_path)
        image.thumbnail((850, 450))

        self.current_image = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.current_image)

        self.output_label.config(text=f"Displaying: {image_name}")

    def clear_image(self):
        self.image_label.config(image="")
        self.current_image = None


if __name__ == "__main__":
    root = tk.Tk()
    app = MacroinvertebrateGUI(root)
    root.mainloop()
