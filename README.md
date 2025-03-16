# Ghostwriter-WP 🚀

**Automate Blog Creation & Publishing with AI**

Ghostwriter-WP is an AI-powered WordPress automation bot that generates and publishes blog posts effortlessly. Powered by **GPT-4o-mini** (configurable to any model), this script streamlines content creation, making blogging faster and easier. 

## 🌟 Features
- ✅ Generate multiple articles at once from a list of topics
- ✅ Automatically publish to WordPress
- ✅ Configurable AI model for content generation
- ✅ Open-source & community-driven

## 🛠️ Setup & Installation

### 1️⃣ Install Dependencies
Ensure you have Python installed, then install the required packages:
```bash
pip install openai requests python-dotenv
```

### 2️⃣ Configure Environment Variables
Create a `.env` file and add your credentials:
```env
OPENAI_API_KEY=your_openai_api_key
WORDPRESS_URL=https://yourwebsite.com
WORDPRESS_USERNAME=your_wp_username
WORDPRESS_PASSWORD=your_wp_password
```

### 3️⃣ Run the Script
Execute the bot with:
```bash
python ai_wordpress_bot.py
```

## 🚀 Usage
1. **Enter topics (comma-separated)**
   ```
   Enter topics (comma-separated): AI trends, Future of Robotics, HealthTech Advancements
   ```
2. The script will:
   - Generate an article for each topic 📝
   - Publish them directly to WordPress 🚀

## ⚡ Example Output
```bash
[✔] Generating article for: AI Trends
[✔] Publishing to WordPress...
[✔] Successfully posted: "The Future of AI Trends in 2025"
```

## 🎨 Customization
- Modify the AI model in `ai_wordpress_bot.py`
- Adjust the formatting, categories, or tags before publishing
- Add SEO enhancements for better ranking

## 🤝 Contributing
Feel free to fork, improve, and submit PRs. Let’s build the ultimate AI blogging tool together! 💡

## 📜 License
MIT License – Free to use and modify.