
from pathlib import Path

from src.data_loader import DataLoader
from src.eda_analysis import EDAAnalysis
from src.visualisations import Visualisations

def main() -> None:
    """
    Run the Stage 1 dataset loading and EDA workflow.
    """
   dataset_path = Path.home() / "Downloads"
    output_folder = Path("outputs/eda")

    output_folder.mkdir(parents=True, exist_ok=True)

    print("Starting Stage 1: Dataset Loading and EDA")
    print("------------------------------------------")

    print("Loading dataset...")
    loader = DataLoader(dataset_path)
    dataframe = loader.load_dataset()

    print(f"Loaded {len(dataframe)} image records.")

    print("Saving dataset index...")
    loader.save_dataset_index(
        dataframe,
        output_folder / "dataset_index.csv",
    )

    print("Running EDA analysis...")
    eda = EDAAnalysis(dataframe)

    dataset_summary = eda.get_dataset_summary()
    class_counts = eda.get_class_counts()
    image_size_summary = eda.get_image_size_summary()
    channel_counts = eda.get_channel_counts()
    balance_message = eda.check_class_balance()

    dataset_summary.to_csv(output_folder / "dataset_summary.csv", index=False)
    class_counts.to_csv(output_folder / "class_counts.csv", index=False)
    image_size_summary.to_csv(output_folder / "image_size_summary.csv")
    channel_counts.to_csv(output_folder / "channel_counts.csv", index=False)

    eda.write_eda_findings(output_folder / "eda_findings.txt")

    print("\nDataset Summary:")
    print(dataset_summary)

    print("\nClass Counts:")
    print(class_counts)

    print("\nImage Size Summary:")
    print(image_size_summary)

    print("\nChannel Counts:")
    print(channel_counts)

    print("\nClass Balance Interpretation:")
    print(balance_message)

    print("\nCreating visualisations...")
    visualisations = Visualisations(dataframe, output_folder)
    visualisations.save_all_visualisations()

    print("\nStage 1 EDA complete.")
    print(f"All outputs saved in: {output_folder}")


if __name__ == "__main__":
    main()
