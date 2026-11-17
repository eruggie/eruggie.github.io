# Pubblicazione WEB 1.2.1 — 17 novembre 2026

Autorizzata dal titolare: correzioni gzip e attesa SQLite, testi/pulsanti e
licenze, commit e pubblicazione. Home personale e relativi due link invariati.

- Sorgenti: `eruggie/qbert-pyramid`, tag `v1.2.1`, commit `fb3fbbaba2152782bffb933f0ad9664eda7eb90d`.
- Gioco/API: https://ruge.eu.pythonanywhere.com/80_arcade_games/qbert/ .
- Home: https://eruggie.github.io/ .
- Release: https://github.com/eruggie/qbert-pyramid/releases/tag/v1.2.1 .
- Runtime, Complete, Source, WebStatic, BUILD_INFO, QA_REPORT, QA_EVIDENCE e checksum.

## Aggiornamento del servizio

Caricati e verificati SHA-256 i file della release. Directory attiva:
`/home/ruge/qbert-web-1.2.1`; database preesistente invariato in
`/home/ruge/qbert-data/leaderboard.sqlite3`. Otto risultati e record 33580
riletti prima/dopo l'aggiornamento. Nessuna migrazione o cancellazione.
Directory precedente `/home/ruge/qbert-web` e configurazione WSGI precedente
conservate; copia privata della configurazione in
`/home/ruge/qbert-web-1.2.1/deployment/previous-wsgi.py`.
Nessun costo, upgrade o cambio della scadenza gratuita del 16 dicembre 2026.

## Verifiche e limiti

131 test GDScript / 126778 verifiche e 41 test Python. Test concorrenti con
32 client e quattro processi su database locali isolati; due partite Chrome/Edge
Windows automatizzate contemporanee, salvataggi gzip, preferenze separate e reload.
Nessun risultato perso o duplicato nei casi verificati. Questi test non
certificano la capacità massima del piano gratuito.

Sul servizio pubblico, Chrome/Edge verificano avvio, classifica reale, audio
misurato, focus, INFORMAZIONI, layout desktop e ritorno HOME. Nessuna eccezione
JavaScript o risorsa fallita nelle tracce. Note e Licenze carica entrambi i
documenti; il controllo visivo ha corretto il contrasto dei riquadri e la
verifica finale conferma testo leggibile. La sola correzione finale modifica
CSS e metadati: HTML, JS, WASM e PCK coincidono con quelli delle prove complete.

GET pubblico gzip HTTP 200; POST non valido HTTP 400. Non sono stati aggiunti
punteggi fittizi sul database pubblico. Le scritture valide e il retry sono
verificati su database privati locali. Nessuna nuova prova nativa Windows.
In headless lo schermo intero del documento è negato; F11 resta soggetto al
browser. Report esatto: [deployment/verification.json](deployment/verification.json).

Conservati tag e asset Windows v1.1.0 e Web v1.2.0. La documentazione del nuovo
tag è congelata; questo repository mantiene separato lo stato operativo.
Per vedere il nuovo gioco nel browser abituale, ricaricare con **Ctrl+F5**.

## Controllo finale dei download e Pages

Tutti gli otto allegati riscaricati da URL pubblici senza autenticazione:
SHA-256 conformi ai file locali e CRC ZIP validi. GitHub indica v1.2.1 come
ultima release stabile. I metadati degli asset delle release precedenti e
i tag v1.1.0/v1.2.0 sono invariati. Pages ha completato la build; home, CSS e
pagina legale serviti via HTTPS coincidono con il repository. Evidenza:
[download-verification-1.2.1.json](deployment/download-verification-1.2.1.json).
