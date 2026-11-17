# Eugenio Ruggieri — sito personale

Home approvata “ruge.”, con due sole voci: **EMCRAG Project** e **80 Arcade Games**.

- **Home:** https://eruggie.github.io/
- **EMCRAG:** https://github.com/eruggie/EMCRAG/blob/main/README.md
- **Gioco:** https://ruge.eu.pythonanywhere.com/80_arcade_games/qbert/
- **Download:** https://github.com/eruggie/qbert-pyramid/releases/tag/v1.2.1

## Versione e provenienza

Q*Bert Pyramid WEB 1.2.1, tag v1.2.1, commit
fb3fbbaba2152782bffb933f0ad9664eda7eb90d. La home è quella approvata
nel pacchetto della release; cambia soltanto la destinazione del link Arcade,
ora rivolta all'host HTTPS effettivo. Hash in SOURCE_PROVENANCE.json.

Il software e i documenti Markdown del tag v1.2.1 sono congelati; questo
repository registra separatamente configurazione e stato operativo del sito.
La release Windows v1.1.0 mantiene tag e asset originali.

## Stato operativo — 17 novembre 2026

GitHub Pages ospita HTML/CSS della home con HTTPS. PythonAnywhere EU Beginner,
account ruge, serve gioco e API alla stessa origine con Python 3.12/WSGI.
File del gioco confrontati SHA-256 con la nuova release. L'aggiornamento usa
lo stesso database di produzione e mantiene i file/configurazione precedenti
per il rollback; nessuna inizializzazione o cancellazione dei punteggi.
La 1.2.1 corregge la doppia decompressione gzip e riduce l'attesa SQLite.
Partite concorrenti e salvataggi sono verificati su database locali isolati;
la verifica pubblica controlla lettura della classifica, avvio, audio e licenze.
Il rapporto completo della patch è in [PUBLICATION_1.2.1.md](PUBLICATION_1.2.1.md).
Il [rapporto della prima pubblicazione](PUBLICATION_REPORT.md) resta storico.

### Rinnovo gratuito e dati

**Scadenza attuale dell'app gratuita: 16 dicembre 2026.** Accedere periodicamente
alla scheda Web di PythonAnywhere e usare **Run until 1 month from today**
prima della scadenza. Il piano non si rinnova automaticamente con il nostro
codice; se scade, gioco e classifica possono diventare indisponibili.
Nessun piano a pagamento, carta di credito o servizio a consumo attivato.

- Configurazione: deployment/pythonanywhere_wsgi.py.
- File su PythonAnywhere: /home/ruge/qbert-web-1.2.1/site e /home/ruge/qbert-web-1.2.1/server.
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
[PythonAnywhere](https://github.com/eruggie/qbert-pyramid/blob/v1.2.1/docs/PYTHONANYWHERE_DEPLOY.md) ·
[GitHub Pages](https://github.com/eruggie/qbert-pyramid/blob/v1.2.1/docs/GITHUB_PUBLICATION.md).

HTML/CSS senza dipendenze esterne o tracking. Originali GPL-3.0-only;
EMCRAG resta un progetto distinto con la propria licenza. Crediti e licenze
Godot/gioco restano nei pacchetti e sul relativo host.
