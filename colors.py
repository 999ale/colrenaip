# colors.py
class Colrenaip:
    COLORS = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }

    def __getattr__(self, color_name):
        """Ritorna una funzione che applica il colore scelto al testo."""
        if color_name not in self.COLORS:
            raise AttributeError(f"{color_name} non è un colore valido.")

        def colorize(text):
            return f"{self.COLORS[color_name]}{text}{self.COLORS['reset']}"
        
        return colorize

# Definisci una funzione per interpretare la sintassi "colore.testo"
def print_colored(text):
    try:
        color, message = text.split(".", 1)
        color_method = getattr(Colrenaip(), color)
        print(color_method(message))
    except (ValueError, AttributeError):
        print("Invalid format. Use 'color.text'.")
