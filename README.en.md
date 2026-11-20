# FilmCraft Premiere Import — Community Preview

[Italiano](README.md) · **English**

A free and **unofficial** FilmCraft build with **File → Import Premiere Pro Project…**.

Open `.prproj` files directly, without opening Premiere or exporting an XML first. Projects and media are read locally. Your videos are not uploaded to GitHub or a conversion service.

**[Download for Apple Silicon Mac](https://github.com/RaffLuly/filmcraft-premiere-import/releases/tag/v0.1.0-preview)** · [Original FilmCraft project](https://github.com/storytold/filmcraft) · [Credits](CREDITS.md)

## Help make it better

**I’m not a developer.** I’m a user who wanted to open my Premiere projects in FilmCraft and decided to share this version, built on the original contributors’ work.

If you can improve the importer, fix bugs, or help bring it to other platforms, **you’re welcome to contribute**. Open an [issue](https://github.com/RaffLuly/filmcraft-premiere-import/issues) or send a pull request. The goal is simple: make it more useful for everyone, while giving credit to the people who did the work.

The importer was not written from scratch for this distribution. Please keep the upstream authors’ credits and licenses in any contributions.

## Compatibility

The ready-to-download app is for **Apple Silicon Macs**, `arm64`, M1 and later. M5 Pro compatibility is expected but has not been tested directly. The bundle declares macOS 11.0 as its minimum; older macOS versions and other Mac models have not been verified. This is not a universal Intel/Apple Silicon app. No verified Windows or Linux packages are included in this distribution yet.

This preview is ad-hoc signed, without an Apple Developer certificate or Apple notarization. macOS may block it from opening. Do not disable your system’s security protections. The public source patch and build instructions are available below.

## How to use it

1. Download the ZIP under **Assets** on the release page, extract it and copy **FilmCraft Premiere.app** to Applications.
2. Open **FilmCraft Premiere**. It is separate from the original app named simply FilmCraft.
3. Create an empty project, then choose **File → Import Premiere Pro Project…** and select a `.prproj` file.
4. Read the import report and save a new `.fcproj` project.

Keep your original projects and all video/audio files. A Premiere project contains references to media, not the videos themselves: the drives must remain accessible. Importing into a project that already contains material adds the imported sequences to the open project.

The regular Import command also accepts `.prproj`. The dedicated command limits the file picker to Premiere projects.

## What to expect

The importer handles sequences, tracks, cuts, audio/video links, bins, markers and several Motion, audio and color properties. It does **not** guarantee identical rendering to Premiere. The report lists approximations, offline items and unsupported features.

- After Effects Dynamic Link compositions (`.aep`) need rendered video files or reconstruction.
- Plug-ins, some effects, LUTs and interpolation may not render the same way.
- A local fix also recognizes MP3 audio saved with a `.mpeg` extension, after checking the file contents.
- Source snapshots and import provenance are stored in **Premiere Imports**, beside the app preferences. Media remain linked to the original files.
- Projects containing this provenance use the `filmcraft.project.workflow` format. Keep this modified build with your saved projects: the original build may refuse that format.
- Automatic Whisper transcription and neural voices are not enabled in this package.

## Where the code comes from

This repository publishes the **complete patch**, scripts to retrieve the exact public upstream source, and build information. It is not an independent rewrite of FilmCraft and does not claim to have invented the importer.

- FilmCraft base: [`a6c0f45966b422142a84bf855332c4a1833450cf`](https://github.com/storytold/filmcraft/tree/a6c0f45966b422142a84bf855332c4a1833450cf).
- Importer: work from upstream PRs [#2312](https://github.com/storytold/filmcraft/pull/2312) and [#4504](https://github.com/storytold/filmcraft/pull/4504), reference commit `fce333299043f1452a5618f0926d8cb7342dd0c7`. Later changes in those PRs are not automatically part of this preview.
- Local changes: dedicated import menu, Italian strings, import-report dialog, compatibility with the base code, snapshots outside the source archive, and MPEG-named MP3 recognition.
- ArtCraft graphic trademarks have been removed from the modified build. The FilmCraft owl icon is retained under its MIT/Apache-2.0 license.
- Automatic update checks at startup are disabled in this build so that an official update does not replace the experimental importer.

See [BUILD-MANIFEST.json](BUILD-MANIFEST.json), the [patch](patches/premiere-import.patch) and [validation record](VALIDATION.md).

## Build from source

You need Git, Python 3, Rust/Cargo and the system dependencies documented by the original project. The tested build used Rust 1.99.1 on an Apple Silicon Mac. No GitHub token is required to download the public sources.

```sh
git clone https://github.com/RaffLuly/filmcraft-premiere-import.git
cd filmcraft-premiere-import
python3 scripts/build.py --destination build/filmcraft-source
```

The script retrieves the pinned base commit, applies the patch and builds the desktop app and CLI. Use `--source-only` to prepare sources without compiling, or `--release` for a new optimized build. These instructions do not promise a bit-for-bit reproduction of the download. The initial package uses the previously tested build with debug symbols stripped and licenses added; it was not recompiled for publication.

## Licenses and independence

Code is licensed under **MIT OR Apache-2.0**, according to the original licenses: [MIT](LICENSE-MIT), [Apache-2.0](LICENSE-APACHE), [NOTICE](NOTICE) and [attributions](ATTRIBUTION.md). Fonts and other materials retain their own licenses in `licenses`.

Community distribution maintained by **RaffLuly**, based on FilmCraft by the ArtCraft Team and contributors. This is not an official release or a product endorsed or supported by ArtCraft or Adobe. Product names describe compatibility.

No private test projects, videos, audio, screenshots or personal data are included. Do not attach confidential projects to public issues. Describe the problem or provide a synthetic example instead.
