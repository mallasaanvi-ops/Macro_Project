from pathlib import Path

import cv2
import pandas as pd


class DataLoader:
    """
    Loads macroinvertebrate image data from a folder structure.

    This class scans all image files inside the dataset folder and creates
    a pandas DataFrame containing image metadata such as file path, label,
    width, height, channels, file name and file extension.
    """

    def __init__(self, dataset_path: str | Path) -> None:
        self.dataset_path = Path(dataset_path)
        self.supported_extensions = {
            ".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp"
        }

    def load_dataset(self) -> pd.DataFrame:
        """
        Scan the dataset folder and return a DataFrame of image metadata.
        """
        records = []

        if not self.dataset_path.exists():
            raise FileNotFoundError(
                f"Dataset folder not found: {self.dataset_path}"
            )

        for file_path in self.dataset_path.rglob("*"):
            if file_path.suffix.lower() not in self.supported_extensions:
                continue

            image = cv2.imread(str(file_path))

            if image is None:
                print(f"Warning: Could not read image: {file_path}")
                continue

            height, width = image.shape[:2]
            channels = image.shape[2] if len(image.shape) == 3 else 1
            label = file_path.parent.name

            records.append(
                {
                    "file_path": str(file_path),
                    "file_name": file_path.name,
                    "file_extension": file_path.suffix.lower(),
                    "label": label,
                    "width": width,
                    "height": height,
                    "channels": channels,
                }
            )

        dataframe = pd.DataFrame(records)

        if dataframe.empty:
            print("Warning: No image records were found.")

        return dataframe

    def save_dataset_index(
        self,
        dataframe: pd.DataFrame,
        output_path: str | Path,
    ) -> None:
        """
        Save the dataset index as a CSV file.
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        dataframe.to_csv(output_path, index=False)
        print(f"Dataset index saved to: {output_path}")