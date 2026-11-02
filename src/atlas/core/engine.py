from atlas.core.commands import handle_command


class AtlasEngine:

    def __init__(self):
        self.running = True

    def start(self):
        print("\nATLAS Core v0.1.0")
        print("Assistant initialisé.")
        print("Tapez /help pour commencer.\n")

        while self.running:
            try:
                user_input = input("You > ").strip()

                if not user_input:
                    continue

                if user_input.startswith("/"):
                    self.running = handle_command(user_input)
                else:
                    print("ATLAS > Intelligence conversationnelle en cours de développement.")

            except KeyboardInterrupt:
                print("\nArrêt demandé.")
                self.running = False
