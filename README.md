# Limburgse Norm — Samen weerbaar

Broncode van gepubliceerde versie 5.
Broncommit: d001e9b64671dfdbbf3550c62b55eaa481f7bca4

## Inhoud

- dist/: de volledige statische website: HTML, CSS, JavaScript, inhoud, afbeeldingen en lettertypen.
- .openai/hosting.json: oorspronkelijke Sites-hostingconfiguratie.
- collect.py en source-report.json: oorspronkelijke importhulp en inhoudsoverzicht. Niet nodig om de website te draaien. De importhulp bevat een oorspronkelijk lokaal pad; pas dat aan vóór gebruik.

## Lokaal bekijken

Voer vanuit de uitgepakte map uit:

    python3 -m http.server 8000 --directory dist

Open http://localhost:8000 in je browser.
Er zijn geen installatie- of bouwstappen nodig. Gebruik een lokale webserver: JavaScript laadt de inhoud uit content.json.

## Aanpassen en hosten

Bewerk dist/styles.css voor de vormgeving, dist/app.js voor de opbouw en interacties en dist/content.json voor de pagina-inhoud. Afbeeldingen en lettertypen staan in dist/assets/.
Voor statische hosting is dist/ de hoofdmap van de website.
