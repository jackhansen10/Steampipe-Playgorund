#!/usr/bin/env python3
"""
Simple Query Runner

A simplified interface for running common Steampipe queries.
"""

import os
import sys
from steampipe_query import SteampipeQueryExecutor

def run_query_from_file(query_file: str, output_format: str = "table", save_csv: bool = True):
    """Run a query from a file and display results."""
    if not os.path.exists(query_file):
        print(f"Query file not found: {query_file}")
        return
    
    with open(query_file, 'r') as f:
        query = f.read()
    
    executor = SteampipeQueryExecutor()
    if executor.connect():
        try:
            result = executor.execute_query(query, output_format, save_csv)
            if result:
                print(result)
        finally:
            executor.disconnect()

def main():
    """Main function for simple query execution."""
    if len(sys.argv) < 2:
        print("Usage: python query_runner.py <query_file> [output_format] [--no-csv]")
        print("Output formats: table, json, csv, pandas")
        print("Use --no-csv to disable automatic CSV saving")
        sys.exit(1)
    
    query_file = sys.argv[1]
    output_format = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith('--') else "table"
    save_csv = "--no-csv" not in sys.argv
    
    run_query_from_file(query_file, output_format, save_csv)

if __name__ == "__main__":
    main()
