import pandas as pd
import requests


def extract_data():
    """Extract user data from the REST API."""
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


def transform_data(raw_data):
    """Clean and transform the extracted user data."""
    df = pd.json_normalize(raw_data)

    df = df[[
        "id",
        "name",
        "username",
        "email",
        "phone",
        "website"
    ]].copy()

    df["email"] = df["email"].str.lower()
    df["name_length"] = df["name"].str.len()

    return df


def load_data(dataframe):
    """Save the transformed data into a CSV file."""
    dataframe.to_csv("transformed_users.csv", index=False)


def run_pipeline():
    """Execute the complete ETL pipeline."""
    raw_data = extract_data()

    transformed_data = transform_data(raw_data)

    load_data(transformed_data)

    print(
        "ETL process completed successfully. "
        "File saved to transformed_users.csv"
    )


if __name__ == "__main__":
    run_pipeline()


# -------------------- PYTEST TESTS --------------------

def test_transform_data():
    sample_data = [
        {
            "id": 1,
            "name": "Ada Lovelace",
            "username": "ada",
            "email": "ADA@EXAMPLE.COM",
            "phone": "123456789",
            "website": "example.com"
        }
    ]

    result = transform_data(sample_data)

    assert result.loc[0, "email"] == "ada@example.com"
    assert result.loc[0, "name_length"] == 12
    assert "name_length" in result.columns


def test_extract_data(monkeypatch):
    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return [
                {
                    "id": 1,
                    "name": "Ada Lovelace",
                    "username": "ada",
                    "email": "ada@example.com",
                    "phone": "123456789",
                    "website": "example.com"
                }
            ]

    def fake_get(url, timeout):
        return FakeResponse()

    monkeypatch.setattr(requests, "get", fake_get)

    result = extract_data()

    assert len(result) == 1
    assert result[0]["name"] == "Ada Lovelace"


def test_load_data(tmp_path):
    sample_data = [
        {
            "id": 1,
            "name": "Ada Lovelace",
            "username": "ada",
            "email": "ada@example.com",
            "phone": "123456789",
            "website": "example.com"
        }
    ]

    dataframe = transform_data(sample_data)

    output_file = tmp_path / "users.csv"

    dataframe.to_csv(output_file, index=False)

    assert output_file.exists()
