# system_music_GTASA
Dear friends, this Python system will get you started on developing a system for downloading and playing music with your own link within your SAMP server.

Flask: Framework for creating web applications.
google-api-python-client: Library to access the Google API.
yt-dlp: Tool to download and convert YouTube videos.
ffmpeg: Command-line tool for audio and video manipulation (required for conversion to MP3).
You can install all these packages using pip. Here's a command that installs them all:

pip install Flask google-api-python-client yt-dlp

Additionally, yt-dlp relies on ffmpeg to convert audio files. ffmpeg is not a Python package, so you need to hook it up separately. Installation depends on your operating system:

For Windows:
Download ffmpeg from the official website: FFmpeg Downloads.
Extract the ZIP file and add the ffmpeg bin folder path to the PATH environment variable.
For macOS:
You can install ffmpeg using Homebrew:

brew install ffmpeg

For Linux:
On Debian/Ubuntu based distributions use:

sudo apt-get install ffmpeg

On Fedora-based distributions, use:

sudo dnf install ffmpeg



And don't forget to download composer!

http://127.0.0.1:5001/convert?query=Nome+da+Música

Bye bye
