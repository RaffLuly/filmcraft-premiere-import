# v0.1.0-preview — importazione Premiere per Mac Apple Silicon

Prima distribuzione sperimentale, gratuita e non ufficiale. Basata su FilmCraft 0.20.1 e sul lavoro upstream delle PR #2312 e #4504, con adattamenti locali. Crediti completi nel repository.

## Un progetto aperto a chi vuole migliorarlo

Non sono uno sviluppatore. Sono un utilizzatore che voleva aprire i propri progetti Premiere in FilmCraft e ha deciso di condividere questa versione, basata sul lavoro degli autori originali.

Se sai come migliorare l’importazione, risolvere problemi o rendere l’app compatibile con altri sistemi, sei il benvenuto. Puoi aprire una issue o proporre una pull request. L’idea è semplice: renderla più utile per tutti, dando sempre credito a chi ha fatto il lavoro.

## Download e uso

Scarica `FilmCraft-Premiere-Import-v0.1.0-preview-macOS-arm64.zip`, estrai e copia `FilmCraft Premiere.app` in Applicazioni. Apri questa app, crea un progetto vuoto e scegli **File → Importa progetto Premiere Pro…**.

Compatibilità del binario: Mac Apple Silicon, arm64. Minimo macOS dichiarato dal bundle: 11.0; le vecchie versioni non sono state provate. Niente pacchetti Intel, Windows o Linux verificati in questa release.

**Firma ad-hoc, senza certificato Apple Developer e senza notarizzazione.** macOS può bloccare l'apertura. Non disattivare le protezioni del sistema; è disponibile il sorgente tramite patch e commit originali fissati.

Non serve Premiere per la conversione locale. Servono invece i file video/audio originali e i relativi dischi. Leggi il rapporto d'importazione: effetti, plugin e interpolazioni possono differire; le composizioni After Effects Dynamic Link non vengono renderizzate. I progetti con provenienza richiedono questa build modificata. Whisper non abilitato.

Questa preview riusa il binario già verificato durante l'integrazione; il confezionamento aggiunge licenze e crediti, rimuove simboli di debug e assegna un bundle identifier comunitario separato. Non è una nuova compilazione ottimizzata per la distribuzione.

Contenuti: app, README, crediti, licenze, BUILD-MANIFEST e riferimento ai sorgenti. Nessun progetto o media privato. Verifica il file SHA256SUMS per l'integrità del download.

---

## English

### FilmCraft Premiere Import — Community Preview

A free, experimental and unofficial FilmCraft build with direct Premiere Pro `.prproj` import. It is based on FilmCraft 0.20.1 and the existing upstream work in PRs [#2312](https://github.com/storytold/filmcraft/pull/2312) and [#4504](https://github.com/storytold/filmcraft/pull/4504), with local integration changes. Full credit belongs to the original authors and contributors.

**I’m not a developer.** I’m a user who wanted to open my Premiere projects in FilmCraft and decided to share this version, built on the original contributors’ work.

If you can improve the importer, fix bugs, or help bring it to other platforms, **you’re welcome to contribute**. Open an issue or send a pull request. The goal is simple: make it more useful for everyone, while giving credit to the people who did the work.

### Download and use

1. Under **Assets**, download `FilmCraft-Premiere-Import-v0.1.0-preview-macOS-arm64.zip`.
2. Extract it and copy **FilmCraft Premiere.app** to Applications. Open this app, rather than the standard FilmCraft app.
3. Create an empty project, then choose **File → Import Premiere Pro Project…** and select your `.prproj` file.
4. Review the import report and save a new FilmCraft project.

**Compatibility:** Apple Silicon Macs (`arm64`, M1 and later). M5 Pro compatibility is expected but has not been tested directly. The bundle declares macOS 11.0 as its minimum; older macOS releases have not been tested. This release does not include verified Intel Mac, Windows or Linux packages.

**Signing:** ad-hoc signed, without an Apple Developer certificate or Apple notarization. macOS may block the app. Do not disable system security protections; the source patch and pinned upstream source/build instructions are public.

Conversion runs locally and does not require opening Premiere. Keep the original video/audio files and their drives available. Effects, plug-ins, LUTs and interpolation may differ. After Effects Dynamic Link compositions are not rendered. Projects saved with import provenance require this modified build. Whisper transcription is not enabled.

The download contains the app, documentation, credits, licenses and build manifest. No private projects or media are included. Check **SHA256SUMS** for download integrity.

[Full English documentation](https://github.com/RaffLuly/filmcraft-premiere-import/blob/main/README.en.md) · [Issues and feedback](https://github.com/RaffLuly/filmcraft-premiere-import/issues)
