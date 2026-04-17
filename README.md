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

### Prerequisites
- **Python 3.10 or higher**
- **CustomTkinter**: `pip install customtkinter`
- **Pillow**: `pip install Pillow`

### How to Run
1. Clone this repository or download the source code.
2. Ensure you have the backend tools (`rpatool` and `unrpyc`) in the project directory.
3. Run the application:
   ```bash
   python m.py
   ```
4. **Step 1**: Select the game executable (`.exe`) to scan the `game` folder.
5. **Step 2**: Select your desired output location.
6. **Step 3**: Select the files you want to process and click **Extract** or **Decompile**.

---

## 📊 Tool Comparison & Details

| Feature | RPA Extraction | RPYC Decompilation |
| :--- | :--- | :--- |
| **Backend Tool** | [rpatool](https://github.com/shizmob/rpatool) | [unrpyc](https://github.com/CensoredUsername/unrpyc) |
| **Input Format** | `.rpa` | `.rpyc` |
| **Output Format** | Images, Audio, etc. | `.rpy` (Source Code) |
| **Error Handling** | Redecisce Fixes | Native unrpyc Logic |

---

## 📜 Credits & Acknowledgments

This GUI application is built upon the incredible work of the following developers and tools:

| Tool | Author / Source | Purpose |
| :--- | :--- | :--- |
| **unrpyc** | [CensoredUsername](https://github.com/CensoredUsername/unrpyc) | The core engine for decompiling `.rpyc` files. |
| **rpatool** | [shizmob](https://github.com/shizmob/rpatool) | The reliable tool for handling Ren'Py Archive (`.rpa`) files. |
| **Redecisce** | Community Fix | Specialized logic used to fix common extraction errors in `.rpa` files. |
| **CustomTkinter** | [TomSchimansky](https://github.com/TomSchimansky/CustomTkinter) | Providing the modern and sleek dark-themed UI components. |

---

## 🔗 Links
- **Patreon**: [Support VastoLordeX](https://www.patreon.com/c/VastoLordeX)
- **Itch.io**: [Download on Itch.io](https://vastolordex.itch.io/rpa-extraction-rpyc-decompilation-engine)
- **GitHub**: [Project Repository](https://github.com/)

---

## ⚠️ Disclaimer
This tool is intended for educational purposes, modding, and translation projects. Please respect the original creators of the games you are analyzing. Ensure you have the right to access the assets before using this tool.
