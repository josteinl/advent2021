import re

sang = """På låven sitter nissen med sin julegrøt,
Så god og søt, så god og søt.
Han nikker, og han smiler, og han er så glad,
For julegrøten vil han gjerne ha.
Men rundt omkring står alle de små rotter,
Og de skotter, og de skotter.
De vil så gjerne ha litt julegodter,
Og de danser, danser rundt i ring.
Men nissefar han truer med sin store skje,
Nei, bare se, og kom avsted.
For julegrøten min den vil jeg ha i fred,
Og ingen, ingen vil jeg dele med.
Men rottene de hopper, og de danser,
Og de svinser, og de svanser.
De klorer etter grøten og de stanser,
Og de står om nissen tett i ring.
Men nissefar han er en liten hissigpropp,
Og med sin kropp, han gjør et hopp.
Jeg henter katten hvis de ikke holder opp.
Når katten kommer, skal det nok bli stopp.
Da løper alle rottene så bange,
Ja, så bange, Ja, så bange,
De svinser og de svanser noen gange,
Og på en-to-tre så er de vekk, vekk vekk
"""

pattern = re.compile(r"([A-b])([v])\w+")


def main():
    ord = re.findall(r"([A-b])([v])\w+", sang)
    print(f"{ord=}")


if __name__ == "__main__":
    main()
