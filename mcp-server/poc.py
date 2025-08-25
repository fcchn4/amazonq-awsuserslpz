"""
URL API Example:
- https://www.swapi.tech/
"""

import httpx
import asyncio
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Inicialize Fast MCP server
mcp = FastMCP("github")

# Constants Variables
API_URL = "https://www.swapi.tech/api/people"


@mcp.tool()
def connection() -> str:
    """PoC: Basic MCP server connection"""
    return "Github MCP server is running!"


@mcp.tool()
def get_api_url() -> str:
    """PoC: Basic MCP server connection"""
    return f"{API_URL}"


@mcp.tool()
async def get_people(people_number: int) -> dict[str, Any]:
    """
    PoC: Get API JSON output
    """

    URL_PEOPLE = f"{API_URL}/{people_number}"

    if not people_number:
        return {"error": "Invalid people number"}

    headers = {
        "User-Agent": "app/1.0",
        "Content-Type": "application/json",
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(URL_PEOPLE, headers=headers, timeout=30.0)

            response.raise_for_status()
            return response.json()

    except httpx.HTTPStatusError as e:
        return {"error": f"HTTP Error {e.response.status_code}", "message": str(e)}
    except Exception as e:
        return {"error": "Request failed", "message": str(e)}


def main():
    """Entry point for the MCP server"""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
