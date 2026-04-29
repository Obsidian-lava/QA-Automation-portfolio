import requests
url = "http://127.0.0.1:8000/tasks"

def test_check_my_local_server():
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()

    assert data['2'], "Такая задача отсутствует"
    assert data['4']["title"], "Безымянная задача"