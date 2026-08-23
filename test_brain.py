from core.brain import MAXBrain


brain = MAXBrain()

test_messages = [
    "Hello MAX",
    "What is Python?",
    "Search the latest AI news",
    "Open Chrome",
    "Remember that my project is called MAX"
]

for message in test_messages:
    result = brain.understand(message)

    print(f"\nUser: {message}")
    print(f"Intent: {result['intent']}")