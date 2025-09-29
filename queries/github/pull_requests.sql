-- Get recent pull requests with status information
SELECT 
    r.name as repository,
    pr.number,
    pr.title,
    pr.state,
    pr.user_login as author,
    pr.created_at,
    pr.updated_at,
    pr.merged_at,
    pr.comments,
    pr.additions,
    pr.deletions,
    pr.changed_files,
    pr.html_url
FROM github_pull_request pr
JOIN github_repository r ON pr.repository_full_name = r.full_name
WHERE pr.created_at > NOW() - INTERVAL '30 days'
ORDER BY pr.created_at DESC
LIMIT 30;
