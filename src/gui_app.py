import tkinter as tk
from tkinter import messagebox


class MacroinvertebrateGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Macroinvertebrate Image Analysis System")
        self.root.geometry("900x600")

        self.create_layout()

    def create_layout(self):
        title = tk.Label(
            self.root,
            text="Macroinvertebrate Image Analysis System",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=20)

        instruction = tk.Label(
            self.root,
            text="Use the buttons below to explore the macroinvertebrate dataset.",
            font=("Arial", 12)
        )
        instruction.pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        tk.Button(
            button_frame,
            text="Load Dataset",
            width=30,
            command=self.load_dataset
        ).pack(pady=5)

        tk.Button(
            button_frame,
            text="Show Dataset Summary",
            width=30,
            command=self.show_summary
        ).pack(pady=5)

        tk.Button(
            button_frame,
            text="View Charts",
            width=30,
            command=self.view_charts
        ).pack(pady=5)

        tk.Button(
            button_frame,
            text="View Sample Images",
            width=30,
            command=self.view_sample_images
        ).pack(pady=5)

        tk.Button(
            button_frame,
            text="Exit",
            width=30,
            command=self.root.quit
        ).pack(pady=5)

        self.output_label = tk.Label(
            self.root,
            text="Status: Waiting for user action.",
            font=("Arial", 12)
        )
        self.output_label.pack(pady=30)

    def load_dataset(self):
        self.output_label.config(
            text="Status: Dataset loaded successfully."
        )

        messagebox.showinfo(
            "Dataset",
            "Dataset loading simulation completed."
        )

    def show_summary(self):
        self.output_label.config(
            text="Status: Dataset summary will display EDA results."
        )

    def view_charts(self):
        self.output_label.config(
            text="Status: Charts will display saved visualisations."
        )

    def view_sample_images(self):
        self.output_label.config(
            text="Status: Sample images will display from the dataset."
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = MacroinvertebrateGUI(root)
    root.mainloop()
