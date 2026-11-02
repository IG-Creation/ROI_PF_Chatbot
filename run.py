#!/usr/bin/env python
"""
Main launcher for ROI & PF Chatbot.
Usage:
    python run.py          -> Launches Web App & Dashboard on http://127.0.0.1:8000
    python run.py --cli    -> Runs interactive CLI Chatbot terminal
"""

import sys
import argparse
import uvicorn
from app.config import config
from app.chatbot.handler import handle_chat_message


def run_cli():
    print("=" * 65)
    print("🤖 ROI & PF Managed Pricing Chatbot (CLI Mode)")
    print("=" * 65)
    print("Type your questions (e.g. 'Calculate ROI for 20k cost and 35k return')")
    print("Type 'exit' or 'quit' to leave.\n")

    session_id = "cli_session"
    while True:
        try:
            user_input = input("\nYou > ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("exit", "quit", "q"):
                print("Goodbye!")
                break

            response = handle_chat_message(user_input, session_id)
            print("\nBot >")
            print(response.message)
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            break


def run_server():
    print("=" * 65)
    print("🚀 Starting ROI & PF Chatbot Server")
    print(f"👉 Local URL: http://{config.host}:{config.port}")
    print("=" * 65)
    uvicorn.run(
        "app.main:app",
        host=config.host,
        port=config.port,
        reload=config.debug,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ROI & PF Chatbot")
    parser.add_argument("--cli", action="store_true", help="Run interactive terminal CLI chatbot")
    parser.add_argument("--host", default=config.host, help="Bind host for web server")
    parser.add_argument("--port", type=int, default=config.port, help="Port for web server")
    args = parser.parse_args()

    if args.cli:
        run_cli()
    else:
        config.host = args.host
        config.port = args.port
        run_server()
