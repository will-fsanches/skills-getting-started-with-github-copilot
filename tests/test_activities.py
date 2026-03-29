import pytest


def test_get_activities_returns_all_activities(client):
    """Test that GET /activities returns all activities"""
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    
    # Should have 9 activities
    assert len(data) == 9
    
    # Check that expected activities are present
    assert "Chess Club" in data
    assert "Programming Class" in data
    assert "Gym Class" in data


def test_get_activities_response_structure(client):
    """Test that activities have the correct structure"""
    response = client.get("/activities")
    data = response.json()
    
    # Check one activity's structure
    chess_club = data["Chess Club"]
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    
    # Check types
    assert isinstance(chess_club["participants"], list)
    assert isinstance(chess_club["max_participants"], int)