import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class MacroinvertebrateGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Macroinvertebrate Image Analysis System")
        self.root.geometry("950x700")

        self.output_folder = os.path.join("outputs", "eda")
        self.image_label = None
        self.current_image = None

        self.create_layout()

    def create_layout(self):
        title = tk.Label(
            self.root,
            text="Macroinvertebrate Image Analysis System",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=15)

        instruction = tk.Label(
            self.root,
            text="Use the buttons below to explore the macroinvertebrate dataset.",
            font=("Arial", 12)
        )
        instruction.pack(pady=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=15)

        tk.Button(button_frame, text="Load Dataset", width=35, command=self.load_dataset).pack(pady=5)
        tk.Button(button_frame, text="Show EDA Findings", width=35, command=self.show_summary).pack(pady=5)
        tk.Button(button_frame, text="View Class Distribution Chart", width=35, command=self.view_class_chart).pack(pady=5)
        tk.Button(button_frame, text="View Sample Images", width=35, command=self.view_sample_images).pack(pady=5)
        tk.Button(button_frame, text="Exit", width=35, command=self.root.quit).pack(pady=5)

        self.output_label = tk.Label(
            self.root,
            text="Status: Waiting for user action.",
            font=("Arial", 12),
            wraplength=850,
            justify="center"
        )
        self.output_label.pack(pady=15)

        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

    def load_dataset(self):
        if os.path.exists(self.output_folder):
            self.output_label.config(text="Status: EDA output folder found successfully.")
            messagebox.showinfo("Dataset", "EDA output folder found successfully.")
        else:
            self.output_label.config(text="Status: outputs/eda folder was not found.")
            messagebox.showerror("Missing Folder", "The outputs/eda folder was not found.")

    def show_summary(self):
        summary_path = os.path.join(self.output_folder, "eda_findings.txt")

        if os.path.exists(summary_path):
            with open(summary_path, "r") as file:
                summary = file.read()

            self.clear_image()
            self.output_label.config(text=summary)
        else:
            self.output_label.config(
                text="EDA findings file not found. Expected file: outputs/eda/eda_findings.txt"
            )

    def view_class_chart(self):
        chart_path = os.path.join(self.output_folder, "class_distribution.png")
        self.display_image(chart_path, "Class distribution chart")

    def view_sample_images(self):
        sample_path = os.path.join(self.output_folder, "sample_images_grid.png")
        self.display_image(sample_path, "Sample macroinvertebrate images")

    def display_image(self, image_path, image_name):
        if not os.path.exists(image_path):
            self.output_label.config(
                text=f"{image_name} not found. Expected file: {image_path}"
            )
            return

        image = Image.open(image_path)
        image.thumbnail((800, 420))

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
