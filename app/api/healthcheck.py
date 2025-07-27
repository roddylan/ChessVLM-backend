from fastapi import APIRouter

router = APIRouter()

@router.get('/healthcheck', status_code=200)
def healthcheck():
    return {"Status": "Healthy"}