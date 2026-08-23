from core.agent import MAXAgent

max_agent = MAXAgent()

response = max_agent.chat("Hello MAX, introduce yourself.")

print("\nMAX:")
print(response)