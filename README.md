# AI Blog Generator

A Flask-based REST API that generates SEO-optimized blog posts using AI. The application includes keyword analysis, content generation with affiliate link placeholders, and automated daily blog generation.

## Features

- REST API endpoint for blog post generation
- SEO metrics analysis (search volume, keyword difficulty, CPC)
- AI-powered content generation using OpenAI API
- Automated daily blog post generation
- Environment variable support
- Affiliate link placeholder insertion

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- OpenAI API key (optional - will use mock data if not provided)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ai-blog-generator-interview-Ryan.git
cd ai-blog-generator-interview-Ryan
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:

```bash
touch .env
```

5. Add your OpenAI API key to `.env` (optional):

```
OPENAI_API_KEY=your_api_key_here
```

## Usage

### Starting the Flask Application

Run the Flask application:

```bash
python app.py
```

The server will start at `http://localhost:5000`

### API Endpoints

#### Generate Blog Post

```
GET /generate?keyword=your+keyword+here
```

Example request:

```bash
curl "http://localhost:5000/generate?keyword=wireless+earbuds"
```

Example response:

```json
{
  "keyword": "wireless earbuds",
  "seo_data": {
    "search_volume": 5000,
    "keyword_difficulty": 45,
    "avg_cpc": 2.5
  },
  "content": "# The Ultimate Guide to Wireless Earbuds...[rest of content]"
}
```

### Automated Blog Generation

The application includes a scheduler that automatically generates a blog post for "wireless earbuds" every day at midnight. The generated posts are saved in the `blogs/` directory with timestamps.

## Project Structure

```
ai-blog-generator-interview-Ryan/
├── app.py                      # Main Flask application
├── ai_generator.py             # AI content generation module
├── seo_fetcher.py             # SEO metrics module
├── requirements.txt           # Python dependencies
├── .env                      # Environment variables (create this)
├── .gitignore               # Git ignore rules
├── README.md                # This file
├── example_wireless_earbuds.md # Example blog post
└── blogs/                   # Generated blog posts directory
```

## Development

- The SEO metrics in `seo_fetcher.py` are currently mocked. Replace with real API calls if needed.
- The AI generation will use OpenAI if an API key is provided, otherwise falls back to mock data.
- The scheduler runs daily at midnight - adjust the schedule in `app.py` if needed.

## Error Handling

- Missing keyword parameter returns 400 Bad Request
- Invalid OpenAI API key falls back to mock data
- Other errors return 500 Internal Server Error with error message

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
