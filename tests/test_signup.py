import pytest


def test_signup_successful(client):
    """Test successful signup for an activity"""
    response = client.post("/activities/Chess%20Club/signup?email=newstudent@mergington.edu")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Signed up newstudent@mergington.edu for Chess Club" in data["message"]
    
    # Verify the participant was added
    get_response = client.get("/activities")
    activities = get_response.json()
    assert "newstudent@mergington.edu" in activities["Chess Club"]["participants"]


def test_signup_activity_not_found(client):
    """Test signup for non-existent activity returns 404"""
    response = client.post("/activities/NonExistent%20Activity/signup?email=test@mergington.edu")
    assert response.status_code == 404
    data = response.json()
    assert "Activity not found" in data["detail"]


def test_signup_duplicate_participant(client):
    """Test that signing up twice returns 400"""
    # First signup
    client.post("/activities/Chess%20Club/signup?email=duplicate@mergington.edu")
    
    # Second signup should fail
    response = client.post("/activities/Chess%20Club/signup?email=duplicate@mergington.edu")
    assert response.status_code == 400
    data = response.json()
    assert "Student already signed up for this activity" in data["detail"]