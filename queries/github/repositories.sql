-- Get all repositories with basic information
-- Note: This query requires a specific repository full_name
-- Replace 'your-username/your-repo' with an actual repository
SELECT 
  name,
  full_name,
  node_id,
  id,
  created_at,
  updated_at,
  disk_usage,
  owner_login,
  primary_language ->> 'name' as language,
  fork_count,
  stargazer_count,
  url,
  license_info ->> 'spdx_id' as license,
  description
FROM github_repository
WHERE full_name = 'jackhansen10/AI-Security-Playground'  -- Replace with actual repo
LIMIT 20;
