import pytest
from cso_app.models import CSOEvent
from datetime import datetime

@pytest.mark.django_db
def test_create_event():
    event = CSOEvent.objects.create(
        location="Test Location",
        latitude=40.0,
        longitude=-80.0,
        start_time=datetime.now(),
        end_time=datetime.now(),
        overflow_volume_m3=10,
        cause="Rainfall",
        severity="High",
    )
    assert event.id is not None
