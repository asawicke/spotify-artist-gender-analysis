# spotify-artist-gender-analysis

# Spotify Playlist Artist Gender Guess

Analyze artists from popular Spotify playlists and estimate gender from first names using the Genderize API. This is a quick demo of the Spotify Web API with Spotipy plus a simple external enrichment step.

## What it does
- Fetches up to 50 tracks from several Spotify editorial playlists
- Extracts artist names and takes the first token of each name
- Queries Genderize to guess gender for each unique first name
- Aggregates counts and writes a summary to `output.txt`

## Example output
Male: 42 (60.0%)
Female: 25 (35.7%)
Unknown: 3 (4.3%)

## Setup

### 1) Requirements
- Python 3.10+
- A Spotify Developer account and app
- Packages: `spotipy`, `requests`, `python-dotenv` (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate
pip install spotipy requests python-dotenv
