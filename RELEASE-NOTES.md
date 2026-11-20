# v0.1.0-preview — importazione Premiere per Mac Apple Silicon

Prima distribuzione sperimentale, gratuita e non ufficiale. Basata su FilmCraft 0.20.1 e sul lavoro upstream delle PR #2312 e #4504, con adattamenti locali. Crediti completi nel repository.

## Download e uso

Scarica `FilmCraft-Premiere-Import-v0.1.0-preview-macOS-arm64.zip`, estrai e copia `FilmCraft Premiere.app` in Applicazioni. Apri questa app, crea un progetto vuoto e scegli **File → Importa progetto Premiere Pro…**.

Compatibilità del binario: Mac Apple Silicon, arm64. Minimo macOS dichiarato dal bundle: 11.0; le vecchie versioni non sono state provate. Niente pacchetti Intel, Windows o Linux verificati in questa release.

**Firma ad-hoc, senza certificato Apple Developer e senza notarizzazione.** macOS può bloccare l'apertura. Non disattivare le protezioni del sistema; è disponibile il sorgente tramite patch e commit originali fissati.

Non serve Premiere per la conversione locale. Servono invece i file video/audio originali e i relativi dischi. Leggi il rapporto d'importazione: effetti, plugin e interpolazioni possono differire; le composizioni After Effects Dynamic Link non vengono renderizzate. I progetti con provenienza richiedono questa build modificata. Whisper non abilitato.

Questa preview riusa il binario già verificato durante l'integrazione; il confezionamento aggiunge licenze e crediti, rimuove simboli di debug e assegna un bundle identifier comunitario separato. Non è una nuova compilazione ottimizzata per la distribuzione.

Contenuti: app, README, crediti, licenze, BUILD-MANIFEST e riferimento ai sorgenti. Nessun progetto o media privato. Verifica il file SHA256SUMS per l'integrità del download.

English: experimental unofficial arm64 Mac build with direct `.prproj` import. Upstream authors credited. Ad-hoc signed, not notarized; effects and Dynamic Link limitations apply. No private media included. Source retrieval and build instructions are published in the repository.
