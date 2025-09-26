import pandas as pd
from pmla.config import DATA_PATH

def load_kyc_data():
    """Load client KYC data from CSV (mocking stock broker system)."""
    df = pd.read_csv(DATA_PATH / "kyc_clients.csv")
    return df

def get_client_by_id(client_id: int):
    df = load_kyc_data()
    client = df[df["client_id"] == client_id]
    if client.empty:
        return None
    return client.to_dict(orient="records")[0]
