import pytest
import sort_ps6 as ps6
from datetime import datetime

def test_PS6Class():
    t = ps6.PS6(0, 9, datetime(1970,1,1), 1, 'minute', 'Test Colorway', 'Test Sculpt', 69, 420, 'https://www.google.com', False)
    assert t