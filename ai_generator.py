"""
AI blog post generator module that uses OpenAI API or falls back to mock data.
"""
import os
from typing import Dict
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def _create_blog_prompt(keyword: str, seo_data: Dict) -> str:
    """
    Create a structured prompt for the AI model.
    """
    return f"""Write a comprehensive blog post about {keyword}.
    
Key SEO metrics to consider:
- Monthly search volume: {seo_data['search_volume']}
- Keyword difficulty: {seo_data['keyword_difficulty']}
- Average CPC: ${seo_data['avg_cpc']}

Requirements:
1. Write in a conversational, engaging style
2. Include an introduction, multiple sections with headings, and a conclusion
3. Add {{AFF_LINK_X}} placeholders where product recommendations would make sense
4. Format in Markdown
5. Keep it informative and helpful for readers
6. Aim for around 1000 words
"""

def _generate_mock_blog_post(keyword: str, seo_data: Dict) -> str:
    """
    Generate a mock blog post when OpenAI API is not available.
    """
    return f"""# The Ultimate Guide to {keyword.title()}

Are you looking for the best {keyword} in {2024}? You've come to the right place! 
In this comprehensive guide, we'll explore everything you need to know about choosing 
and using {keyword}.

## Why Trust This Guide?
With over {seo_data['search_volume']} monthly searches, {keyword} is clearly a hot topic.
Our team has spent countless hours researching and testing various options to bring you
the most accurate and helpful information.

## Top Recommendations

1. Best Overall: The Premium Pro Model {{AFF_LINK_1}}
   - Outstanding quality
   - Superior performance
   - Great value for money

2. Budget-Friendly Option: EconoChoice {{AFF_LINK_2}}
   - Affordable pricing
   - Good basic features
   - Perfect for beginners

## How to Choose the Right {keyword.title()}

Consider these key factors when making your decision:
1. Your specific needs
2. Budget considerations (prices range from ${seo_data['avg_cpc']} to $199)
3. Brand reputation

## Expert Tips and Tricks

Here are some pro tips to get the most out of your {keyword}:
- Regular maintenance is key
- Start with the basics
- Upgrade gradually as needed

## Conclusion

Finding the perfect {keyword} doesn't have to be difficult. Whether you choose our top 
recommendation {{AFF_LINK_1}} or the budget-friendly {{AFF_LINK_2}}, you're now equipped 
with the knowledge to make an informed decision.

*Last updated: {2024}*
"""

def generate_blog_post(keyword: str, seo_data: Dict) -> str:
    """
    Generate a blog post using OpenAI API or fall back to mock data.
    
    Args:
        keyword (str): The main keyword for the blog post
        seo_data (dict): SEO metrics for the keyword
        
    Returns:
        str: Generated blog post content in Markdown format
    """
    if not openai.api_key:
        return _generate_mock_blog_post(keyword, seo_data)
    
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional blog writer specializing in product reviews and guides."},
                {"role": "user", "content": _create_blog_prompt(keyword, seo_data)}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return _generate_mock_blog_post(keyword, seo_data) 