sangen = [
    "Spredt og i klynger der elven seg slynger",
    "ligger du Porsblomstens by.",
    "Dampfløyter hviner og sagblader synger",
    "muntert ved kveld og ved gry.",
    "",
    "ref.:",
    "",
    "For ditt vell vårt hjerte banker,",
    "og fra fremmed havn",
    "hjem til deg går våre tanker,",
    "kjært er Porsgrunns navn.",
    "",
    "Klang ifra ambolt og svingende hammer,",
    "kullrøyk fra piper mot sky,",
    "elven med tauing av flåter og prammer, -",
    "- baugen er vendt mot det ny.",
    "",
    "ref.",
    "",
    "Vendte vi hjemad der ute fra verden,",
    "Telemarks fjelde de blå",
    "vinket imot oss: velkommen fra ferden,",
    "- byen ved elven vi så.",
    "",
    "ref.",
]

arrangement = """Fra linje nummer 7: Tegn nummer så lang som linje nummer 8 er lang. 
Fra linje nummer 15: Tegn nummer så lang som linje nummer 20 er lang. 
Fra linje nummer 5: Tegn nummer så lang som linje nummer 4 er lang. 
Fra linje nummer 13: Tegn nummer så lang som linje nummer 5 er lang. 
Fra linje nummer 1: Tegn nummer så lang som linje nummer 10 er lang. 
Fra linje nummer 2: Tegn nummer så lang som linje nummer 1 er lang."""


def main():
    for line in arrangement.split("\n"):
        line_words = line.split()
        source_line_number = int(line_words[3][:-1])
        source_line = sangen[source_line_number]
        inspect_line_number = int(line_words[11])

        character_number = len(sangen[inspect_line_number])

        print(f"{source_line=} {character_number=} = {source_line[character_number]=}")

        # print(f"{source_line=}")  # [source_line_number-1]}")


if __name__ == "__main__":
    main()
