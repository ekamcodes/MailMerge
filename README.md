
# Mail Merge Project ✉️

This is a simple Python script that automates the creation of personalized letters using a template and a list of names.

## 📌 What It Does

The script:
- Reads a list of names from `invited_names.txt`
- Loads a letter template from `start_letter.txt`
- Replaces the placeholder `[name]` with each person's name
- Generates a new letter for each person in the `Output/ReadyToSend/` folder

---

## 🗂 Folder Structure

```
MailMergeProject/
├── Input/
│   ├── Letters/
│   │   └── start_letter.txt
│   └── Names/
│       └── invited_names.txt
├── Output/
│   └── ReadyToSend/
│       └── letter_<name>.txt
├── main.py
└── .gitignore
```

---

## ▶️ How to Run

1. Make sure you have Python 3 installed.
2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Run the script:

   ```bash
   python main.py
   ```

---

## ✏️ Customize

- Replace `start_letter.txt` with your own letter template.
- Add or update names in `invited_names.txt`.

---

## 📁 Output

Generated letters will be saved to:

```
Output/ReadyToSend/
```

Each letter will be named like: `letter_John.txt`, `letter_Emily.txt`, etc.

---

## 🛠 Requirements

This script uses only built-in Python libraries — no external dependencies required.
