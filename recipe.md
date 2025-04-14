# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

class Tracker():
parameters: song, type: string
return: a list of the songs (variable to store list)

method to add track
method to return list

## 3. Create Examples as Tests

test_if_track_is_empty():
    if it's empty = return empty list

test_add_one_track_to_tracker():
    return should be a list containing 1 track

test_add_two_different_tracks_to_tracker():
    adding two tracks
    return list containing with 2 tracks 

test_add_two_identical_tracks_to_tracker():
    adding two tracks with the same name
    return list containing one track name (rather than it being repeated) 

test_returning_the_track_list():
    create a track list
    call the track list method 
    return list should match the list we've created   

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
