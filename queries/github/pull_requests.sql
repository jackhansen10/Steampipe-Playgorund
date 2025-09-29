-- Get recent pull requests for a specific repository
-- Replace 'turbot/steampipe' with the repository you want to query
SELECT 
    repository_full_name,
    number,
    title,
    state,
    user_login as author,
    created_at,
    updated_at,
    merged_at,
    comments,
    additions,
    deletions,
    changed_files,
    html_url
FROM github_pull_request
WHERE repository_full_name = 'turbot/steampipe'  -- Replace with your target repository
  AND created_at > NOW() - INTERVAL '30 days'
ORDER BY created_at DESC
LIMIT 30;
