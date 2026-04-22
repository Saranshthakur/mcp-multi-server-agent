# MCP Multi-Server Agent with LangGraph

## Overview

This project demonstrates how to build a modular AI agent using Model Context Protocol (MCP), LangGraph, and LangChain MCP Adapters.

The system connects multiple tool servers (math + weather) to a single agent. The agent dynamically selects and invokes tools instead of hardcoding them.

---

## Architecture

User Query → LangGraph Agent → MCP Client → Tool Servers → Response

---

## Tech Stack

- Python
- LangGraph
- LangChain
- MCP (Model Context Protocol)
- FastMCP

---

## Project Structure

.
├── client.py  
├── mathserver.py  
├── weather.py  
├── main.py  
├── requirements.txt  
├── pyproject.toml  
├── .env.example  
└── README.md  

---

## Setup

### 1. Install dependencies

pip install -r requirements.txt

### 2. Add API key

Create `.env` file:

OPENAI_API_KEY=your_key_here

---

## Run

Start weather server:

python weather.py

Run agent:

python main.py

---

## Example Queries

- What is 10 + 20?
- Multiply 5 and 6
- What is the weather in Chicago?

---

## Notes

- Weather API is mocked
- No memory or persistence yet
- Focus is on MCP integration + agent orchestration
