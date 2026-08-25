def create_category(client, name: str = "食費") -> int:
    response = client.post("/api/categories", json={"name": name})
    assert response.status_code == 200
    return response.json()["id"]


def transaction_data(category_id: int, **overrides):
    data = {
        "title": "昼食",
        "amount": 1000,
        "type": "expense",
        "date": "2026-08-25",
        "category_id": category_id,
    }
    data.update(overrides)
    return data


def test_transaction_crud(client):
    category_id = create_category(client)

    created = client.post(
        "/api/transactions",
        json=transaction_data(category_id),
    )

    assert created.status_code == 201
    transaction_id = created.json()["id"]

    updated = client.put(
        f"/api/transactions/{transaction_id}",
        json=transaction_data(
            category_id,
            title="夕食",
            amount=1500,
            type="income",
        ),
    )

    assert updated.status_code == 200
    assert updated.json()["title"] == "夕食"
    assert updated.json()["amount"] == 1500
    assert updated.json()["type"] == "income"

    deleted = client.delete(f"/api/transactions/{transaction_id}")

    assert deleted.status_code == 204
    assert deleted.content == b""
    assert client.get("/api/transactions").json()["data"] == []


def test_transactions_are_sorted_by_date_and_id_descending(client):
    category_id = create_category(client)

    for title, date in [
        ("old", "2026-08-23"),
        ("new-first", "2026-08-25"),
        ("new-second", "2026-08-25"),
    ]:
        response = client.post(
            "/api/transactions",
            json=transaction_data(category_id, title=title, date=date),
        )
        assert response.status_code == 201

    response = client.get("/api/transactions")

    assert response.status_code == 200
    assert [item["title"] for item in response.json()["data"]] == [
        "new-second",
        "new-first",
        "old",
    ]


def test_invalid_transaction_input_returns_422(client):
    category_id = create_category(client)

    zero_amount = client.post(
        "/api/transactions",
        json=transaction_data(category_id, amount=0),
    )
    invalid_date = client.post(
        "/api/transactions",
        json=transaction_data(category_id, date="not-a-date"),
    )

    assert zero_amount.status_code == 422
    assert invalid_date.status_code == 422


def test_missing_category_returns_404(client):
    response = client.post(
        "/api/transactions",
        json=transaction_data(999),
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "カテゴリが見つかりません"}


def test_update_and_delete_missing_transaction_return_404(client):
    category_id = create_category(client)

    updated = client.put(
        "/api/transactions/999",
        json=transaction_data(category_id),
    )
    deleted = client.delete("/api/transactions/999")

    assert updated.status_code == 404
    assert updated.json() == {"detail": "収支が見つかりません"}
    assert deleted.status_code == 404
    assert deleted.json() == {"detail": "収支が見つかりません"}
