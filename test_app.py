import json

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.json['message'] == 'Are you feeling fruity????'

    def test_get_fruits(self, api):
        res = api.get('/api/fruits')
        assert res.status == '200 OK'
        assert len(res.json) == 2

    def test_get_fruit(self, api):
        res = api.get('/api/fruits/2')
        assert res.status == '200 OK'
        assert res.json['fruit'] == 'Test Fruit 2'

    def test_get_fruits_error(self, api):
        res = api.get('/api/fruits/4')
        assert res.status == '400 BAD REQUEST'
        assert "fruit with id 4" in res.json['message']

    def test_post_fruits(self, api):
        mock_data = json.dumps({'name': 'Molly'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/api/fruits', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 3

    # def test_patch_fruit(self, api):
    #     mock_data = json.dumps({'name': 'Molly'})
    #     mock_headers = {'Content-Type': 'application/json'}
    #     res = api.patch('/api/fruits/2', data=mock_data, headers=mock_headers)
    #     assert res.json['id'] == 2
    #     assert res.json['name'] == 'Molly'

    def test_delete_fruit(self, api):
        res = api.delete('/api/fruits/1')
        assert res.status == '204 NO CONTENT'

    def test_not_found(self, api):
        res = api.get('/bob')
        assert res.status == '404 NOT FOUND'
        assert 'Oops!' in res.json['message']