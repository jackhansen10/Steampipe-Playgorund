# Steampipe Playground

A comprehensive playground environment for testing and experimenting with [Steampipe](https://hub.steampipe.io/) queries across multiple data sources including Confluence, GitHub, AWS, and Slack.

## 🚀 Features

- **Multi-source queries**: Pre-built queries for GitHub, Confluence, AWS, and Slack
- **Python integration**: Execute queries programmatically with data transformation capabilities
- **Multiple output formats**: Table, JSON, CSV, and pandas DataFrame
- **Easy setup**: Simple installation and configuration
- **Example scripts**: Ready-to-run examples demonstrating data analysis and transformation

## 📁 Project Structure

```
Steampipe-Playgorund/
├── scripts/                 # Python query execution scripts
│   ├── steampipe_query.py   # Main query executor with full features
│   └── query_runner.py      # Simple query runner
├── queries/                 # SQL query files organized by source
│   ├── github/             # GitHub-related queries
│   ├── confluence/         # Confluence queries
│   ├── aws/               # AWS resource queries
│   └── slack/             # Slack workspace queries
├── examples/               # Example Python scripts
│   └── basic_usage.py     # Usage examples and data transformation
├── config/                # Configuration files
├── requirements.txt       # Python dependencies
├── setup.sh              # Automated setup script
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## 🛠️ Installation

### Quick Setup (Recommended)

Use the automated setup script to get started quickly:

```bash
# Clone the repository
git clone <your-repo-url>
cd Steampipe-Playgorund

# Run the setup script
./setup.sh
```

The setup script will:
- Check if Steampipe is installed
- Install Python dependencies
- Install required Steampipe plugins
- Create configuration files
- Start the Steampipe service

### Manual Installation

### 1. Install Steampipe

Follow the [official Steampipe installation guide](https://steampipe.io/docs/install) for your operating system.

**macOS (using Homebrew):**
```bash
brew install turbot/tap/steampipe
```

**Linux:**
```bash
sudo /bin/sh -c "$(curl -fsSL https://steampipe.io/install/steampipe.sh)"
```

**Windows:**
```powershell
Invoke-Expression (Invoke-WebRequest -Uri "https://steampipe.io/install/steampipe.ps1").Content
```

### 2. Install Required Plugins

```bash
# Install GitHub plugin
steampipe plugin install github

# Install Confluence plugin
steampipe plugin install confluence

# Install AWS plugin
steampipe plugin install aws

# Install Slack plugin
steampipe plugin install slack
```

### 3. Configure Plugins

#### GitHub Configuration
```bash
# Set your GitHub token
export GITHUB_TOKEN=your_github_token_here

# Or add to ~/.steampipe/config/github.spc
```

#### Confluence Configuration
```bash
# Set Confluence credentials
export CONFLUENCE_URL=https://your-domain.atlassian.net
export CONFLUENCE_USERNAME=your_email@domain.com
export CONFLUENCE_API_TOKEN=your_api_token

# Or add to ~/.steampipe/config/confluence.spc
```

#### AWS Configuration
```bash
# Configure AWS credentials (standard AWS methods)
aws configure
# Or set environment variables
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-east-1
```

#### Slack Configuration
```bash
# Set Slack token
export SLACK_TOKEN=xoxb-your-bot-token

# Or add to ~/.steampipe/config/slack.spc
```

### 4. Install Python Dependencies

```bash
pip3 install -r requirements.txt
```

### 5. Start Steampipe Service

```bash
steampipe service start
```

## 🎯 Usage

### Quick Start

1. **Start Steampipe service:**
   ```bash
   steampipe service start
   ```

2. **Configure your credentials** in the `.env` file (created by setup script)

3. **Test the setup:**
   ```bash
   python3 scripts/steampipe_query.py --list-tables
   ```

4. **Run a pre-built query:**
   ```bash
   python3 scripts/query_runner.py queries/github/repositories.sql
   ```

5. **Execute a custom query:**
   ```bash
   python3 scripts/steampipe_query.py "SELECT * FROM github_repository LIMIT 5"
   ```

6. **Run examples:**
   ```bash
   python3 examples/basic_usage.py
   ```

### Python Scripts

#### Main Query Executor (`scripts/steampipe_query.py`)

The main script provides comprehensive query execution capabilities:

```bash
# Execute a query with table output (default)
python3 scripts/steampipe_query.py "SELECT name, stargazers_count FROM github_repository ORDER BY stargazers_count DESC LIMIT 10"

# Execute a query with JSON output
python3 scripts/steampipe_query.py "SELECT * FROM confluence_page LIMIT 5" --output json

# Execute a query from a file
python3 scripts/steampipe_query.py --file queries/aws/ec2_instances.sql --output csv

# List available tables
python3 scripts/steampipe_query.py --list-tables

# List tables for a specific plugin
python3 scripts/steampipe_query.py --list-tables --plugin github

# Describe a table schema
python3 scripts/steampipe_query.py --describe github_repository
```

#### Simple Query Runner (`scripts/query_runner.py`)

A simplified interface for running queries from files:

```bash
# Run a query file with default table output
python3 scripts/query_runner.py queries/github/repositories.sql

# Run a query file with JSON output
python3 scripts/query_runner.py queries/confluence/pages.sql json
```

### Example Queries

#### GitHub Queries
- **Repositories**: Get repository information with stars, forks, and metadata
- **Issues**: Recent issues across repositories
- **Pull Requests**: Recent pull requests with status information

#### Confluence Queries
- **Pages**: All Confluence pages with metadata
- **Spaces**: Confluence spaces information

#### AWS Queries
- **EC2 Instances**: Running instances with configuration details
- **S3 Buckets**: Bucket information with security settings

#### Slack Queries
- **Channels**: Channel information with member counts
- **Messages**: Recent messages from channels

### Data Transformation Examples

See `examples/basic_usage.py` for comprehensive examples of:
- Querying data from multiple sources
- Transforming data with pandas
- Calculating custom metrics
- Exporting results in different formats

```bash
python3 examples/basic_usage.py
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# GitHub
GITHUB_TOKEN=your_github_token

# Confluence
CONFLUENCE_URL=https://your-domain.atlassian.net
CONFLUENCE_USERNAME=your_email@domain.com
CONFLUENCE_API_TOKEN=your_api_token

# AWS
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=us-east-1

# Slack
SLACK_TOKEN=xoxb-your-bot-token
```

### Steampipe Configuration Files

Alternatively, configure plugins using Steampipe config files in `~/.steampipe/config/`:

**github.spc:**
```hcl
connection "github" {
  plugin = "github"
  token  = "your_github_token"
}
```

**confluence.spc:**
```hcl
connection "confluence" {
  plugin = "confluence"
  url    = "https://your-domain.atlassian.net"
  username = "your_email@domain.com"
  api_token = "your_api_token"
}
```

## 📊 Output Formats

The query executor supports multiple output formats:

- **Table**: Formatted table output (default)
- **JSON**: JSON format for programmatic use
- **CSV**: Comma-separated values for spreadsheet import
- **Pandas**: Returns pandas DataFrame for data analysis

## 🚨 Troubleshooting

### Common Issues

1. **Connection refused**: Ensure Steampipe service is running
   ```bash
   steampipe service start
   ```

2. **Authentication errors**: Verify your API tokens and credentials are set correctly

3. **Plugin not found**: Install the required plugin
   ```bash
   steampipe plugin install <plugin_name>
   ```

4. **Permission denied**: Check file permissions
   ```bash
   chmod +x scripts/*.py
   ```

5. **Python command not found**: Use python3 instead of python
   ```bash
   python3 scripts/steampipe_query.py --list-tables
   ```

### Getting Help

- Check [Steampipe documentation](https://steampipe.io/docs)
- Visit [Steampipe Hub](https://hub.steampipe.io/) for plugin details
- Review plugin-specific documentation for configuration options

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your queries or improvements
4. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [Steampipe](https://steampipe.io/) for the amazing query engine
- [Turbot](https://turbot.com/) for maintaining Steampipe
- The open-source community for the various plugins
