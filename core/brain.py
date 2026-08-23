from core.router import MAXRouter


class MAXBrain:
    def __init__(self):
        self.router = MAXRouter()

    def understand(self, user_message: str) -> dict:
        intent = self.router.route(user_message)

        return {
            "message": user_message,
            "intent": intent
        }