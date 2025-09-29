-- Get detailed information for a specific repository
-- Replace 'turbot/steampipe' with the repository you want to query
SELECT 
  name,
  full_name,
  description,
  url,
  owner_login,
  primary_language ->> 'name' as language,
  fork_count,
  stargazer_count,
  watcher_count,
  open_issues_count,
  created_at,
  updated_at,
  pushed_at,
  disk_usage,
  license_info ->> 'spdx_id' as license,
  is_private,
  is_fork,
  is_archived,
  is_disabled
FROM github_repository
WHERE full_name = 'turbot/steampipe'  -- Replace with your target repository
