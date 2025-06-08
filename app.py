"""
Main Flask application module for the AI blog generator.
"""
import os
from datetime import datetime
from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv

from seo_fetcher import get_seo_data
from ai_generator import generate_blog_post

# Load environment variables
load_dotenv()

app = Flask(__name__)

def generate_scheduled_blog():
    """
    Scheduled job to generate a blog post for a fixed keyword.
    Saves the output to a file in the blogs directory.
    """
    keyword = "wireless earbuds"
    print(f"Generating scheduled blog post for keyword: {keyword}")
    
    # Create blogs directory if it doesn't exist
    os.makedirs("blogs", exist_ok=True)
    
    # Generate the blog post
    seo_data = get_seo_data(keyword)
    content = generate_blog_post(keyword, seo_data)
    
    # Save to file with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"blogs/blog_{keyword.replace(' ', '_')}_{timestamp}.md"
    
    with open(filename, "w") as f:
        f.write(content)
    
    print(f"Blog post saved to: {filename}")

# Initialize scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(
    func=generate_scheduled_blog,
    trigger="cron",
    hour=0,  # Run at midnight
    minute=0,
    id="daily_blog_generator"
)
scheduler.start()

@app.route("/generate", methods=["GET"])
def generate():
    """
    Generate a blog post based on the provided keyword.
    
    Query Parameters:
        keyword (str): The main topic for the blog post
        
    Returns:
        JSON response containing the keyword, SEO data, and generated content
    """
    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "Missing 'keyword' parameter"}), 400
    
    try:
        # Get SEO data
        seo_data = get_seo_data(keyword)
        
        # Generate blog post
        content = generate_blog_post(keyword, seo_data)
        
        return jsonify({
            "keyword": keyword,
            "seo_data": seo_data,
            "content": content
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True) 