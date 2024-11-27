from src.analysis import run_analysis

def test_run_analysis():
    result = run_analysis()
    assert "avg_height_male" in result
    assert "avg_height_female" in result
    assert "avg_weight_male" in result
    assert "avg_weight_female" in result
    assert result["avg_height_male"] > 0
    assert result["avg_height_female"] > 0
    assert result["avg_weight_male"] > 0
    assert result["avg_weight_female"] > 0