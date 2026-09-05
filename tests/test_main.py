from main import fill_na_publisher
from main import sales_by_genres
import pandas as pd

def test_fill_na_publisher_replaces_missing():
    df = pd.DataFrame({"Publisher": ["Nintendo", None, "Sega"]})
    result = fill_na_publisher(df)
    assert result[0] == "Nintendo"
    assert result[1] == "Unknown"
    assert result[2] == "Sega"

def test_fill_na_publisher_no_missing_values():
    df = pd.DataFrame({"Publisher": ["Nintendo", "Sega"]})
    result = fill_na_publisher(df)
    assert result[0] == "Nintendo"
    assert result[1] == "Sega"

def test_fill_na_publisher_empty():
    df = pd.DataFrame({"Publisher": []})
    result = fill_na_publisher(df)
    assert result.empty

def test_sales_by_genre():
    df = pd.DataFrame({
        "Genre": ["Action", "Action", "Sports"],
        "Global_Sales": [10, 5, 20]
    })
    result = sales_by_genres(df)
    assert result["Action"] == 15
    assert result["Sports"] == 20

def test_sales_by_genre_single_row():
    df = pd.DataFrame({
        "Genre": ["Action"],
        "Global_Sales": [10]
    })
    result = sales_by_genres(df)
    assert result["Action"] == 10

def test_sales_by_genre_empty():
    df = pd.DataFrame({"Genre": [], "Global_Sales": []})
    result = sales_by_genres(df)
    assert result.empty