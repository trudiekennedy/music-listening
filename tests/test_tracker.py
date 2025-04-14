from lib.tracker import *

def test_if_track_is_empty():
    tracker = Tracker()
    assert tracker.track_list == []

def test_add_one_track_to_tracker():
    tracker = Tracker()
    tracker.add_track("Teenage Kicks")
    assert tracker.track_list == ["Teenage Kicks"]

def test_add_two_tracks_to_tracker():
    tracker = Tracker()
    tracker.add_track("Teenage Kicks")
    tracker.add_track("Billy Jean")
    assert tracker.track_list == ["Teenage Kicks", "Billy Jean"]

def test_add_two_identical_tracks_to_tracker():
    tracker = Tracker()
    tracker.add_track("Billy Jean")
    tracker.add_track("Billy Jean")
    assert tracker.track_list == ["Billy Jean"]

""" 
test_returning_the_track_list():
    create a track list
    call the track list method 
    return list should match the list we've created   
"""

def test_returning_the_track_list():
    tracker = Tracker()
    tracker.add_track("Teenage Kicks")
    tracker.add_track("Billy Jean")
    assert tracker.return_track_list() == ["Teenage Kicks", "Billy Jean"]