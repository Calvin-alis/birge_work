from  fastapi import APIRouter

router = APIRouter()

@router.get('/')
def index():
    return {'status': 'ok'}

@router.get('/test')
def test_info():
    return 'Hello, all done, start work!'