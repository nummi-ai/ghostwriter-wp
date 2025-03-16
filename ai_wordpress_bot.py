import openai
import requests
import os

# Load credentials from environment variables (with placeholders for safety)
WORDPRESS_URL = os.getenv("WORDPRESS_URL", "https://your-wordpress-site.com/wp-json/wp/v2/posts")
WORDPRESS_USER = os.getenv("WORDPRESS_USER", "your_username")
WORDPRESS_PASSWORD = os.getenv("WORDPRESS_PASSWORD", "your_password")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key")

# Initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def generate_article(topic):
    """Generates an article using OpenAI GPT-4o-mini"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional content writer."},
            {"role": "user", "content": f"Write a detailed blog post about {topic} in 200 words. "}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

def post_to_wordpress(title, content):
    """Posts the generated article to WordPress"""
    auth = (WORDPRESS_USER, WORDPRESS_PASSWORD)
    headers = {"Content-Type": "application/json"}
    
    post_data = {
        "title": title,
        "content": content,
        "status": "draft"  # Change to 'publish' if you want it live immediately
    }

    response = requests.post(WORDPRESS_URL, json=post_data, auth=auth, headers=headers)

    if response.status_code == 201:
        print(f"✅ Successfully posted: {response.json().get('link')}")
    else:
        print(f"❌ Failed to post. Error: {response.text}")

if __name__ == "__main__":
    topics = input("Enter blog topics (separated by commas): ").strip()
    topics_list = [t.strip() for t in topics.split(",") if t.strip()]

    for topic in topics_list:
        print(f"\n📝 Generating article for: {topic}...")
        article_content = generate_article(topic)
        print(f"\nGenerated Article for '{topic}':\n", article_content)

        confirm = input(f"\nPost '{topic}' to WordPress? (yes/no): ").strip().lower()
        if confirm == "yes":
            post_to_wordpress(topic, article_content)
