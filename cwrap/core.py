from pyfiglet import Figlet


def do_figlet(text: str, font: str, language):
    fig = Figlet(font=font)
    return fig.renderText(text)
