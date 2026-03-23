# get

A dead-simple terminal tool to download YouTube videos and audio.

## Install

```bash
brew tap rayinuk13/get https://github.com/rayinuk13/get
brew install get
```

## Uninstall

```bash
brew uninstall get
brew untap rayinuk13/get
```

## Usage

```bash
get -mp3 <url>   # Download audio as MP3
get -mp4 <url>   # Download video as MP4
```

## Examples

```bash
get -mp3 https://www.youtube.com/watch?v=dQw4w9WgXcQ
get -mp4 https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

Files are saved to `~/Downloads/`.

## Requirements

- `yt-dlp` and `ffmpeg` — installed automatically via Homebrew

## License

MIT
