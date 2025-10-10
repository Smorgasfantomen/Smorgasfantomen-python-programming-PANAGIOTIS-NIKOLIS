Program för linjär klassificering

Detta program läser koordinater från en CSV eller TXT-fil och klassar dem baserat på en linjärekvation.

Vid programstart väljer du om du vill läsa data från unlabelled_data.csv eller datapoints.txt.

Väljer du CSV:n får du därefter välja om du vill sortera punkterna baserat på:
1: En linjärekvation som passerar genom medelkoordinaten, vänd 90° mot medellinjen
eller
2: En av tre fördefinierade linjärekvationer.

Efter detta lagras koordinaterna i labelled_data.csv med kolumnerna X-värde, Y-värde, och sortering.

Slutligen visas en graf med fyra linjärekvationer (den medeldatabaserade och de tre fördefinierade) och alla datapunkter, färgmässigt sorterade utifrån den sorteringsformel som valdes.

Väljer du TXT:n använder programmet den datan och utför alternativ 1 i förra stycket, med skillnaden att den inte visar de fördefinierade linjerna (dessa blir irrelevanta då koordinaterna i datapoints.txt ligger en ganska bra bit från origo).