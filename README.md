# Tunnelbear Checker

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

<img width="1648" height="782" alt="image" src="https://github.com/user-attachments/assets/0c16c7bc-5fc8-456f-abbd-cc66ba1d7041" />


## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/impatient13/tunnelbear-checker.git
   cd tunnelbear-checker
