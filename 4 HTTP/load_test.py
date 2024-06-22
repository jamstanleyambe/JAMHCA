import molotov

@molotov.scenario(10)
async def scenario_one(session):
    async with session.get('http://your-server-url/api/endpoint1') as response:
        assert response.status == 200, f"Unexpected status: {response.status}"
        json_data = await response.json()
        assert 'expected_key' in json_data, "Missing expected key in JSON response"

@molotov.scenario(5)
async def scenario_two(session):
    async with session.get('http://your-server-url/api/endpoint2') as response:
        assert response.status == 200, f"Unexpected status: {response.status}"
        json_data = await response.json()
        assert 'another_key' in json_data, "Missing another key in JSON response"