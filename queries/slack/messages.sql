-- Get recent Slack messages from channels
SELECT 
    c.name as channel_name,
    m.ts,
    m.user,
    m.text,
    m.type,
    m.subtype,
    m.thread_ts,
    m.reply_count,
    m.reply_users_count,
    m.reactions,
    m.attachments,
    m.files,
    _ctx_connection_name
FROM slack_message m
JOIN slack_conversation c ON m.channel = c.id
WHERE m.ts > (EXTRACT(EPOCH FROM NOW()) - 86400) * 1000000  -- Last 24 hours
ORDER BY m.ts DESC
LIMIT 100;
