import ctypes
import os
import sys
from flask import Flask, render_template, request, jsonify
from difflib import SequenceMatcher

app = Flask(__name__, template_folder='templates1')

# --- 1. Load C Library ---
c_lib = None
if sys.platform.startswith('win'):
    lib_name = 'chatbot_lib.dll'
else:
    lib_name = 'chatbot_lib.so'

try:
    if os.path.exists(lib_name):
        c_lib = ctypes.CDLL(f'./{lib_name}')
        c_lib.get_similarity_score.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        c_lib.get_similarity_score.restype = ctypes.c_int
        print(f"SUCCESS: Loaded {lib_name}")
    else:
        print("WARNING: C lib not found. Using Python fallback.")
except Exception:
    print("ERROR: C lib failed. Using Python fallback.")

# --- 2. THE EXPANDED KNOWLEDGE BASE ---
data = {
    # --- DIAGNOSTIC (The new command) ---
    "check engine": "CORE DIAGNOSTIC: I am currently running on " + ("C-LANGUAGE CORE (High Speed)" if c_lib else "PYTHON FALLBACK (Safety Mode)"),

    # --- IDENTITY ---
    "who are you": "I am NeonMind v2.0, a hybrid Python-C AI construct designed for your school project.",
    "what is this project": "This is a web-based chatbot that demonstrates the integration of high-level Python with low-level C code.",
    
    # --- HOW IT WORKS ---
    "how do you work": "I use a Python Flask server as my nervous system and a C language library as my brain for high-speed text processing.",
    "how does the matching work": "I compare your input against my database using the 'Levenshtein Distance' algorithm to find the closest match.",
    "what is levenshtein": "Levenshtein distance is a mathematical formula that calculates how many edits (inserts, deletes, subs) it takes to turn one word into another.",

    # --- TECH STACK ---
    "tech stack": "My architecture: Python (Flask) Backend + C Language Core + HTML5/CSS3 Neon UI.",
    "why use c": "C is used for the heavy lifting. It calculates text similarity much faster than Python can, optimizing performance.",
    "why use python": "Python handles the web server (Flask) because it is excellent for routing and handling HTTP requests.",

    # --- FILE EXPLANATIONS ---
    "explain app.py": "app.py is the main controller. It receives your messages from the browser and sends them to the C library for analysis.",
    "explain chatbot_lib.c": "chatbot_lib.c is my compiled C brain. It contains the raw math logic to compare text strings efficiently.",
    "explain index.html": "index.html is the visual interface. It uses CSS Flexbox and gradients to create this futuristic terminal look.",
    "explain hosting": "I am hosted on a cloud server (like Render). When deployed, the server compiles my C code automatically.",

    # --- SYSTEM COMMANDS ---
    "status": "SYSTEM INTEGRITY: 100%. C-Module: Linked. Python-Core: Active.",
    "security": "FIREWALL: Active. Port 5000 is monitoring for input.",
    "reboot": "INITIATING REBOOT... Cache cleared. RAM flushed. System ready.",
    "developer": "Developed by a student with a passion for mixing high-level and low-level programming.",
    "help": "Click the commands on the left sidebar to query my database."
}

# --- 3. Python Fallback (Smarter Math) ---
def python_similarity(s1, s2):
    return int(SequenceMatcher(None, s1, s2).ratio() * 100)

# --- 4. Logic ---
def get_best_match(user_input):
    best_score = 0
    best_response = ""
    
    for command, answer in data.items():
        if c_lib:
            score = c_lib.get_similarity_score(user_input.lower().encode('utf-8'), command.encode('utf-8'))
        else:
            score = python_similarity(user_input.lower(), command)
        
        if score > best_score:
            best_score = score
            best_response = answer
            
    # Threshold
    if best_score < 55:
        return "ACCESS DENIED: Command not recognized. Please verify syntax."
        
    return best_response

@app.route("/")
def home():
    return render_template("index1.html")

@app.route("/get_response", methods=["POST"])
def get_bot_response():
    user_text = request.form.get("msg", "")
    bot_response = get_best_match(user_text)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)