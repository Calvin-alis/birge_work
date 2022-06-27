from  fastapi import APIRouter, Body, Depends
from forms import UserLoginForm
from models import  conntect_db

router = APIRouter()

@router.post('/login', name='user:login')
def login(user_form: UserLoginForm= Body(..., embed=True), database = Depends(conntect_db)):
    return {'status': 'ok'}


@router.get('/test')
def test_info():
    return 'Hello, all done, start work!'

@router.get('/alternat/')
async def alternate(n = 0, first_value , second_value):
    try:
        n = int(n)
        result = []
        while len(result) != n:
            if len(result) < n:
                result.append(first_value)
            if len(result) < n:
                result.append(second_value)
        return f' Codewars Task have result: {result}'
    except:
        return 'Wrong parameters! Try Again.'
