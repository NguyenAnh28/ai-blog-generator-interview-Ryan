"""
SEO data fetcher module that provides keyword metrics.
This is a mock implementation that returns sample data based on keyword characteristics.
"""
import random


def get_seo_data(keyword: str) -> dict:
    """
    Get SEO metrics for a given keyword.
    Currently implements a mock that returns sample data based on keyword length.
    
    Args:
        keyword (str): The keyword to analyze
        
    Returns:
        dict: Dictionary containing SEO metrics
    """
    # Mock implementation - generates "realistic" looking data based on keyword length
    keyword_length = len(keyword)
    
    # Longer keywords typically have lower search volume but less competition
    search_volume = max(100, int(10000 / (keyword_length * 0.5)))
    keyword_difficulty = min(100, keyword_length * 10 + random.randint(10, 30))
    avg_cpc = round(random.uniform(0.5, 5.0), 2)
    
    return {
        "keyword": keyword,
        "search_volume": search_volume,
        "keyword_difficulty": keyword_difficulty,
        "avg_cpc": avg_cpc
    } 