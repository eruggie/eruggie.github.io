# Pubblicazione Web 1.2.0 — 16 novembre 2026

## Destinazioni operative

- Home personale: https://eruggie.github.io/
- Gioco: https://ruge.eu.pythonanywhere.com/80_arcade_games/qbert/
- Release: https://github.com/eruggie/qbert-pyramid/releases/tag/v1.2.0
- Sorgenti congelati: commit 013230b7fc3e0db95b080cf0e9bcc7380e792461, tag v1.2.0.

Utente: ultima candidata testata e accettata, autorizzazione esplicita a
completamento e pubblicazione. Tag e asset Windows v1.1.0 preservati.
I Markdown della release sono congelati nel tag; questo rapporto descrive
separatamente le operazioni di hosting completate successivamente.

## Verifiche

Build stabile ricostruita, non ottenuta rinominando candidate: 131 test
GDScript / 126776 verifiche, 32 test Python. Runtime estratto, HTTP/MIME,
percorsi, ZIP e sorgenti corrispondenti verificati. Otto asset pubblicati,
riscaricati senza autenticazione e confrontati SHA-256; CRC ZIP conformi.

PythonAnywhere EU Beginner, account ruge, Python 3.12, HTTPS obbligatorio.
File pubblici WASM/PCK/JS/worklet/CSS/immagini e BUILD_INFO confrontati
con la release. API server attiva sulla stessa origine del gioco.
Salvataggio, retry idempotente e persistenza dopo un vero reload del worker
verificati con publication-qa.sqlite3, separato dal database definitivo.
In seguito attivato leaderboard.sqlite3, inizialmente vuoto; DB di QA rimosso.
Nessun punteggio fittizio lasciato nella classifica di produzione.
Percorsi privati e database non serviti via HTTP.

Chrome 157.0.8103.79 ed Edge 157.0.4341.60, Windows, profili temporanei:
home approvata, link Arcade fra i domini, avvio, menu, INFORMAZIONI con
versione 1.2.0, input/salti, focus e pausa/ripresa, layout 1024×768, HOME
con redirect a Pages. Segnale audio effettivo misurato dopo salti: picco
0.074737548828125 in entrambi i browser, contesto running. Nessuna eccezione
JavaScript, richiesta fallita o risposta HTTP >=400 nelle sessioni completate.
Home servita da Pages confrontata con l'HTML approvato con il solo URL Arcade
configurato. Link EMCRAG conservato al README pubblico verificato.

Dati numerici in [deployment/verification.json](deployment/verification.json).
Anteprime: [home](deployment/home-preview.png), [gioco](deployment/game-preview.png).

## Limiti documentati

Una prima sessione automatizzata Edge non ha completato l'avvio entro il
limite del test; la successiva prova completa è riuscita. Causa non determinata.
Il primo caricamento richiede circa 41 MB di risorse; il piano gratuito non
fornisce garanzie di prestazioni o uptime. Browser test automatizzati distinti
dai test manuali dell'utente; nessun nuovo test nativo Windows dichiarato.
Nessuna nuova verifica fullscreen automatizzata, oltre alle limitazioni browser
già documentate nella release. Nessun anti-cheat o garanzia di scalabilità.

## Gestione gratuita

**Scadenza dell'app: 16 dicembre 2026.** Nel pannello Web di PythonAnywhere EU
usare **Run until 1 month from today** prima della scadenza e ripetere il rinnovo
periodicamente. È un rinnovo manuale, non un acquisto. Non sono stati attivati
piani a pagamento, fatturazione o domini personalizzati.

Database privato: /home/ruge/qbert-data/leaderboard.sqlite3. Conservarlo durante
aggiornamenti, fare backup SQLite e non caricarlo su GitHub. Credenziali non
inserite nei repository. Google Drive non è stato usato come server.
