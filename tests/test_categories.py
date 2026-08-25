def create_category(client, name: str):
    return client.post("/api/categories", json={"name": name})


def test_create_and_list_categories_in_creation_order(client):
    first = create_category(client, "食費")
    second = create_category(client, "交通費")

    assert first.status_code == 200
    assert second.status_code == 200

    response = client.get("/api/categories")

    assert response.status_code == 200
    assert [category["name"] for category in response.json()] == [
        "食費",
        "交通費",
    ]


def test_category_name_is_trimmed(client):
    response = create_category(client, "  食費  ")

    assert response.status_code == 200
    assert response.json()["name"] == "食費"


def test_create_duplicate_category_returns_409(client):
    create_category(client, "食費")

    response = create_category(client, "  食費  ")

    assert response.status_code == 409
    assert response.json() == {
        "detail": "同じ名前のカテゴリが既に存在します"
    }


def test_update_category(client):
    category = create_category(client, "食費").json()

    response = client.put(
        f"/api/categories/{category['id']}",
        json={"name": "飲食費"},
    )

    assert response.status_code == 200
    assert response.json() == {"id": category["id"], "name": "飲食費"}


def test_update_missing_category_returns_404(client):
    response = client.put("/api/categories/999", json={"name": "食費"})

    assert response.status_code == 404
    assert response.json() == {"detail": "カテゴリが見つかりません"}


def test_update_to_duplicate_category_name_returns_409(client):
    create_category(client, "食費")
    category = create_category(client, "交通費").json()

    response = client.put(
        f"/api/categories/{category['id']}",
        json={"name": "食費"},
    )

    assert response.status_code == 409
    assert response.json() == {
        "detail": "同じ名前のカテゴリが既に存在します"
    }
