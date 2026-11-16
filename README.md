# Eugenio Ruggieri — sito personale

Home approvata “ruge.”, con due voci: **EMCRAG Project** e **80 Arcade Games**.
Sorgenti della home: Q*Bert Pyramid WEB 1.2.0, tag v1.2.0,
commit 013230b7fc3e0db95b080cf0e9bcc7380e792461.

## Stato operativo — 16 novembre 2026

- Release del gioco disponibile: https://github.com/eruggie/qbert-pyramid/releases/tag/v1.2.0
- Home approvata presente in questo repository; HTML e CSS conservati.
- GitHub Pages ha attivato automaticamente la home su https://eruggie.github.io/.
- Backend: account EU ruge creato; autenticazione per il deployment in corso.
- Il gioco online e la classifica non sono ancora dichiarati operativi.
- Il link Arcade è ancora relativo e verrà impostato all'URL HTTPS reale prima
  della verifica finale del sito. Non è dichiarato un gioco funzionante sul dominio github.io.

Backend predisposto: **PythonAnywhere EU Beginner**, gratuito con rinnovo
manuale mensile e storage persistente. Google Drive non esegue Python/SQLite.
La creazione/verifica email dell'account richiede l'intervento personale del
proprietario; nessuna fatturazione deve essere attivata.

## Attivazione del gioco

1. Creare il piano Beginner gratuito su https://eu.pythonanywhere.com/pricing/ .
2. Caricare ed estrarre l'asset Runtime 1.2.0 in ~/qbert-web.
3. Creare la web app Manual configuration con Python >=3.10.
4. Usare deployment/pythonanywhere_wsgi.py nel file WSGI del servizio;
   controllare che account.name corrisponda allo username/domain assegnato.
   Nessuna static mapping: il modulo incluso serve file e API alla stessa origine.
5. Reload, HTTPS e verifica del gioco/API; database in ~/qbert-data fuori dal sito.
6. Configurare il link Arcade con il dominio reale, pubblicare Pages dal ramo
   main, cartella root e verificare i due collegamenti e il ritorno HOME.

Istruzioni congelate e limiti:
https://github.com/eruggie/qbert-pyramid/blob/v1.2.0/docs/PYTHONANYWHERE_DEPLOY.md
https://github.com/eruggie/qbert-pyramid/blob/v1.2.0/docs/GITHUB_PUBLICATION.md

HTML/CSS senza dipendenze o tracking. Codice originale GPL-3.0-only;
EMCRAG è collegato come progetto distinto e conserva la propria licenza.
Lo stato operativo viene aggiornato qui senza modificare il tag del gioco.
