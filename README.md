# FilmCraft Premiere Import — Community Preview

**Italiano** · [English](README.en.md)

Versione gratuita e **non ufficiale** di FilmCraft con il comando **File → Importa progetto Premiere Pro…**.

Importa direttamente i file `.prproj`, senza aprire Premiere e senza esportare prima un XML. La lettura dei progetti e dei media avviene localmente. I video non vengono caricati su GitHub o su un servizio di conversione.

**[Scarica la versione per Mac Apple Silicon](https://github.com/RaffLuly/filmcraft-premiere-import/releases/tag/v0.1.0-preview)** · [Progetto originale](https://github.com/storytold/filmcraft) · [Crediti](CREDITS.md)

## Un progetto aperto a chi vuole migliorarlo

Non sono uno sviluppatore. Sono un utilizzatore che voleva aprire i propri progetti Premiere in FilmCraft e ha deciso di condividere questa versione, basata sul lavoro degli autori originali.

Se sai come migliorare l’importazione, risolvere problemi o rendere l’app compatibile con altri sistemi, sei il benvenuto. Puoi aprire una issue o proporre una pull request. L’idea è semplice: renderla più utile per tutti, dando sempre credito a chi ha fatto il lavoro.

## A chi serve

Il download pronto è per Mac con chip Apple Silicon (M1 e successivi), architettura `arm64`. Il bundle dichiara macOS 11 come minimo; le vecchie versioni di macOS e gli altri modelli di Mac non sono stati verificati. Non è un'app universale Intel/Apple Silicon. Windows e Linux non hanno ancora un pacchetto verificato in questa distribuzione.

Questa preview non è firmata con un certificato Apple Developer e non è notarizzata: macOS può impedirne l'apertura. Non disattivare le protezioni del sistema. Per chi preferisce compilare, il codice di base e la patch sono disponibili qui sotto.

## Uso

1. Scarica lo ZIP dalla pagina della release, estrailo e copia **FilmCraft Premiere.app** in Applicazioni.
2. Apri **FilmCraft Premiere**: è separata dall'app originale chiamata semplicemente FilmCraft.
3. Crea un progetto vuoto, poi scegli **File → Importa progetto Premiere Pro…** e seleziona il `.prproj`.
4. Leggi il rapporto d'importazione e salva come nuovo progetto `.fcproj`.

Conserva i progetti originali e tutti i file video/audio. Il progetto Premiere contiene riferimenti ai media, non i video stessi: i dischi devono essere disponibili. Importare in un progetto già popolato aggiunge le sequenze al progetto aperto.

Il comando Importa normale accetta anch'esso `.prproj`. Il comando dedicato mostra soltanto questi file nella finestra di selezione.

## Cosa aspettarsi

L'importatore gestisce sequenze, tracce, tagli, collegamenti audio/video, raccoglitori, marcatori e varie proprietà Motion/audio/colore. Il risultato non garantisce la stessa resa di Premiere: il rapporto segnala approssimazioni, elementi offline e funzioni non riprodotte.

- Le composizioni After Effects Dynamic Link (`.aep`) richiedono video renderizzati o ricostruzione.
- Plugin, alcuni effetti, LUT e interpolazioni possono non essere riprodotti allo stesso modo.
- La correzione locale riconosce anche musica MP3 salvata con estensione `.mpeg`, dopo verifica del contenuto.
- Le copie di riferimento e la provenienza dell'importazione sono conservate nella cartella **Premiere Imports** accanto alle preferenze dell'app; i media restano collegati ai file originali.
- I progetti che contengono questa provenienza usano il formato `filmcraft.project.workflow`. Mantieni questa versione insieme ai progetti salvati: la build originale può rifiutare il formato.
- La trascrizione automatica Whisper e le voci neurali non sono abilitate in questo pacchetto.

## Provenienza del codice

Questo repository contiene la **patch completa**, gli script per recuperare il sorgente pubblico esatto e le informazioni di compilazione. Non è una riscrittura autonoma di FilmCraft e non rivendica l'invenzione dell'importatore.

- FilmCraft base: [`a6c0f45966b422142a84bf855332c4a1833450cf`](https://github.com/storytold/filmcraft/tree/a6c0f45966b422142a84bf855332c4a1833450cf).
- Importatore derivato dalle proposte [#2312](https://github.com/storytold/filmcraft/pull/2312) e [#4504](https://github.com/storytold/filmcraft/pull/4504), riferimento `fce333299043f1452a5618f0926d8cb7342dd0c7`.
- Adattamenti: comando nel menu, traduzione italiana, rapporto nell'interfaccia, compatibilità con il codice base, copie di riferimento fuori dall'archivio sorgente e riconoscimento MP3 con estensione `.mpeg`.
- Marchi grafici ArtCraft rimossi dalla build modificata. Icona FilmCraft mantenuta secondo la sua licenza MIT/Apache-2.0.
- Aggiornamenti automatici all'avvio disattivati in questa build, per evitare che un aggiornamento ufficiale sostituisca l'importatore sperimentale.

Vedi [BUILD-MANIFEST.json](BUILD-MANIFEST.json), [patch](patches/premiere-import.patch) e [verifiche](VALIDATION.md).

## Compilare dal sorgente

Servono Git, Python 3, Rust/Cargo e le dipendenze di sistema documentate dal progetto originale. La build verificata usava Rust 1.99.1 su Mac Apple Silicon. Nessun token GitHub è richiesto per scaricare i sorgenti pubblici.

```sh
git clone https://github.com/RaffLuly/filmcraft-premiere-import.git
cd filmcraft-premiere-import
python3 scripts/build.py --destination build/filmcraft-source
```

Lo script recupera il commit base, applica la patch e compila app desktop e CLI. Per preparare soltanto i sorgenti usa `--source-only`; per una nuova compilazione ottimizzata usa `--release`. Queste opzioni non producono una compilazione bit-per-bit identica al pacchetto pubblicato. Il pacchetto iniziale è la build già provata, ripulita dei simboli di debug e con licenze aggiunte; non è stato ricompilato per questa pubblicazione.

## Licenze e indipendenza

Codice MIT OR Apache-2.0, secondo le licenze originali: [MIT](LICENSE-MIT), [Apache-2.0](LICENSE-APACHE), [NOTICE](NOTICE), [attribuzioni](ATTRIBUTION.md). Font e altri materiali conservano le proprie licenze nella cartella `licenses`.

Distribuzione comunitaria curata da **RaffLuly**, basata su FilmCraft del team ArtCraft e dei suoi contributori. Non è una release ufficiale né un prodotto approvato o supportato da ArtCraft o Adobe. I nomi dei prodotti sono usati per descrivere la compatibilità.

Non sono inclusi progetti, video, audio, schermate o dati privati usati durante le prove. Non allegare progetti riservati alle segnalazioni pubbliche; descrivi il problema o usa un esempio sintetico.

---

**English:** Unofficial FilmCraft community preview with direct Premiere `.prproj` import. Apple Silicon Mac binary only. Local conversion; no Adobe subscription required for the importer. This repository publishes the complete patch and pinned upstream source retrieval/build instructions. Unsupported effects and After Effects Dynamic Link are not reproduced faithfully. Experimental, ad-hoc signed, not Apple-notarized. See the release notes and upstream credits before use.
