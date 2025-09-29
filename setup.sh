#!/bin/bash

# Steampipe Playground Setup Script
# This script helps set up the Steampipe playground environment

set -e

echo "🚀 Setting up Steampipe Playground..."
echo "=================================="

# Check if Steampipe is installed
if ! command -v steampipe &> /dev/null; then
    echo "❌ Steampipe is not installed."
    echo "Please install Steampipe first:"
    echo "  macOS: brew install turbot/tap/steampipe"
    echo "  Linux: sudo /bin/sh -c \"\$(curl -fsSL https://steampipe.io/install/steampipe.sh)\""
    echo "  Windows: Invoke-Expression (Invoke-WebRequest -Uri \"https://steampipe.io/install/steampipe.ps1\").Content"
    exit 1
fi

echo "✅ Steampipe is installed"

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Make scripts executable
echo "🔧 Making scripts executable..."
chmod +x scripts/*.py
chmod +x examples/*.py

# Install Steampipe plugins
echo "🔌 Installing Steampipe plugins..."
steampipe plugin install github
steampipe plugin install confluence
steampipe plugin install aws
steampipe plugin install slack

echo "✅ Plugins installed"

# Create config directory if it doesn't exist
mkdir -p config

# Create example environment file
if [ ! -f .env ]; then
    echo "📝 Creating example .env file..."
    cat > .env << EOF
# GitHub Configuration
GITHUB_TOKEN=your_github_token_here

# Confluence Configuration
CONFLUENCE_URL=https://your-domain.atlassian.net
CONFLUENCE_USERNAME=your_email@domain.com
CONFLUENCE_API_TOKEN=your_api_token_here

# AWS Configuration
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_DEFAULT_REGION=us-east-1

# Slack Configuration
SLACK_TOKEN=xoxb-your-bot-token-here
EOF
    echo "⚠️  Please edit .env file with your actual credentials"
fi

# Start Steampipe service
echo "🚀 Starting Steampipe service..."
steampipe service start

echo ""
echo "🎉 Setup complete!"
echo "=================================="
echo ""
echo "Next steps:"
echo "1. Edit .env file with your actual API tokens and credentials"
echo "2. Test the setup by running: python scripts/steampipe_query.py --list-tables"
echo "3. Try a sample query: python scripts/query_runner.py queries/github/repositories.sql"
echo "4. Run examples: python examples/basic_usage.py"
echo ""
echo "For more information, see README.md"
