# AMP Plex Template

This repository contains an AMP (Application Management Panel) template for deploying Plex Media Server. It defines the configuration files needed by AMP to install and manage a Plex server instance.

## Setup
1. Place the contents of this repository inside your AMP `Templates` directory.
2. Create a new AMP instance and select **Plex Media Server** when prompted for a template.
3. AMP will download and install the latest Plex release using the settings in `plex-media-serverupdates.json`.

## Configuration Files
- `manifest.json` – Basic metadata that identifies the template.
- `plex-media-server.kvp` – Key/value settings for how AMP launches and controls the server.
- `plex-media-serverconfig.json` – Placeholder for configuration options (currently empty).
- `plex-media-servermetaconfig.json` – Placeholder for meta configuration (currently empty).
- `plex-media-serverports.json` – List of network ports used by Plex.
- `plex-media-serverupdates.json` – Update stages executed by AMP to download and install Plex.


