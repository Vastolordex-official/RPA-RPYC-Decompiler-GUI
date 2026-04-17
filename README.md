# RPA Extraction & RPYC Decompilation Engine

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GUI](https://img.shields.io/badge/UI-CustomTkinter-cyan.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![RenPy](https://img.shields.io/badge/Engine-Ren'Py-ff69b4.svg)](https://www.renpy.org/)

A powerful and user-friendly **Graphical User Interface (GUI)** designed to simplify the process of extracting Ren'Py Archive (`.rpa`) files and decompiling Ren'Py compiled script (`.rpyc`) files back into readable `.rpy` source code.

---

## 🚀 Features

- **Full GUI Experience**: No command-line knowledge required.
- **Batch Processing**: Extract multiple `.rpa` archives or decompile multiple `.rpyc` files at once.
- **Selective Extraction**: Choose exactly which files you want to process using the built-in file scanner.
- **Real-time Terminal**: Integrated log window to monitor the extraction and decompilation progress.
- **Custom Output**: Easily select your desired output directory for extracted assets.
- **Auto-Verification**: Built-in checks to ensure all necessary backend tools are ready.

---

## 🛠️ Installation & Usage

This tool requires **Python 3** to be installed on your system.

### Recommended Installation (for Debian/Ubuntu Users)

For a hassle-free experience with all dependencies built-in, it is highly recommended to use the `.deb` package. You can download it from:

*   [VastoLordeX Itch.io](https://vastolordex.itch.io/rpa-extraction-rpyc-decompilation-engine)
*   [GitHub Releases](https://github.com/)

To install the `.deb` package:

```bash
sudo dpkg -i rpa-tool_1.0.0_all.deb
```

After installation, you can launch the GUI application by typing `rpa-tool` in your terminal.

### Manual Installation (Advanced Users)

To run the GUI manually, follow these steps:

1.  **File Structure**:
    Ensure you have the following files and folders in the same directory:
    *   `RPA-RPYC-Decompiler-GUI.py`
    *   `extractor.py`
    *   `rpatool_new.py`
    *   `unrpyc/` (the complete folder from GitHub)
    *   `profile.gif`
    *   `128x128.png`

2.  **Set up a Virtual Environment**:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install customtkinter pillow packaging darkdetect
    ```

4.  **Run the Application**:
    *   **GUI Version**:
        ```bash
        source .venv/bin/activate
        python RPA-RPYC-Decompiler-GUI.py
        ```
    *   **CLI Version** (Not yet implemented):
        ```bash
        source .venv/bin/activate
        python extractor.py
        ```

### Usage Steps (GUI)
1.  **Select Game EXE**: Click the button to select the game executable (`.exe`). This will scan the associated `game` folder for `.rpa` and `.rpyc` files.
2.  **Select Output Location**: Choose the directory where you want the extracted and decompiled files to be saved.
3.  **Process Files**: Select the specific `.rpa` or `.rpyc` files you wish to process from the lists, then click the respective **Extract** or **Decompile** buttons.

---

## 📊 Tool Comparison & Details

| Feature | RPA Extraction | RPYC Decompilation |
| :--- | :--- | :--- |
| **Backend Tool** | [rpatool](https://github.com/shizmob/rpatool) | [unrpyc](https://github.com/CensoredUsername/unrpyc) |
| **Input Format** | `.rpa` | `.rpyc` |
| **Output Format** | Images, Audio, etc. | `.rpy` (Source Code) |
| **Error Handling** | Redecisce Fixes | Native unrpyc Logic |

---

## ⚠️ Disclaimer

This tool is intended for educational purposes, modding, and translation projects. Please respect the original creators of the games you are analyzing and ensure you have the right to access the assets before using this tool.

**This tool is NOT for sale.** If you modify this GUI, please provide proper credits and acknowledge the original contributors.

---

## 👥 Credits and Contributors

This project is made possible by the contributions of:

*   **VastoLordeX**: Original GUI development and integration.
*   **CensoredUsername**: For the foundational `unrpyc` tool.
*   **shizmob**: For the robust `rpatool`.
*   **Community**: For various fixes and improvements, including the "Redecisce" fixes for RPA extraction errors.

If you encounter any bugs or have suggestions, please open an issue on the [GitHub repository](https://github.com/).

---

## 🔗 Links
- **Patreon**: [Support VastoLordeX](https://www.patreon.com/c/VastoLordeX)
- **Itch.io**: [Download on Itch.io](https://vastolordex.itch.io/rpa-extraction-rpyc-decompilation-engine)
- **GitHub**: [Project Repository](https://github.com/)
