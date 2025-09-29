#!/usr/bin/env python3
"""
Basic Usage Examples for Steampipe Query Executor

This script demonstrates how to use the SteampipeQueryExecutor class
to run queries and transform data.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from steampipe_query import SteampipeQueryExecutor
import pandas as pd

def example_github_analysis():
    """Example: Analyze GitHub repositories."""
    print("=== GitHub Repository Analysis ===")
    
    executor = SteampipeQueryExecutor()
    if not executor.connect():
        return
    
    try:
        # Get repositories as pandas DataFrame
        query = """
        SELECT 
            name,
            language,
            stargazers_count,
            forks_count,
            open_issues_count,
            created_at
        FROM github_repository
        WHERE language IS NOT NULL
        ORDER BY stargazers_count DESC
        LIMIT 10
        """
        
        result = executor.execute_query(query, "pandas")
        if result is not None:
            print("Top 10 repositories by stars:")
            print(result.to_string(index=False))
            
            # Data transformation example
            print("\nLanguage distribution:")
            lang_stats = result.groupby('language').agg({
                'stargazers_count': 'sum',
                'forks_count': 'sum',
                'name': 'count'
            }).rename(columns={'name': 'repo_count'})
            print(lang_stats)
    
    finally:
        executor.disconnect()

def example_confluence_content():
    """Example: Analyze Confluence content."""
    print("\n=== Confluence Content Analysis ===")
    
    executor = SteampipeQueryExecutor()
    if not executor.connect():
        return
    
    try:
        # Get pages as JSON
        query = """
        SELECT 
            title,
            space_name,
            author_display_name,
            created,
            version
        FROM confluence_page
        ORDER BY created DESC
        LIMIT 5
        """
        
        result = executor.execute_query(query, "json")
        if result:
            print("Recent Confluence pages:")
            print(result)
    
    finally:
        executor.disconnect()

def example_aws_inventory():
    """Example: AWS resource inventory."""
    print("\n=== AWS Resource Inventory ===")
    
    executor = SteampipeQueryExecutor()
    if not executor.connect():
        return
    
    try:
        # Get EC2 instances as CSV
        query = """
        SELECT 
            instance_id,
            instance_type,
            state_name,
            public_ip_address,
            launch_time
        FROM aws_ec2_instance
        WHERE state_name = 'running'
        ORDER BY launch_time DESC
        """
        
        result = executor.execute_query(query, "csv")
        if result:
            print("Running EC2 instances (CSV format):")
            print(result)
    
    finally:
        executor.disconnect()

def example_custom_transformation():
    """Example: Custom data transformation."""
    print("\n=== Custom Data Transformation ===")
    
    executor = SteampipeQueryExecutor()
    if not executor.connect():
        return
    
    try:
        # Get data and perform custom analysis
        query = """
        SELECT 
            name,
            stargazers_count,
            forks_count,
            open_issues_count,
            created_at
        FROM github_repository
        WHERE stargazers_count > 1000
        ORDER BY stargazers_count DESC
        LIMIT 20
        """
        
        result = executor.execute_query(query, "pandas")
        if result is not None:
            # Calculate engagement metrics
            result['engagement_score'] = (
                result['stargazers_count'] * 0.4 + 
                result['forks_count'] * 0.3 + 
                result['open_issues_count'] * 0.3
            )
            
            result['age_days'] = (pd.Timestamp.now() - pd.to_datetime(result['created_at'])).dt.days
            
            print("Top repositories with engagement metrics:")
            print(result[['name', 'stargazers_count', 'forks_count', 'engagement_score', 'age_days']].to_string(index=False))
    
    finally:
        executor.disconnect()

def main():
    """Run all examples."""
    print("Steampipe Query Executor - Usage Examples")
    print("=" * 50)
    
    # Run examples
    example_github_analysis()
    example_confluence_content()
    example_aws_inventory()
    example_custom_transformation()
    
    print("\n" + "=" * 50)
    print("Examples completed!")

if __name__ == "__main__":
    main()
