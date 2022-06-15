from  fastapi import APIRouter, Body, Depends
from birg_work.forms import UserLoginForm
from birg_work.models import  conntect_db

router = APIRouter()

@router.post('/login', name='user:login')
def login(user_form: UserLoginForm= Body(..., embed=True), database =  ):
    return {'status': 'ok'}


@router.get('/test')
def test_info():
    return 'Hello, all done, start work!'

