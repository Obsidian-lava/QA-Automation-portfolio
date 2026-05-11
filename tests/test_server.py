import requests
url = "http://127.0.0.1:8000/tasks"

def test_check_my_local_server():
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()

    assert '2' in data, "Такая задача отсутствует"
    assert data['4']["title"], "Безымянная задача"

def test_delete():
    task_id = "2"

    delete_url = f"{url}/{task_id}"

    response_delete = requests.delete(delete_url)

    response = requests.get(url)
    data = response.json()

    assert task_id not in data, "Эта задача все еще присутствует в базе"

def test_put():
    task_id = "4"

    put_url = f"{url}/{task_id}"

    new_data = {"title": "special task", "description": "this is special task"}

    response_put = requests.put(put_url, json=new_data)

    response = requests.get(url)
    data = response.json()

    assert data[task_id]["title"] == new_data["title"]
    assert data[task_id]["description"] == new_data["description"]

def test_patch():
    task_id = "1"

    patch_url = f"{url}/{task_id}"

    requests.post(f"{url}/{task_id}", json={"title": "best title", "description": "best description"})

    requests.patch(f"{url}/{task_id}", json={"title": "title was changed"})

    response = requests.get(url)

    data = response.json()


    assert data[task_id]["title"] == "title was changed"
    assert data[task_id]["description"] == "best description"