from test.test_main import client
from main import app
from fastapi import status
from router.auth import get_current_user
from database import SessionLocal
from models import Todos

def override_get_current_user():
    return{
        'id':1,
        'username':'testuser'
    }

def test_todo():
    db=SessionLocal()
    db.query(Todos).filter(Todos.id==99).delete()
    
    todo=Todos(
        id = 99,                 # Use = instead of :
        title = 'Testing',       # Use = instead of :
        description = 'Testing', # Use = instead of :
        priority = 5,            # Use = instead of :
        completed = True,
        owner_id = 1
        )
    db.add(todo)
    db.commit()

app.dependency_overrides[get_current_user] = override_get_current_user

def test_read_todos():
    response=client.get('/')
    assert response.status_code == status.HTTP_200_OK
    
def test_read_specific_todos():
    response = client.get('/todo/99')
    assert response.status_code==status.HTTP_200_OK