from pathlib import Path
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

OUTPUT_FOLDER = Path("outputs/eda")


def open_file(file_path: Path):
    """
    Open a file using the operating system default application.
    """

    if not file_path.exists():
        messagebox.showerror(
            "Missing File",
            f"{file_path.name} was not found."
        )
        return

    try:
        if sys.platform == "darwin":
            subprocess.run(["open", str(file_path)])

        elif sys.platform == "win32":
            subprocess.run(
                ["start", str(file_path)],
                shell=True
            )

        else:
            subprocess.run(["xdg-open", str(file_path)])

    except Exception as error:
        messagebox.showerror(
            "Error",
            f"Could not open file:\n{error}"
        )


def load_dataset():
    """
    Check whether the EDA output folder exists.
    """

    if OUTPUT_FOLDER.exists():

        files = list(OUTPUT_FOLDER.iterdir())

        file_names = [file.name for file in files]

        messagebox.showinfo(
            "Success",
            "EDA output folder found successfully."
        )

        output_label.config(
            text=(
                "EDA folder found.\nFiles: "
                + ", ".join(file_names)
            )
        )

    else:
        messagebox.showerror(
            "Missing Folder",
            "The outputs/eda folder does not exist."
        )


def show_eda_findings():
    """
    Open eda_findings.txt
    """

    open_file(
        OUTPUT_FOLDER / "eda_findings.txt"
    )


def view_class_distribution():
    """
    Open class_distribution.png
    """

    open_file(
        OUTPUT_FOLDER / "class_distribution.png"
    )


def view_sample_images():
    """
    Open sample_images_grid.png
    """

    open_file(
        OUTPUT_FOLDER / "sample_images_grid.png"
    )


# -----------------------------
# GUI SETUP
# -----------------------------

root = tk.Tk()

root.title(
    "Macroinvertebrate Image Analysis System"
)

root.geometry("900x600")

root.configure(bg="#f2f2f2")


title_label = tk.Label(
    root,
    text="Macroinvertebrate Image Analysis System",
    font=("Arial", 24, "bold"),
    bg="#f2f2f2"
)

title_label.pack(pady=30)


description_label = tk.Label(
    root,
    text=(
        "Use the buttons below to explore "
        "the macroinvertebrate dataset."
    ),
    font=("Arial", 14),
    bg="#f2f2f2"
)

description_label.pack(pady=10)


button_width = 40


load_button = tk.Button(
    root,
    text="Load Dataset",
    width=button_width,
    height=2,
    command=load_dataset
)

load_button.pack(pady=10)


eda_button = tk.Button(
    root,
    text="Show EDA Findings",
    width=button_width,
    height=2,
    command=show_eda_findings
)

eda_button.pack(pady=10)


chart_button = tk.Button(
    root,
    text="View Class Distribution Chart",
    width=button_width,
    height=2,
    command=view_class_distribution
)

chart_button.pack(pady=10)


sample_button = tk.Button(
    root,
    text="View Sample Images",
    width=button_width,
    height=2,
    command=view_sample_images
)

sample_button.pack(pady=10)


exit_button = tk.Button(
    root,
    text="Exit",
    width=button_width,
    height=2,
    command=root.destroy
)

exit_button.pack(pady=10)


output_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#f2f2f2",
    wraplength=800,
    justify="center"
)

output_label.pack(pady=30)


root.mainloop()
