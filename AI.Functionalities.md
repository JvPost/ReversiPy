|> - AI
    Go's 3 componenten:
        1. Policy network
            1.1 Getraind op games van hoog niveau
        2. Value network
            2.1 Valueerd het bord
        3. Tree search 

        Werkt op de volgende manier:
        1. Scant het bord en bedenkt waar hij een steen kan plaatsen, voor iedere keus geeft 
        het een kans van winnen.
        Voor de hoogste keuzes wordt een boom gemaakt van mogelijke volgende moves.
        
        2. Berekent voor elke volgende movie weer hoe hoog de kans is dat hij gaat winnen 
        (recursie)?

        3. Hij probeert de kans van winnen zo veel mogelijk te vergroten, maar het maakt hem
        niet uit hoe hard hij wint.


    [] - Next best move search.
        [ ] - Vooruit kijken (advances search tree)

