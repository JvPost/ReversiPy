[] DevOps
    [X] - Gulp Folder structuur uitzoeken. (Dist folder is voor productie)
    [X] - Gulp auto prefixer. (last 2 versions)
    [X] - Gulp build functionaliteit.
        [X] - JS
        [X] - css
        [X] - html
    [X] - Gulp (& flask) browsersync.
    [ ] - API en Game modules uit elkaar trekken.
    [?] - Gulpify (remove jinja functionalities)
        [x] - render_template veranderen naar send_file.
        [] - Jinja2 handlebars weghalen.
        [] - Static en Templates weghalen.
        [] - 1 dist en 1 src folder.
        [] - Gulp taken aanpassen.
            [] - File paths aanpassen.
            [] - Alles concatteren (css & js).
            [] - Verplaatsen naar dist op .on('change', () => {});
        [] - Maak van spel een popup.


[] Speler
    [ ] - Als speler wil ik dat ik automatisch een spel join
        [ ] - Splashscreen wordt laten zien tijdens het wachten op een andere speler.
        [ ] - Mogelijkheid om het tegen een (getrainde) AI op te nemen.
    [X] - Als speler wil ik een spel kunnen spelen.
        [X] - Bij het openen van de pagina wordt een bord laten zien (Fiches worden bepaald door array, van ResponseModule).
            [X] - Backend: Bepaal of speler al in spel zit.
                [X] - Sessions maken voor unieke combinatie computer + browser
                [X] - Session moet verbonden worden met een token, die gebruikt kan worden in de spel communicatie (push en put).
            [X] - Als het een nieuw spel is.
                [X] - Wordt een nieuwe speler voor mij gezorgd, en wordt ik automatisch aan de game toegevoegd. ('api/Spel/joinGame) // NEXT
                [X] - Wordt een nieuw bord laten zien.
            [X] - Als het een bestaand spel is.
                [X] -Wordt het bord van het lopende spel laten zien.
    [ ] - Als speler wil ik een spel af kunnen breken om een nieuw spel te beginnen 
        [ ] - Session kan verbroken worden, via een surrender.
        [ ] - Speler gaat weer automatisch in een queue.
        

[ ] Spel -
    [X] - Regels om een zet te maken.
    [ ] - Elke ronde calculeren welke moves mogelijk zijn.
    [ ] - Elke ronde calculeren of de speler die aan de beurt is verloren heeft.
        [ ] - backend (berekenen)
        [ ] - frontend
            [ ] - Visualiseren (licht groen welke velden gespeeld kunnen worden)
            [ ] - Uitrekenen of een move mag, voordat ik hem stuur.
                [ ] - Als het een iligale move is, veld (2x) rood laten blinken.
    [?] - Handlebars mogelijkheden toevoegen 