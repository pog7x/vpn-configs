README_TEMPLATE = """\
# VPN Configs

[![Frequent Update](https://github.com/{repo}/actions/workflows/frequent_update.yml/badge.svg)](https://github.com/{repo}/actions/workflows/frequent_update.yml)

Automated aggregator that collects free VPN configuration files from multiple \
open-source repositories across GitHub and mirrors them into a single, \
regularly updated location.

## How It Works

1. A GitHub Actions workflow runs **every hour** on a cron schedule.
2. The script reads a curated list of source URLs from `urls.txt`.
3. Each source is fetched, deduplicated via MD5 hash comparison, and saved \
to the `githubmirror/` directory.
4. The table below is regenerated with the latest update timestamps.

## Configs

{configs_table}

## Quick Start

```bash
# Clone the repository
git clone https://github.com/{repo}.git
cd {repo_name}

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export GH_TOKEN="your_github_token"
export REPO_NAME="owner/repo"

# Run
python main.py
```

## Requirements

| Package | Purpose |
|---------|---------|
| [aiohttp](https://pypi.org/project/aiohttp/) | Async HTTP requests |
| [aiofiles](https://pypi.org/project/aiofiles/) | Async file I/O |
| [PyGithub](https://pypi.org/project/PyGithub/) | GitHub API integration |
| [py-markdown-table](https://pypi.org/project/py-markdown-table/) | Markdown table generation |

## Disclaimer

This project is provided for **educational and informational purposes only**. \
The maintainers do not host, create, or endorse any VPN configurations — all \
files are mirrored from publicly available open-source repositories. Use at \
your own risk and in compliance with your local laws.
"""
