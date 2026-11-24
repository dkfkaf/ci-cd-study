from orderlab.api import create_app

@pytest.fixture
def client():
    return TestClient(create_app())


def test_create_and_get(client):
    response= client.post(
        "/orders",
        json={"price": 10000, "quantity": 2},
    )

    assert response.status_code==201
    assert response.json() == {
        "id": 1,
        "subtotal": 20000,

    }
    response =client.get("/orders/1")
    assert response.status_code ==200
    assert response.json() == {
        "id": 1,
        "subtotal": 20_000,

    }