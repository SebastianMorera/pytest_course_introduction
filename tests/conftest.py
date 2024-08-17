import pytest
from stuff.accum import Accumulator

### Chapter 6: Fixtures
@pytest.fixture
def accum(scope='function'):
    yield Accumulator()
    print("DONE with the test!")