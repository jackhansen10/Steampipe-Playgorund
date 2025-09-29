-- Get list of repositories (no qualifier required)
-- This shows repositories you have access to
SELECT 
  name,
  full_name,
  description,
  url,
  owner_login,
  primary_language ->> 'name' as language,
  fork_count,
  stargazer_count,
  created_at,
  updated_at
FROM github_repository
WHERE full_name = 'jackhansen10/AI-Security-Playground'
ORDER BY full_name DESC
LIMIT 20;
