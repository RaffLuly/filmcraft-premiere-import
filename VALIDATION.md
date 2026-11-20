# Validation and limits

## Integration checks performed on 12 November 2026

- Premiere interchange tests: 66 passed, 3 ignored (optional corpus/stress cases).
- Premiere engine tests: 29 passed, 1 ignored (optional corpus), before the final snapshot-location regression was added.
- Format library: 30 passed.
- Dedicated import menu regression: 1 passed.
- MPEG-named MP3 decode regression: 1 passed.
- Desktop snapshot location regression: 1 passed.
- Desktop app and CLI build completed successfully.
- Native menu observed and import performed in the desktop app; camera images and timeline cuts displayed.
- A read-only private test project imported 12 sequences. Its SHA-256 remained unchanged. Two After Effects compositions remained offline as documented. No private project, hash, media, path or screenshots are included here.

These are recorded results from the integration session, not claims of fresh runs during publication. They do not establish compatibility with every Premiere project or every Mac.

## Publication checks

- The published patch applies cleanly to the pinned upstream source.
- The app executable is arm64 and links to system frameworks/libraries, not private media files.
- Publication packaging removes debug symbols, preserves license notices, adds font/icon license texts and uses a separate community bundle identifier.
- Ad-hoc code signature verified with `codesign --verify --strict --deep`.
- ZIP contents and repository files checked for private project/media inclusions and known private source paths.

No Windows, Linux, Intel Mac, old-macOS compatibility, Apple notarization or full visual parity certification is claimed. Speech transcription is disabled in this build. Test on copies of your projects and review the import report.
