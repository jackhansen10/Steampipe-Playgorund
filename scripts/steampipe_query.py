#!/usr/bin/env python3
"""
Steampipe Query Executor

A Python script to execute SQL queries against Steampipe and return formatted results.
Supports various output formats and data transformation.
"""

import os
import sys
import argparse
import json
import pandas as pd
from typing import Dict, List, Any, Optional
import psycopg2
from psycopg2.extras import RealDictCursor
from tabulate import tabulate
from colorama import init, Fore, Style
from dotenv import load_dotenv

# Initialize colorama for cross-platform colored output
init()

# Load environment variables
load_dotenv()

class SteampipeQueryExecutor:
    """Execute SQL queries against Steampipe and format results."""
    
    def __init__(self, host: str = "localhost", port: int = 9193, database: str = "steampipe"):
        """Initialize the Steampipe connection."""
        self.host = host
        self.port = port
        self.database = database
        self.connection = None
        
    def connect(self) -> bool:
        """Establish connection to Steampipe."""
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user="steampipe"
            )
            print(f"{Fore.GREEN}✓ Connected to Steampipe at {self.host}:{self.port}{Style.RESET_ALL}")
            return True
        except psycopg2.Error as e:
            print(f"{Fore.RED}✗ Failed to connect to Steampipe: {e}{Style.RESET_ALL}")
            return False
    
    def disconnect(self):
        """Close the Steampipe connection."""
        if self.connection:
            self.connection.close()
            print(f"{Fore.YELLOW}Disconnected from Steampipe{Style.RESET_ALL}")
    
    def execute_query(self, query: str, output_format: str = "table") -> Optional[Any]:
        """Execute a SQL query and return formatted results."""
        if not self.connection:
            print(f"{Fore.RED}✗ Not connected to Steampipe{Style.RESET_ALL}")
            return None
        
        try:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                print(f"{Fore.CYAN}Executing query...{Style.RESET_ALL}")
                cursor.execute(query)
                
                # Fetch all results
                results = cursor.fetchall()
                
                if not results:
                    print(f"{Fore.YELLOW}No results returned{Style.RESET_ALL}")
                    return None
                
                # Convert to list of dictionaries
                data = [dict(row) for row in results]
                
                # Format output based on requested format
                if output_format == "json":
                    return self._format_json(data)
                elif output_format == "csv":
                    return self._format_csv(data)
                elif output_format == "pandas":
                    return self._format_pandas(data)
                else:  # table format
                    return self._format_table(data)
                    
        except psycopg2.Error as e:
            print(f"{Fore.RED}✗ Query execution failed: {e}{Style.RESET_ALL}")
            return None
    
    def _format_json(self, data: List[Dict]) -> str:
        """Format results as JSON."""
        return json.dumps(data, indent=2, default=str)
    
    def _format_csv(self, data: List[Dict]) -> str:
        """Format results as CSV."""
        if not data:
            return ""
        
        df = pd.DataFrame(data)
        return df.to_csv(index=False)
    
    def _format_pandas(self, data: List[Dict]) -> pd.DataFrame:
        """Format results as pandas DataFrame."""
        return pd.DataFrame(data)
    
    def _format_table(self, data: List[Dict]) -> str:
        """Format results as a table."""
        if not data:
            return "No data to display"
        
        df = pd.DataFrame(data)
        return tabulate(df, headers='keys', tablefmt='grid', showindex=False)
    
    def get_available_tables(self, plugin: Optional[str] = None) -> List[str]:
        """Get list of available tables, optionally filtered by plugin."""
        query = """
        SELECT table_name, table_schema 
        FROM information_schema.tables 
        WHERE table_schema NOT IN ('information_schema', 'pg_catalog')
        """
        
        if plugin:
            query += f" AND table_schema = '{plugin}'"
        
        query += " ORDER BY table_schema, table_name"
        
        results = self.execute_query(query, "pandas")
        if results is not None and not results.empty:
            return results['table_name'].tolist()
        return []
    
    def describe_table(self, table_name: str) -> Optional[str]:
        """Get table schema information."""
        query = f"""
        SELECT column_name, data_type, is_nullable, column_default
        FROM information_schema.columns
        WHERE table_name = '{table_name}'
        ORDER BY ordinal_position
        """
        
        return self.execute_query(query, "table")

def main():
    """Main function to handle command line arguments and execute queries."""
    parser = argparse.ArgumentParser(description="Execute SQL queries against Steampipe")
    parser.add_argument("query", nargs="?", help="SQL query to execute")
    parser.add_argument("-f", "--file", help="File containing SQL query")
    parser.add_argument("-o", "--output", choices=["table", "json", "csv", "pandas"], 
                       default="table", help="Output format")
    parser.add_argument("--host", default="localhost", help="Steampipe host")
    parser.add_argument("--port", type=int, default=9193, help="Steampipe port")
    parser.add_argument("--database", default="steampipe", help="Steampipe database")
    parser.add_argument("--list-tables", action="store_true", help="List available tables")
    parser.add_argument("--plugin", help="Filter tables by plugin name")
    parser.add_argument("--describe", help="Describe table schema")
    
    args = parser.parse_args()
    
    # Initialize executor
    executor = SteampipeQueryExecutor(args.host, args.port, args.database)
    
    # Connect to Steampipe
    if not executor.connect():
        sys.exit(1)
    
    try:
        # Handle different operations
        if args.list_tables:
            tables = executor.get_available_tables(args.plugin)
            if tables:
                print(f"\n{Fore.CYAN}Available tables:{Style.RESET_ALL}")
                for table in tables:
                    print(f"  • {table}")
            else:
                print(f"{Fore.YELLOW}No tables found{Style.RESET_ALL}")
        
        elif args.describe:
            result = executor.describe_table(args.describe)
            if result:
                print(f"\n{Fore.CYAN}Table schema for '{args.describe}':{Style.RESET_ALL}")
                print(result)
        
        elif args.query or args.file:
            # Get query from argument or file
            if args.file:
                if not os.path.exists(args.file):
                    print(f"{Fore.RED}✗ File not found: {args.file}{Style.RESET_ALL}")
                    sys.exit(1)
                with open(args.file, 'r') as f:
                    query = f.read()
            else:
                query = args.query
            
            # Execute query
            result = executor.execute_query(query, args.output)
            if result is not None:
                print(f"\n{Fore.CYAN}Query Results:{Style.RESET_ALL}")
                print(result)
        
        else:
            parser.print_help()
    
    finally:
        executor.disconnect()

if __name__ == "__main__":
    main()
