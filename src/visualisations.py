from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class Visualisations:
    def __init__(self, dataframe: pd.DataFrame, output_folder: str | Path):
        self.dataframe = dataframe
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(parents=True, exist_ok=True)

    def save_class_distribution_chart(self):
        plt.figure(figsize=(14, 7))

        class_order = self.dataframe["label"].value_counts().index

        sns.countplot(
            data=self.dataframe,
            x="label",
            order=class_order
        )

        plt.title("Number of Macroinvertebrate Images per Class")
        plt.xlabel("Macroinvertebrate Class")
        plt.ylabel("Number of Images")
        plt.xticks(rotation=90)
        plt.tight_layout()

        output_path = self.output_folder / "class_distribution.png"
        plt.savefig(output_path)
        plt.close()

        print(f"Saved chart: {output_path}")

    def save_top_classes_chart(self, top_n=10):
        top_classes = self.dataframe["label"].value_counts().head(top_n)

        plt.figure(figsize=(10, 6))

        sns.barplot(
            x=top_classes.values,
            y=top_classes.index
        )

        plt.title(f"Top {top_n} Macroinvertebrate Classes by Image Count")
        plt.xlabel("Number of Images")
        plt.ylabel("Class Label")
        plt.tight_layout()

        output_path = self.output_folder / "top_10_classes.png"
        plt.savefig(output_path)
        plt.close()

        print(f"Saved chart: {output_path}")

    def save_image_size_distribution(self):
        plt.figure(figsize=(10, 6))

        plt.hist(
            self.dataframe["width"],
            bins=20,
            alpha=0.7,
            label="Width"
        )

        plt.hist(
            self.dataframe["height"],
            bins=20,
            alpha=0.7,
            label="Height"
        )

        plt.title("Image Width and Height Distribution")
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")
        plt.legend()
        plt.tight_layout()

        output_path = self.output_folder / "image_size_distribution.png"
        plt.savefig(output_path)
        plt.close()

        print(f"Saved chart: {output_path}")

    def save_width_height_scatterplot(self):
        plt.figure(figsize=(8, 6))

        sns.scatterplot(
            data=self.dataframe,
            x="width",
            y="height",
            hue="label",
            legend=False
        )

        plt.title("Image Width Compared with Image Height")
        plt.xlabel("Image Width")
        plt.ylabel("Image Height")
        plt.tight_layout()

        output_path = self.output_folder / "width_height_scatterplot.png"
        plt.savefig(output_path)
        plt.close()

        print(f"Saved chart: {output_path}")

    def save_sample_images_grid(self, sample_count=9):
        if self.dataframe.empty:
            print("No images available for sample grid.")
            return

        sample_dataframe = self.dataframe.sample(
            min(sample_count, len(self.dataframe)),
            random_state=42
        )

        rows = 3
        cols = 3

        plt.figure(figsize=(10, 10))

        for index, (_, row) in enumerate(sample_dataframe.iterrows()):
            image = cv2.imread(row["file_path"])

            if image is None:
                continue

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            plt.subplot(rows, cols, index + 1)
            plt.imshow(image)
            plt.title(row["label"], fontsize=9)
            plt.axis("off")

        plt.suptitle("Sample Macroinvertebrate Images", fontsize=16)
        plt.tight_layout()

        output_path = self.output_folder / "sample_images_grid.png"
        plt.savefig(output_path)
        plt.close()

        print(f"Saved chart: {output_path}")

    def save_all_visualisations(self):
        self.save_class_distribution_chart()
        self.save_top_classes_chart()
        self.save_image_size_distribution()
        self.save_width_height_scatterplot()
        self.save_sample_images_grid()