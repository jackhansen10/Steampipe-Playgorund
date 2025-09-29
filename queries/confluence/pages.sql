-- Get all Confluence pages with metadata
SELECT 
    id,
    title,
    type,
    status,
    space_key,
    space_name,
    author_id,
    author_display_name,
    created,
    version,
    version_created,
    version_created_by,
    body_storage_value,
    body_storage_representation,
    extensions_position,
    _ctx_connection_name
FROM confluence_page
ORDER BY created DESC
LIMIT 50;
