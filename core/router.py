class MAXRouter:

    def route(self, user_message: str) -> str:
        message = user_message.lower().strip()

        # Memory-related requests
        memory_keywords = [
            "remember",
            "don't forget",
            "do not forget",
            "save this",
            "store this",
            "what did i tell you"
        ]

        if any(keyword in message for keyword in memory_keywords):
            return "memory"

        # Computer-control requests
        computer_keywords = [
            "open chrome",
            "open browser",
            "open notepad",
            "open calculator",
            "close chrome",
            "close browser",
            "open vs code",
            "shutdown",
            "restart my computer"
        ]

        if any(keyword in message for keyword in computer_keywords):
            return "computer"

        # Web-related requests
        web_keywords = [
            "search the web",
            "search online",
            "search internet",
            "latest news",
            "today's news",
            "current news",
            "what is happening today",
            "latest",
            "current price"
        ]

        if any(keyword in message for keyword in web_keywords):
            return "web"

        # Normal conversation
        return "conversation"