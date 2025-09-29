-- Get Confluence spaces information
SELECT 
    id,
    key,
    name,
    type,
    description,
    homepage_id,
    created,
    creator_display_name,
    _ctx_connection_name
FROM confluence_space
ORDER BY created DESC;
