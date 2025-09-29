-- Get all repositories with basic information
SELECT 
    name,
    full_name,
    description,
    html_url,
    language,
    stargazers_count,
    forks_count,
    open_issues_count,
    created_at,
    updated_at,
    pushed_at,
    size,
    default_branch
FROM github_repository
ORDER BY stargazers_count DESC
LIMIT 20;
