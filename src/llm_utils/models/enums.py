from enum import Enum

class LLMClients(str, Enum):
    ollama = "ollama"
    openai = "openai"

class EmbeddingsClients(str, Enum):
    openai = "openai"
    ollama = "ollama"
