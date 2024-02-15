from fastapi import APIRouter
import ExchangeModule.service as Service 
from ExchangeModule.model import CodeList

router = APIRouter()

@router.get("/code/list", summary="Get a list of country codes", response_model=CodeList)
async def code_list(
    ):
    """
        Получить список кодов стран
    """
    try:
        json_structure = await Service.code_list()
        return json_structure
    except Exception as e:
        return {"error": str(e)}
   