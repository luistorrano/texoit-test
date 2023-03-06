import json

def test_interval(app, client):
    res = client.get('/interval')
    assert res.status_code == 200
    res_json = json.loads(res.get_data(as_text=True))
    assert 'min' in res_json
    assert 'max' in res_json
    assert len(res_json.get('min')) > 0
    assert len(res_json.get('max')) > 0