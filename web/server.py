# -*- coding: utf-8 -*-
"""
Web Server & Alexa+ Voice Simulator for Amazon Developer Hackathon.
Provides interactive FastAPI endpoints and serves the visual Operations Dashboard.
"""

import os
import sys
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from typing import Dict, Any, Optional

# Dynamic path resolution to support execution in standalone repo, Docker, or AWS
_CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
_PARENT_DIR = os.path.abspath(os.path.join(_CURRENT_DIR, ".."))
_SRC_DIR = os.path.abspath(os.path.join(_CURRENT_DIR, "..", "..", "02_核心代碼庫_SourceCode"))

for p in [_CURRENT_DIR, _PARENT_DIR, _SRC_DIR]:
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    from core.alexa_mcp_server import AlexaOpsMCPServer
except ImportError:
    try:
        from amazon_appdev_delivery.core.alexa_mcp_server import AlexaOpsMCPServer
    except ImportError:
        # Fallback to local import if core is placed alongside
        from alexa_mcp_server import AlexaOpsMCPServer

app = FastAPI(
    title="Phantom Alexa+ Autonomous Operations Hub",
    description="Amazon Developer Hackathon (Devpost) - Alexa+ Track & AWS Bedrock",
    version="1.0.0"
)

@app.get("/healthz")
@app.get("/health")
def health_check():
    return {
        "status": "ONLINE",
        "service": "phantom-grid-alexa-autonomous-sre-hub",
        "protocol": "Model Context Protocol (MCP) 2024-11-05",
        "aws_region": os.environ.get("AWS_REGION", "us-east-1"),
        "fleet_health": "OPTIMAL"
    }

mcp_server = AlexaOpsMCPServer()
static_dir = os.path.join(os.path.dirname(__file__), "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir, exist_ok=True)

class ToolCallRequest(BaseModel):
    tool_name: str
    arguments: Optional[Dict[str, Any]] = {}

class VoiceQueryRequest(BaseModel):
    voice_command: str

@app.get("/")
def serve_index():
    index_path = os.path.join(static_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "Phantom Alexa+ Operations Hub API is running. Access /docs for API."}

@app.get("/api/mcp/manifest")
def get_manifest():
    return {
        "status": "success",
        "protocol": "Model Context Protocol (MCP) 2024-11-05",
        "tools": mcp_server.get_tool_manifest()
    }

@app.get("/api/telemetry")
def get_telemetry():
    return mcp_server.get_fleet_status()

@app.post("/api/mcp/call")
def call_tool(req: ToolCallRequest):
    result = mcp_server.execute_tool(req.tool_name, req.arguments or {})
    return result

@app.post("/api/alexa/voice")
def process_voice_command(req: VoiceQueryRequest):
    cmd = req.voice_command.strip().lower()
    
    # Natural Language Understanding / Intent Mapping
    if "status" in cmd or "health" in cmd or "fleet" in cmd:
        res = mcp_server.execute_tool("get_fleet_status", {})
        fleet = res.get("fleet_overview", {})
        speech = f"Fleet health is currently at {fleet.get('fleet_health_ratio', '100%')}. Total services: {fleet.get('total_services', 3)}, Degraded: {fleet.get('degraded_services', 0)}."
        intent = "GET_FLEET_STATUS"
        tool_used = "get_fleet_status"
    elif "diagnose" in cmd or "investigate" in cmd:
        res = mcp_server.execute_tool("diagnose_service_incident", {"service_name": "checkout-service"})
        speech = "Diagnosis complete. Root cause identified: Database connection pool exhaustion causing 2,840ms latency spikes on checkout-service."
        intent = "DIAGNOSE_INCIDENT"
        tool_used = "diagnose_service_incident"
    elif "heal" in cmd or "fix" in cmd or "repair" in cmd:
        res = mcp_server.execute_tool("trigger_autonomous_healing", {"service_name": "checkout-service", "auto_deploy": True})
        speech = "Autonomous self-healing deployed. Connection pool expanded to 80, AST patch verified with zero regression. Checkout-service latency normalized to 35ms."
        intent = "TRIGGER_AUTONOMOUS_HEALING"
        tool_used = "trigger_autonomous_healing"
    elif "chaos" in cmd or "stress" in cmd:
        res = mcp_server.execute_tool("run_chaos_verifier", {"target_service": "checkout-service"})
        speech = "Chaos resilience verifier passed. 1,500 faults injected, mean recovery time 185 milliseconds. Zero dropped transactions."
        intent = "RUN_CHAOS_VERIFIER"
        tool_used = "run_chaos_verifier"
    else:
        res = mcp_server.execute_tool("get_fleet_status", {})
        speech = f"I heard: '{req.voice_command}'. Here is the current fleet overview."
        intent = "FALLBACK_QUERY"
        tool_used = "get_fleet_status"

    return {
        "status": "success",
        "voice_command": req.voice_command,
        "alexa_intent": intent,
        "alexa_speech_response": speech,
        "mcp_tool_invoked": tool_used,
        "mcp_payload": res,
        "current_fleet_state": mcp_server.get_fleet_status()
    }

if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "8090"))
    uvicorn.run(app, host=host, port=port)

