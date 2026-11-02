from atlas.core.diagnostics import system_info


COMMANDS = {
    "/help": "Afficher les commandes disponibles",
    "/about": "Informations sur ATLAS",
    "/version": "Afficher la version",
    "/sysinfo": "Afficher les informations système",
    "/clear": "Effacer le terminal",
    "/exit": "Quitter ATLAS",
}


def handle_command(command: str):

    command = command.strip()

    if command == "/help":
        print("\nCommandes disponibles :")

        for name, description in COMMANDS.items():
            print(f"{name:<12} {description}")

    elif command == "/about":
        print("\nATLAS")
        print("Autonomous Technology & Logic Assistance System")
        print("Assistant personnel intelligent en développement.")

    elif command == "/version":
        print("\nATLAS version 0.1.0")

    elif command == "/sysinfo":
        system_info()

    elif command == "/clear":
        print("\033[2J\033[H", end="")

    elif command == "/exit":
        print("\nArrêt d'ATLAS.")
        return False

    else:
        print(f"\nCommande inconnue : {command}")
        print("Utilisez /help.")

    return True
