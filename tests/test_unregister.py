import pytest


def test_unregister_successful(client):
    """Test successful unregister from an activity"""
    # First sign up
    client.post("/activities/Chess%20Club/signup?email=removeme@mergington.edu")
    
    # Then unregister
    response = client.delete("/activities/Chess%20Club/signup?email=removeme@mergington.edu")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Unregistered removeme@mergington.edu from Chess Club" in data["message"]
    
    # Verify the participant was removed
    get_response = client.get("/activities")
    activities = get_response.json()
    assert "removeme@mergington.edu" not in activities["Chess Club"]["participants"]


def test_unregister_activity_not_found(client):
    """Test unregister from non-existent activity returns 404"""
    response = client.delete("/activities/NonExistent%20Activity/signup?email=test@mergington.edu")
    assert response.status_code == 404
    data = response.json()
    assert "Activity not found" in data["detail"]


def test_unregister_student_not_signed_up(client):
    """Test unregistering a student who is not signed up returns 400"""
    response = client.delete("/activities/Chess%20Club/signup?email=notsignedup@mergington.edu")
    assert response.status_code == 400
    data = response.json()
    assert "Student is not signed up for this activity" in data["detail"]