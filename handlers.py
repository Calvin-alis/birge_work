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

