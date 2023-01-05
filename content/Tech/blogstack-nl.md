Title: Blogstack
Tags: web, software
Lang: nl
Date: 2022-06-07
Status: published

Je kan natuurlijk geen website bouwen zonder iets te zeggen over hoe het in
elkaar steekt.

woord.baudvine.net maakt onderdeel uit van een bredere poging mijn online
infrastructuur eenvoudiger te maken:

- baudvine.net uit Google Workspaces ontwarren.
- Verhuis alles naar één domein.
- dvanb.nl is een pracht van een domein, maar meer gehecht aan mijn voornaam dan
  ik, dus die mag weg.
- Stop met een VPS die ik alleen gebruikte om wat statische pagina's te hosten.

*Woord* is gehost bij
[nearlyfreespeech.net](https://www.nearlyfreespeech.net/), een van de meest
blijf-bij-je-leest diensten die ik ooit heb gebruikt. In plaats van
abonnementskosten betaal je bij NFSN voor de middelen die je gebruikt, wat mij
uitstekend schikt met m'n statische site en vijf lezers.

TLS certificaten worden verzorgd door [Let's Encrypt](https://letsencrypt.org/).
Ik heb ooit iets geschreven over [Let's Encrypt inregelen voor
Lighttpd]({filename}lighty-certbot.md) toen ik nog een eigen webserver draaide,
maar het is veel makkelijker met NFSN: log in via SSH, draai een script dat er
al is, accepteer de voorwaarden, en nu heeft woord.baudvine.net HTTPS.

De site wordt in elkaar geplakt door [Pelican](http://docs.getpelican.com/), een
*static site generator* die Markdown- en ReStructuredText-documenten als input
gebruikt. Ik hoef me niet druk te maken over de beveiliging van een dynamische
site, en ik kan m'n posts tikken in een markuptaal die ik al ken.

Het theme is een [aangepaste versie van
Sober](https://github.com/barometz/pelican-sober). Ik heb wat bugs opgelost en
het een en ander toegevoegd, zoals Open Graph tags en links naar vertaalde
artikels. Ik heb weinig verstand van zaken als typografie, dus daar blijf ik
lekker vanaf.

Het genereren en deployen gaat via een [GitHub
workflow](https://github.com/barometz/woord.baudvine.net/blob/main/.github/workflows/publish.yml),
hoewel ik alles evengoed in een lokale checkout kan doen. Ik probeer CI scripts
over het algemeen klein te houden - hoe meer ik kan debuggen zonder naar GitHub
te pushen, des te beter.
