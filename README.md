# Python Utilities Collection

A diverse set of Python tools and applications for various purposes, from productivity to entertainment.
This repository was made just to pratice python coding so feel free to use any of this code :).

## 🔧 Requirements
Python 3.6+
External packages:
    - requests
    - python-dotenv
    - colorama

## 📦 Projects Overview

### 🌤️ Weather Fetcher (`pocasi.py`)
Retrieve current weather information for Prague using the OpenWeatherMap API.

**Features:**
- Real-time temperature data
- Weather condition descriptions
- Easy city modification (in code)

**Setup:**
1. Obtain API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Create `.env` file with `API=your_api_key_here`
3. Install dependencies: `pip install requests python-dotenv`

### ✅ Interactive TODO Manager (`TODO.py`)
A console-based task management system with persistent storage.

**Features:**
- Add, complete, and delete tasks
- Set completion dates
- JSON-based data persistence
- Simple intuitive interface

### 🎮 Text Adventure Game (`game.py`)
A class-based RPG adventure with combat, inventory, and exploration.

**Features:**
- Three character classes (Mage, Warrior, Archer)
- Turn-based combat system
- Random encounters (monsters, treasure, NPCs)
- Progressive difficulty scaling
- Colorful console output

**Install game dependencies:**
```bash
pip install colorama
```
**🔐 Password Generator (pass_gen.py)**
Generate secure random passwords with customizable length.

**Features:**
- Adjustable password length (user-defined)
- Alphanumeric character set (letters + digits)
- Simple command-line interface

**No external dependencies**

**Usage:**
```bash
python pass_gen.py
```
**Example:**
Enter the amount of symbols: 12
Output: e.g., "X7fK9p2qR8tL"

