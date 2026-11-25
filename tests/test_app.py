from app.main import app


def test_index():
    r = app.test_client().get("/")
    assert r.status_code == 200
    assert r.get_json()["service"] == "rosa-depot"


def test_healthz():
    r = app.test_client().get("/healthz")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}
