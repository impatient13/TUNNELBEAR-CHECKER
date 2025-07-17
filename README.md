# Tunnelbear Checker

![Tunnelbear Checker](https://img.shields.io/badge/Tunnelbear-Checker-green)

## Description

Tunnelbear Checker is a Python script that verifies TunnelBear account credentials using their official API.  
It reads a combos file (email:password format), tests each account, and saves valid accounts in a `valids.txt` file.

The script features a simple, colorized console interface that displays results in real-time.

## Features

- Checks TunnelBear accounts through the API.
- Handles errors and rate limiting (e.g., too many requests).
- Automatically saves valid accounts.
- Color-coded console output.
- Compatible with Windows and Linux terminals.

SCREEN:

https://media.discordapp.net/attachments/1394983518672781363/1395478389204320469/image.png?ex=687a9806&is=68794686&hm=12df862681c770a008a0d3f5caa4374bb7340f30fde89dcd4a1c0e894ff0cc2a&=&format=webp&quality=lossless&width=1145&height=585

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/tunnelbear-checker.git
   cd tunnelbear-checker
