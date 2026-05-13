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

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Load Dataset", width=25, command=self.load_dataset).pack(pady=5)
        tk.Button(button_frame, text="Show Dataset Summary", width=25, command=self.show_summary).pack(pady=5)
        tk.Button(button_frame, text="View Charts", width=25, command=self.view_charts).pack(pady=5)
        tk.Button(button_frame, text="View Sample Images", width=25, command=self.view_sample_images).pack(pady=5)
        tk.Button(button_frame, text="Exit", width=25, command=self.root.quit).pack(pady=5)

        self.output_label = tk.Label(
            self.root,
            text="Select an option to begin.",
            font=("Arial", 12)
        )
        self.output_label.pack(pady=30)

    def load_dataset(self):
        self.output_label.config(text="Dataset loading feature will connect to Person A's code.")

    def show_summary(self):
        self.output_label.config(text="Dataset summary feature will connect to EDA analysis.")

    def view_charts(self):
        self.output_label.config(text="Chart viewing feature will display saved EDA charts.")

    def view_sample_images(self):
        self.output_label.config(text="Sample image viewer will display macroinvertebrate images.")


if __name__ == "__main__":
    root = tk.Tk()
    app = MacroinvertebrateGUI(root)
    root.mainloop()
