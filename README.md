# spotify-artist-gender-analysis

# Spotify Playlist Artist Gender Guess

Analyze artists from popular Spotify playlists and estimate gender from first names using the Genderize API. This is a quick demo of the Spotify Web API with Spotipy plus a simple external enrichment step.

## What it does
- Fetches up to 50 tracks from several Spotify editorial playlists
- Extracts artist names and takes the first token of each name
- Queries Genderize to guess gender for each unique first name
- Aggregates counts and writes a summary to `output.txt`

## Example output
