from pathlib import Path
import random
import pandas as pd


def prepare_cefr_dataset() -> None:
    """Creates a dummy DataFrame, processes it, and saves it to CSV files."""

    # Step 1: Create dummy DataFrame
    data = {
        'text': [f'This is text number {i+1}' for i in range(100)],
        'Annotator I': [random.randint(1, 6) for _ in range(100)]
    }
    df = pd.DataFrame(data)

    # Step 2: Map Annotator I scores to CEFR labels
    score_to_cefr = {1: "A1", 2: "A2", 3: "B1", 4: "B2", 5: "C1", 6: "C2"}
    df["label"] = df["Annotator I"].map(score_to_cefr)
    

    # Step 3: Drop rows with NaN labels
    df.dropna(subset=["label"], inplace=True)

    # Step 4: Drop unnecessary columns
    df = df[["text", "label"]]
    # Step 5: Split into train, validation, test sets
    train_df = df.sample(frac=0.7, random_state=42)
    temp_df = df.drop(train_df.index)
    validation_df = temp_df.sample(frac=0.5, random_state=42)
    test_df = temp_df.drop(validation_df.index)

    # Step 6: Save to CSV
    train_df.to_csv("train_cefr.csv", index=False)
    validation_df.to_csv("validation_cefr.csv", index=False)
    test_df.to_csv("test_cefr.csv", index=False)


if __name__ == "__main__":
    prepare_cefr_dataset()
    print("✅ All datasets are prepared and saved!")