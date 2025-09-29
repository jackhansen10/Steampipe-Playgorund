-- Get S3 buckets with their configuration and policies
SELECT 
    name,
    region,
    creation_date,
    versioning_enabled,
    versioning_mfa_delete,
    public_access_block_configuration,
    server_side_encryption_configuration,
    tags,
    _ctx_connection_name
FROM aws_s3_bucket
ORDER BY creation_date DESC;
