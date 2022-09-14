import pytest
from src.server.client import Client


class TestClient:

    @pytest.fixture
    def init_cl(self):
        self.cl = Client('127.0.0.1', 10000)
        yield
        self.cl.close()

    def test_open(self):
        assert self.cl.open() == True

    def test_recv_set(self):
        assert self.cl.recieve() == 'SET'
