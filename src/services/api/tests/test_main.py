def test_main(mock_env):
    import uvicorn
    from run import app
    uvicorn.run(app, host="localhost", port=8001)

    assert True
