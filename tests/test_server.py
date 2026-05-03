import requests
url = "http://127.0.0.1:8000/tasks"

def test_check_my_local_server():
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()

    assert data['2'], "Такая задача отсутствует"
    assert data['4']["title"], "Безымянная задача"

def test_delete():
    task_id = '2'

    delete_url = f"{url}/{task_id}"

    response_delete = requests.delete(delete_url)

    response = requests.get(url)
    data = response.json()

    assert not data[task_id], "Эта задача все еще присутствует в базе"

    response_retry = requests.delete(delete_url)

    assert response_retry.status_code == 404