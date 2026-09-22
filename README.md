# iPhoneModelTool

A lightweight, portable command-line tool designed to help forensic examiners and investigators quickly narrow down and identify iPhone models based on physical characteristics. 

Built with **Python standard libraries only**, this tool requires no external package installations (`pip`), making it secure and simple to run on locked-down lab workstations or standalone field laptops.

---

## Features

* **Interactive Menu-Driven Interface:** Numbered options minimize input errors during fast-paced examinations.
* **Skip Capability:** Investigators can easily bypass questions when a specific physical trait is ambiguous, damaged, or unknown.
* **Dynamic SQL Filtering:** Uses a local SQLite database (`iphones.db`) to rapidly filter down potential matches as data points are entered.
* **Multi-Value Attribute Support:** Efficiently handles complex fields (such as special colour variants shared across multiple models) using comma-safe matching logic.
* **Zero Dependencies:** Runs entirely on Python's built-in `sqlite3` and `csv` modules.

---

## Tech Stack

* **Language:** Python 3.x
* **Database:** SQLite3 (local, file-based)
* **Dependencies:** None (uses built-in modules: `sqlite3`, `csv`, `sys`, etc.)

---

## Project Structure

* **iPhone_quiz.py**       The main interactive CLI identification script
* **iphones.db**          The SQLite database containing information on each iPhone model

---

## How To Use

* Un-zip folder to a known location (ie. Documents)
  * MD5 hash `8c7ab9a141f8a2da762642eb0848a358`
* Open Command Prompt and navigate to folder where files are saved (ie. `cd C:\Users\\**[USER]**\Documents\iPhoneModelTool`)
* run the following command: `python iPhone_quiz.py`
* answer questions until final results are given 
