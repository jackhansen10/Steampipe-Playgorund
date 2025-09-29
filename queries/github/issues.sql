-- Get recent issues across repositories
SELECT 
    r.name as repository,
    i.number,
    i.title,
    i.state,
    i.user_login as author,
    i.created_at,
    i.updated_at,
    i.comments,
    i.html_url
FROM github_issue i
JOIN github_repository r ON i.repository_full_name = r.full_name
WHERE i.created_at > NOW() - INTERVAL '30 days'
ORDER BY i.created_at DESC
LIMIT 50;
