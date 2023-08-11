
# Disable Movement Control

This repository contains Python scripts for remote control purposes using sockets. The project consists of two main parts: the sender (owner) and the receiver (bot). The sender script sends a Python script to the receiver over a network connection, and the receiver executes the script to disable movement control.

## Getting Started

These instructions will help you understand and set up the project on your local machine for development and testing purposes.

### Prerequisites

You need to have Python installed on both the sender and receiver machines. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/)

### Installation

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/liad07/disable-movement-control.git
   ```

2. Navigate to the project folder.

   ```bash
   cd disable-movement-control
   ```

## Usage

### Sender (Owner) Script

1. Open the `owner_code.py` script.
2. Replace `'bot_ip'` with the actual IP address of the receiver (bot).
3. Run the script using the command:

   ```bash
   python owner_code.py
   ```

4. Enter a command (1, 2, or 3) and press Enter to send the command and script to the receiver.

### Receiver (Bot) Script

1. Open the `client_code.py` script.
2. Run the script using the command:

   ```bash
   python client_code.py
   ```

3. The receiver will wait for a connection and receive the script and command from the sender.

## DISABLEMOVEMENT Script

The `DISABLEMOVEMENT.py` script disables mouse movement and blocks certain keyboard keys. It's a sample script that gets sent and executed by the receiver.

### Customize Supported Keys

You can customize the list of supported keys by modifying the `supported_keys` list in the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

