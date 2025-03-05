from fastapi import APIRouter, HTTPException
from schemas.key_value_schema import KeyValue
from database.db import r
from starlette import status
from typing import List

router = APIRouter()

# Just for testing purpose

@router.post("/set", status_code=status.HTTP_201_CREATED, response_model=KeyValue)
def set_key_value(
    key_value: KeyValue
):
    response = r.get(key_value.key)
    if response:
        raise HTTPException(status_code=409, detail="key already exists")
    r.set(key_value.key, key_value.value)
    return KeyValue(
        key=key_value.key,
        value=r.get(key_value.key).decode()
    )


@router.get("/get/{key}", status_code=status.HTTP_200_OK, response_model=KeyValue)
def get_key_value(
    key: str
):
    response = r.get(key)
    if not response:
        raise HTTPException(status_code=404, detail="key not found")
    value = response.decode()
    return KeyValue(
        key=key,
        value=value
    )

@router.get("/search", status_code=status.HTTP_200_OK, response_model=List[str])
def search_keys(
    prefix: str = "",
    suffix: str = ""
):
    return r.keys(f"{prefix}*{suffix}")




