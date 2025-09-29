-- Get EC2 instances with their current state and configuration
SELECT 
    instance_id,
    instance_type,
    state_name,
    state_code,
    public_ip_address,
    private_ip_address,
    vpc_id,
    subnet_id,
    availability_zone,
    launch_time,
    image_id,
    key_name,
    security_groups,
    tags,
    _ctx_connection_name
FROM aws_ec2_instance
ORDER BY launch_time DESC;
