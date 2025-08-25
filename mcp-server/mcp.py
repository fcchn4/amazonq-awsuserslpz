import httpx
import asyncio
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Inicialize Fast MCP server
mcp = FastMCP("github")

# Constants Variables
"""
GIT_URL = "https://github.com"
GIT_API_PATH = "rest/api/1.0"
GIT_USER_AGENT = "app/1.0"
GIT_API_TOKEN = "This_is_a_token!"
"""


@mcp.tool()
def connection() -> str:
    """Test: Basic MCP server connection"""
    return "Bitbucket MCP server is running!"


def main():
    """Entry point for the MCP server"""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
