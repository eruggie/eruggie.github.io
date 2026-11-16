# Eugenio Ruggieri — sito personale

Home approvata “ruge.”, con due sole voci: **EMCRAG Project** e **80 Arcade Games**.

- **Home:** https://eruggie.github.io/
- **EMCRAG:** https://github.com/eruggie/EMCRAG/blob/main/README.md
- **Gioco:** https://ruge.eu.pythonanywhere.com/80_arcade_games/qbert/
- **Download:** https://github.com/eruggie/qbert-pyramid/releases/tag/v1.2.0

## Versione e provenienza

Q*Bert Pyramid WEB 1.2.0, tag v1.2.0, commit
013230b7fc3e0db95b080cf0e9bcc7380e792461. La home è quella approvata
nel pacchetto della release; cambia soltanto la destinazione del link Arcade,
ora rivolta all'host HTTPS effettivo. Hash in SOURCE_PROVENANCE.json.

Il software e i documenti Markdown del tag v1.2.0 sono congelati; questo
repository registra separatamente configurazione e stato operativo del sito.
La release Windows v1.1.0 mantiene tag e asset originali.

## Stato operativo — 16 novembre 2026

GitHub Pages ospita HTML/CSS della home con HTTPS. PythonAnywhere EU Beginner,
account ruge, serve gioco e API alla stessa origine con Python 3.12/WSGI.
File del gioco confrontati SHA-256 con la release; API e persistenza dopo
riavvio verificati usando un database di QA separato. Il database di produzione
è stato inizializzato vuoto, senza record fittizi. Il flusso browser pubblico è stato verificato su Chrome ed Edge, inclusi
audio misurato, focus e ritorno HOME: [rapporto completo](PUBLICATION_REPORT.md).

### Rinnovo gratuito e dati

**Scadenza attuale dell'app gratuita: 16 dicembre 2026.** Accedere periodicamente
alla scheda Web di PythonAnywhere e usare **Run until 1 month from today**
prima della scadenza. Il piano non si rinnova automaticamente con il nostro
codice; se scade, gioco e classifica possono diventare indisponibili.
Nessun piano a pagamento, carta di credito o servizio a consumo attivato.

- Configurazione: deployment/pythonanywhere_wsgi.py.
- File su PythonAnywhere: /home/ruge/qbert-web/site e /home/ruge/qbert-web/server.
- Database privato di produzione: /home/ruge/qbert-data/leaderboard.sqlite3.
- Non mettere database o credenziali nel repository o nella directory pubblica.
- Conservare lo stesso DB durante gli aggiornamenti e fare backup SQLite.
- Nessuna static mapping sull'intera cartella del gioco: il modulo hosted_wsgi
  serve file ammessi e API, con streaming e MIME WASM/PCK.
- HOME e la voce del menu passano dalla radice dell'host del gioco a questa home.

Il piano gratuito offre un worker e 512 MiB; SQLite è per questo piccolo
progetto, non è una garanzia di scalabilità o uptime. Google Drive può conservare
backup e ZIP ma non esegue il backend. Nessuna CORS/API key è inserita nel client.

Istruzioni congelate:
[PythonAnywhere](https://github.com/eruggie/qbert-pyramid/blob/v1.2.0/docs/PYTHONANYWHERE_DEPLOY.md) ·
[GitHub Pages](https://github.com/eruggie/qbert-pyramid/blob/v1.2.0/docs/GITHUB_PUBLICATION.md).

HTML/CSS senza dipendenze esterne o tracking. Originali GPL-3.0-only;
EMCRAG resta un progetto distinto con la propria licenza. Crediti e licenze
Godot/gioco restano nei pacchetti e sul relativo host.
