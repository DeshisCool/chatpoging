# De Limburgse norm

Nederlandstalige, responsieve kennisbank op basis van de aangeleverde inhoud. Gebouwd met Vite en vanilla JavaScript.

## Ontwikkelen

Gebruik Node.js 22.12+ of 24.

```sh
npm ci
npm run dev
```

## Controle en productie

```sh
npm test
npm run build
npm run preview
```

`dist/` bevat de statische productieversie. De navigatie gebruikt hash-routes, zodat geen server-side routeherschrijving nodig is.

## Inhoud

Home, Handreiking, Checklist, Productenoverzicht en Contact, met zes thema’s en lokale zoekfunctie. `/public/werkchecklist.csv` is een eigen werkdocument, geen officiële normchecklist. Productnamen, contactgegevens en de namen van de drie tussenliggende piramideniveaus zijn niet aangeleverd; deze worden niet als feiten gepresenteerd. Stem de inhoud vóór publicatie af met de inhoudelijk verantwoordelijke. De Limburgillustratie is schematisch.

Geen backend of persoonsgegevensverwerking. Google Fonts is optioneel; zonder externe verbinding worden de lokale systeemlettertypen gebruikt.
