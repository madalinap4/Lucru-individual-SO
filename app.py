from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app, resources={r"/*": {"origins": "*"}})

def primul_potrivit(procese, blocuri_libere):
    rezultat = blocuri_libere.copy()
    for proces in procese:
        for i in range(len(rezultat)):
            if rezultat[i] >= proces:
                rezultat[i] -= proces
                break
    return rezultat

def urmatorul_potrivit(procese, blocuri_libere):
    rezultat = blocuri_libere.copy()
    ultima_pozitie = 0
    for proces in procese:
        for i in range(len(rezultat)):
            index = (ultima_pozitie + i) % len(rezultat)
            if rezultat[index] >= proces:
                rezultat[index] -= proces
                ultima_pozitie = index + 1
                break
    return rezultat

def cel_mai_potrivit(procese, blocuri_libere):
    rezultat = blocuri_libere.copy()
    for proces in procese:
        cel_mai_bun_index = -1
        for i in range(len(rezultat)):
            if rezultat[i] >= proces:
                if cel_mai_bun_index == -1 or rezultat[i] < rezultat[cel_mai_bun_index]:
                    cel_mai_bun_index = i
        if cel_mai_bun_index != -1:
            rezultat[cel_mai_bun_index] -= proces
    return rezultat

def cel_mai_nepotrivit(procese, blocuri_libere):
    rezultat = blocuri_libere.copy()
    for proces in procese:
        cel_mai_rau_index = -1
        for i in range(len(rezultat)):
            if rezultat[i] >= proces:
                if cel_mai_rau_index == -1 or rezultat[i] > rezultat[cel_mai_rau_index]:
                    cel_mai_rau_index = i
        if cel_mai_rau_index != -1:
            rezultat[cel_mai_rau_index] -= proces
    return rezultat

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_memory', methods=['POST'])
def process_memory():
    data = request.get_json()
    procese = data.get('procese', [])
    blocuri_libere = data.get('blocuri_libere', [])

    rezultate = {
        "Primul Potrivit": primul_potrivit(procese, blocuri_libere),
        "Urmatorul Potrivit": urmatorul_potrivit(procese, blocuri_libere),
        "Cel Mai Potrivit": cel_mai_potrivit(procese, blocuri_libere),
        "Cel Mai Nepotrivit": cel_mai_nepotrivit(procese, blocuri_libere)
    }

    rezultate_in_rind = {cheie: ", ".join(map(str, valoare)) for cheie, valoare in rezultate.items()}

    return jsonify(rezultate_in_rind)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8082)
