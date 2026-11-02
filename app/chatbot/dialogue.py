"""
Dialogue context and conversational memory management.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field
import time


class Message(BaseModel):
    role: str  # 'user' | 'assistant' | 'system'
    content: str
    timestamp: float = Field(default_factory=time.time)
    data: Optional[Dict] = None


class SessionState(BaseModel):
    session_id: str
    messages: List[Message] = []
    last_context: Dict = {}
    created_at: float = Field(default_factory=time.time)
    updated_at: float = Field(default_factory=time.time)

    def add_message(self, role: str, content: str, data: Optional[Dict] = None):
        self.messages.append(Message(role=role, content=content, data=data))
        self.updated_at = time.time()

    def update_context(self, updates: Dict):
        self.last_context.update({k: v for k, v in updates.items() if v is not None})
        self.updated_at = time.time()


class SessionManager:
    def __init__(self):
        self._sessions: Dict[str, SessionState] = {}

    def get_or_create(self, session_id: str) -> SessionState:
        if not session_id or session_id not in self._sessions:
            sid = session_id or "default_session"
            self._sessions[sid] = SessionState(session_id=sid)
        return self._sessions[session_id]

    def clear(self, session_id: str):
        if session_id in self._sessions:
            del self._sessions[session_id]


session_manager = SessionManager()
