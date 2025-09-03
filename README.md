<p style="text-align: center"><img src="docs/images/logo/click-helper-logo.png" alt="click-helper-logo"></p>

# click-helper - automate your GUI with a simple, human-friendly language

click-helper is a tool for GUI automation. Its purpose is to simplify the process of creating automation scripts, making it accessible to a wider audience.

The project uses a YAML-based configuration file to define automation steps. This declarative approach eliminates the need to write complex programming code for routine tasks.

The structure of click-helper allows scripts to be easy to read, modify, and share with others. The tool was developed to be a straightforward solution for automating repetitive desktop tasks.

Users define their actions using simple commands, such as `CLICK(X, Y)` for a click at a specific coordinate or `OPEN(app)` to start an application. The instructions are executed in the order they appear in the configuration file.

## FEATURES

- **YAML-based Language**: Use a human-readable and declarative language to write scripts, making them clear and easy to maintain.

- **Structured Logs**: Integrates with Grafana Loki to provide structured logs for better monitoring and debugging.

- **Single-file Commands**: All commands are defined in one configuration file, simplifying the management and organization of your automation scripts.

## REQUIREMENTS

To run click-helper, you need Python 3+ and Poetry installed.

## QUICK START

The project's dependencies are managed by Poetry, but you have two options for setup:

- **Option 1 (Recommended)**: Use the `start.sh` script. It handles all dependency installations and launches the application for you.
You just need to make the file executable:

```bash
chmod +x start.sh
./start.sh
```

- **Option 2 (Manual)**: If you prefer a manual setup, you'll need to install the core dependencies first, which include the `python3-tk` and `python3-dev` packages.


- Next, you must have Poetry installed to manage the project's dependencies. Once Poetry is set up, you can install the necessary packages and run the application with these commands:

```bash
poetry install
poetry run python -m src.click_helper.main
```

## HOW TO CHANGE COMMANDS

The list of commands is modular and can be easily expanded. The logic for each command is linked to a function in the source code.

To add a new command, follow these steps:

1. Open the source code file where the commands are handled (`src/click_helper/files/command_script.yaml`).

2. In your YAML file, add the new commands and save the file.

3. Run the application again, and it will automatically recognize the new commands.

## SUPPORTED COMMANDS

The click-helper tool supports a range of commands for automating GUI tasks. These commands are executed sequentially, based on the order they appear in your YAML configuration file.

- `LOG: "<message>"`: Writes a custom message to the structured log. It expects a string value enclosed in quotation marks.

- `WAIT: <time_in_seconds>`: Pauses the script execution for a specified duration. It expects a number representing the number of seconds to wait.

- `OPEN_PROCESS: ["<process_name>"]`: Starts a new process or opens an application on your system. It expects a list of strings containing the name of the process.

- `HOTKEY: ["<command_01>", "<command_02>", "<command_03>"]`: Simulates pressing a specific keyboard hotkey combination. It expects a list of strings, where each string is a key to be pressed (e.g., `ctrl` + `alt` + `s`).

- `MOVE_TO: [<x_coordinate>, <y_coordinate>]`: Moves the mouse cursor to a specific screen location. It expects a list of two numbers representing the x and y coordinates.

- `CLICK: []`: Performs a mouse click at the current cursor position.

- `WRITE: "<message>"`: Types a string of text, simulating keyboard input. It expects a string value enclosed in quotation marks.

### COMMAND FILE EXAMPLE

```yaml
- LOG: "Initializing 'click-helper' command script"
- WAIT: 1
- WAIT: 1
- OPEN_PROCESS: ["google-chrome"] # Open Google Chrome
- WAIT: 5 # Wait for the browser to open and all elements to load
- HOTKEY: ["win", "up"] # Maximize window
- HOTKEY: ["ctrl", "l"] # Focus address bar
- MOVE_TO: [2264, 66] # Coordinates for the address bar
- WAIT: 1
- CLICK: [] # Click on the current mouse position
- WRITE: "Hello, World!" # Type "Hello, World!"
- LOG: "Done"
```

## LICENSE

click-helper is an open-source software distributed under the **[MIT License](https://opensource.org/license/MIT)**.

- **Open Source**: The source code is always visible and accessible to everyone.

- **Freedom to Use**: You are free to use, copy, modify, distribute, and sublicense the software, including for commercial purposes.

- **Extensible**: Feel free to add your own features and components.

The full license and terms can be found in the **[LICENSE.md](./LICENSE.md)** file.