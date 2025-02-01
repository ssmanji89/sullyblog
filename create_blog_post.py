import os
import sys
from datetime import datetime
from github import Github
import openai

# Set your OpenAI API key and GitHub token as environment variables before running the script.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not OPENAI_API_KEY:
    sys.exit("Error: OPENAI_API_KEY environment variable not set.")
if not GITHUB_TOKEN:
    sys.exit("Error: GITHUB_TOKEN environment variable not set.")

# Replace with your GitHub repository in the format "username/repository"
REPO_NAME = "ssmanji89/jekyll-TeXt-theme.sulemanji.com"

# Configure OpenAI with your API key.
openai.api_key = OPENAI_API_KEY

def generate_blog_post(topic: str) -> str:
    """
    Generates a blog post in markdown format using OpenAI's API.
    The generated post includes YAML front matter with the specified author.
    
    Parameters:
        topic (str): The topic of the blog post.
    
    Returns:
        str: The blog post content in markdown format.
    """
    # Define the prompt instructing the model to include YAML front matter.
    prompt = (
        f"Write a detailed, well-structured blog post about '{topic}' in markdown format. "
        "Include a YAML front matter block at the top with keys for 'title', 'date', and 'author'. "
        "Set the 'author' to 'Suleman Shahnawaz Manji' and the 'date' to today's date. "
        "Ensure the content is formatted in markdown with appropriate headings, bullet points, and code blocks if necessary."
    )

    # Call the ChatCompletion endpoint using the new API.
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    # Extract the generated blog content from the API response.
    blog_content = response.choices[0].message.content.strip()
    return blog_content

def get_amazon_products(query: str):
    """
    Retrieves sample Amazon products based on the query.
    In a production environment, integrate with the Amazon Product Advertising API.
    """
    products = [
        {
            "title": "AI-Powered Smart Speaker",
            "url": "https://amzn.to/3EmhFPq"
        },
        {
            "title": "Next-Generation AI Robot",
            "url": "https://www.amazon.com/dp/B0DEF456?tag=sghpgs-20"
        }
    ]
    return products

def commit_blog_post_to_github(file_path: str, content: str, commit_message: str):
    """
    Commits the generated blog post to a GitHub repository.
    
    Parameters:
        file_path (str): The path (within the repository) where the file should be stored.
        content (str): The markdown content to commit.
        commit_message (str): A descriptive commit message.
    """
    # Authenticate with GitHub using PyGithub.
    github_client = Github(GITHUB_TOKEN)
    repo = github_client.get_repo(REPO_NAME)
    try:
        # Try to get the existing file from the repository.
        existing_file = repo.get_contents(file_path)
        # If found, update the file.
        repo.update_file(existing_file.path, commit_message, content, existing_file.sha)
        print(f"File '{file_path}' updated successfully in the repository.")
    except Exception as e:
        # If the file does not exist, create a new file.
        repo.create_file(file_path, commit_message, content)
        print(f"File '{file_path}' created successfully in the repository.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_blog_post.py '<blog_topic>'")
        sys.exit(1)

    # The blog topic is provided as a command-line argument.
    topic = sys.argv[1]

    # Generate the blog post content using the ChatGPT API.
    blog_post = generate_blog_post(topic)
    
    # Retrieve Amazon products based on the topic.
    products = get_amazon_products(topic)
    if products:
        blog_post += "\n\n## Recommended Products\n"
        for product in products:
            blog_post += f"- [{product['title']}]({product['url']})\n"

    # Create a filename using the current date and a sanitized version of the topic.
    date_str = datetime.now().strftime("%Y-%m-%d")
    safe_topic = topic.lower().replace(" ", "-")
    file_name = f"_posts/{date_str}-{safe_topic}.md"  # Ensure your repo has a 'posts' directory.

    # Define a commit message for GitHub.
    commit_message = f"Add new blog post on '{topic}'"

    # Commit the generated blog post to GitHub.
    commit_blog_post_to_github(file_name, blog_post, commit_message)
