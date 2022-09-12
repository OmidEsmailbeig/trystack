import pytest


TEST_PROJECT_ID = None


@pytest.mark.parametrize(
    ('headers', 'data', 'status'),
    [
        ({}, '', 415),
        ({'Content-Type': 'application/json'}, 'test', 400),
        ({'Content-Type': 'application/json'}, {'name': ''}, 400),
        ({'Content-Type': 'application/json'}, {'name': 1}, 400),
        ({'Content-Type': 'application/json'}, {'name': 'test', 'family': 'test'}, 400),
        ({'Content-Type': 'application/json'}, {'name': 'test'}, 201),
        ({'Content-Type': 'application/json'}, {'name': 'test'}, 409),
        ({'Content-Type': 'application/json'}, {'test': 'test'}, 400),
    ]
)
def test_create_project(client, headers, data, status):
    if type(data) is dict:
        response = client.post('/api/v1/projects', headers=headers, json=data)
    else:
        response = client.post('/api/v1/projects', headers=headers, data=data)
    assert response.status_code == status
    if response.status_code == 201:
        global TEST_PROJECT_ID
        TEST_PROJECT_ID = response.get_json()['project']['id']


@pytest.mark.parametrize(
    ('headers', 'status'),
    [
        ({}, 415),
        ({'Content-Type': 'application/json'}, 200)
    ],
)
def test_get_projects(client, headers, status):
    response = client.get(
        '/api/v1/projects',
        headers=headers,
    )
    assert response.status_code == status


@pytest.mark.parametrize(
    ('headers', 'project_id', 'status'),
    [
        ({}, 'test', 415),
        ({'Content-Type': 'application/json'}, 'test', 404),
        ({'Content-Type': 'application/json'}, 'TEST_PROJECT_ID', 200),
    ],
)
def test_get_project(client, headers, project_id, status):
    response = client.get(
        f'/api/v1/projects/{TEST_PROJECT_ID if project_id == "TEST_PROJECT_ID" else project_id}',
        headers=headers
    )
    assert response.status_code == status


@pytest.mark.parametrize(
    ('headers', 'project_id', 'data', 'status'),
    [
        ({}, 'test', '', 415),
        ({'Content-Type': 'application/json'}, 'test', 'test', 400),
        ({'Content-Type': 'application/json'}, 'test', {'name': ''}, 400),
        ({'Content-Type': 'application/json'}, 'test', {'status': ''}, 400),
        ({'Content-Type': 'application/json'}, 'test', {'status': -10}, 400),
        ({'Content-Type': 'application/json'}, 'test', {'status': 1}, 404),
        ({'Content-Type': 'application/json'}, 'TEST_PROJECT_ID', {'status': 1}, 200),
    ],
)
def test_update_project(client, headers, project_id, data, status):
    print(TEST_PROJECT_ID if project_id == TEST_PROJECT_ID else project_id)
    if type(data) is dict:
        response = client.patch(
            f'/api/v1/projects/{TEST_PROJECT_ID if project_id == "TEST_PROJECT_ID" else project_id}',
            headers=headers,
            json=data
        )
    else:
        response = client.patch(
            f'/api/v1/projects/{TEST_PROJECT_ID if project_id == "TEST_PROJECT_ID" else project_id}',
            headers=headers,
            data=data
        )
    assert response.status_code == status


@pytest.mark.parametrize(
    ('headers', 'project_id', 'status'),
    [
        ({}, 'test', 415),
        ({'Content-Type': 'application/json'}, 'test', 404),
        ({'Content-Type': 'application/json'}, 'TEST_PROJECT_ID', 204),
    ],
)
def test_delete_project(client, headers, project_id, status):
    response = client.delete(
        f'/api/v1/projects/{TEST_PROJECT_ID if project_id == "TEST_PROJECT_ID" else project_id}',
        headers=headers
    )
    response.status_code == status
