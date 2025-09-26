from fastapi import APIRouter, HTTPException
from pmla.data_access import load_kyc_data, get_client_by_id

router = APIRouter()

@router.get("/clients")
def get_all_clients():
    df = load_kyc_data()
    return df.to_dict(orient="records")

@router.get("/clients/{client_id}")
def get_client(client_id: int):
    client = get_client_by_id(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client
