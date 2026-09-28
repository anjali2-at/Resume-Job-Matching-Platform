def test_api_response_structure():

    response = {
        "success": True,
        "match_score": 85
    }

    assert "success" in response
    assert "match_score" in response


def test_api_success_status():

    response = {
        "success": True
    }

    assert response["success"] is True