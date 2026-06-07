from fastmcp import FastMCP
import random,json

mcp = FastMCP("Simple Calculator Server")

@mcp.tool
def add(a:int,b:int)->int:
    """Add 2 numbers together"""
    return a+b

@mcp.tool
def random_number(min: int = 1,max: int = 100) -> int:
    """Generate a random number within the given range"""
    return random.randint(min,max)

@mcp.resource("info://server")
def server_info()->str:
    """Get info. related to this server"""
    info = {
        "name":"Simple Calculator Server",
        "version":"1.0"
    }
    return json.dumps(info,indent=2)

if __name__=="__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)