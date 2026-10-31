import pytest
from hotel_booking import booking_cost, cancellation_refund, room_upgrade

# BOOKING COST TESTS

def test_standard_booking():
    assert booking_cost("standard", 2, 2, False) == 4000

def test_deluxe_booking():
    assert booking_cost("deluxe", 3, 2, False) == 10500

def test_peak_season():
    assert booking_cost("standard", 2, 2, True) == 5000

def test_extra_guests():
    assert booking_cost("standard", 2, 3, False) == 5000

def test_weekly_discount():
    assert booking_cost("standard", 7, 2, False) == 12600

def test_unknown_room():
    with pytest.raises(ValueError):
        booking_cost("presidential", 2, 2, False)

def test_invalid_nights():
    with pytest.raises(ValueError):
        booking_cost("standard", 0, 2, False)

# CANCELLATION REFUND TESTS

def test_full_refund():
    assert cancellation_refund(1000, 10, False) == 1000

def test_partial_refund():
    assert cancellation_refund(1000, 4, False) == 500

def test_no_refund():
    assert cancellation_refund(1000, 1, False) == 0

def test_member_refund():
    assert cancellation_refund(1000, 4, True) == 750

# ROOM UPGRADE TESTS

def test_no_rooms_available():
    assert room_upgrade("standard", True, 0) == "standard"

def test_standard_member_upgrade():
    assert room_upgrade("standard", True, 2) == "deluxe"

def test_deluxe_member_upgrade():   
    assert room_upgrade("deluxe", True, 2) == "suite"

def test_non_member_no_upgrade():
    assert room_upgrade("standard", False, 2) == "standard"

def test_suite_no_upgrade():
    assert room_upgrade("suite", True, 2) == "suite"
