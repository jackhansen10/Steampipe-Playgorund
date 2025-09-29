-- Get Slack channels with member information
SELECT 
    id,
    name,
    is_channel,
    is_group,
    is_im,
    is_mpim,
    is_private,
    is_archived,
    is_general,
    created,
    creator,
    is_member,
    is_pending,
    is_muted,
    num_members,
    topic_value,
    purpose_value,
    _ctx_connection_name
FROM slack_conversation
WHERE is_channel = true
ORDER BY num_members DESC;
