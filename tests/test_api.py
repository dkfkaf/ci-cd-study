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

def test_invalid_price(client):
    response = client.post(
    "/orders",
    json={"price": -1, "quantity":1},
    )
    assert response.status_code == 422

def test_not_found(client):
        response = client.get("/orders/999")
        assert response.status_code == 404
        assert response.json() == {"detail": "not found"}

def test_fresh_store_per_teset(client):
     response = client.get("/orders/1")
     assert response.status_code == 404