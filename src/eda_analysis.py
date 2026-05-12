from pathlib import Path
import pandas as pd


class EDAAnalysis:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def get_dataset_summary(self):
        if self.dataframe.empty:
            return pd.DataFrame([{
                "total_images": 0,
                "total_classes": 0,
                "average_width": 0,
                "average_height": 0
            }])

        return pd.DataFrame([{
            "total_images": len(self.dataframe),
            "total_classes": self.dataframe["label"].nunique(),
            "average_width": round(self.dataframe["width"].mean(), 2),
            "average_height": round(self.dataframe["height"].mean(), 2),
            "min_width": self.dataframe["width"].min(),
            "max_width": self.dataframe["width"].max(),
            "min_height": self.dataframe["height"].min(),
            "max_height": self.dataframe["height"].max()
        }])

    def get_class_counts(self):
        class_counts = self.dataframe["label"].value_counts().reset_index()
        class_counts.columns = ["label", "image_count"]
        return class_counts

    def get_image_size_summary(self):
        return self.dataframe[["width", "height"]].describe()

    def get_channel_counts(self):
        channel_counts = self.dataframe["channels"].value_counts().reset_index()
        channel_counts.columns = ["channels", "image_count"]
        return channel_counts

    def check_class_balance(self):
        class_counts = self.get_class_counts()

        if class_counts.empty:
            return "No class data was found."

        largest_class_count = class_counts["image_count"].max()
        smallest_class_count = class_counts["image_count"].min()

        if smallest_class_count == 0:
            return "Some classes contain no images."

        imbalance_ratio = largest_class_count / smallest_class_count

        if imbalance_ratio > 2:
            return (
                "The dataset appears imbalanced because the largest class has "
                f"{imbalance_ratio:.2f} times more images than the smallest class."
            )

        return "The dataset appears reasonably balanced."

    def write_eda_findings(self, output_path):
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        summary = self.get_dataset_summary()
        class_counts = self.get_class_counts()
        balance_message = self.check_class_balance()

        findings = f"""
Exploratory Data Analysis Findings

Dataset summary:
{summary.to_string(index=False)}

Class counts:
{class_counts.to_string(index=False)}

Class balance:
{balance_message}

Why this matters:
This EDA helps the group understand the dataset before classification.
It shows the number of images, number of classes, image sizes and class balance.
"""

        output_path.write_text(findings.strip(), encoding="utf-8")
        print(f"EDA findings saved to: {output_path}")