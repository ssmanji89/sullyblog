# Suleman Shahnawaz Manji Blog

This repository hosts a blog powered by ChatGPT-generated posts and is served via GitHub Pages.

## Setup

1. **Environment Variables:**
   Set the following environment variables with your OpenAI API key and GitHub token:

   ```bash
   export OPENAI_API_KEY="your_openai_api_key"
   export GITHUB_TOKEN="your_github_personal_access_token"
   ```

2. **Generating a Blog Post:**
   Use the provided Python script to generate and commit a new blog post. For example:

   ```bash
   python create_blog_post.py "Blog Post Title"
   ```

   This script uses the OpenAI API to generate the content (including YAML front matter) and commits the post to the repository under the `posts/` directory.

3. **Local Development:**
   To preview your site locally:
   - Ensure you have [Ruby](https://www.ruby-lang.org/en/) and [Bundler](https://bundler.io/) installed.
   - Install the GitHub Pages dependencies by running:
     ```bash
     bundle install
     ```
   - Serve the site locally:
     ```bash
     bundle exec jekyll serve
     ```
   - Open your browser and navigate to `http://localhost:4000`.

## Repository Structure

- **\_config.yml**: Jekyll configuration file.
- **index.md**: Home page of your blog.
- **Gemfile**: Ruby dependencies for GitHub Pages.
- **posts/**: Directory where blog posts are stored.
  - **.keep**: An empty file to ensure the directory is tracked by Git.
- **create_blog_post.py**: Python script to generate and commit blog posts.

Enjoy your automated blog!
