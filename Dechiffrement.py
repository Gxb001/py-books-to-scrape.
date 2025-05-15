def cipher_caesar(text, shift):
    """
    Applique un chiffrement de César sur le texte avec un décalage donné.
    """
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decipher_caesar(text, shift=None):
    """
    Déchiffre un texte chiffré par César.
    - Si shift est None, retourne une liste de tous les déchiffrements possibles (décalages 1 à 25).
    - Sinon, applique le décalage spécifié pour déchiffrer.
    """
    if shift is None:
        results = []
        for s in range(1, 26):
            deciphered = cipher_caesar(text, -s)
            results.append((s, deciphered))
        return results
    else:
        return cipher_caesar(text, -shift)


def score_word_plausibility(word):
    """
    Évalue la probabilité qu'un mot soit valide en anglais, français ou espagnol.
    Retourne le meilleur score parmi les trois langues basé sur les fréquences des lettres.
    """
    # Fréquences des lettres (approximatives, en %) pour chaque langue
    english_letter_freq = {
        'e': 12.7, 't': 9.1, 'a': 8.2, 'o': 7.5, 'i': 7.0, 'n': 6.7, 's': 6.3,
        'h': 6.1, 'r': 6.0, 'd': 4.3, 'l': 4.0, 'c': 2.8, 'u': 2.8, 'm': 2.4,
        'w': 2.4, 'f': 2.2, 'g': 2.0, 'y': 2.0, 'p': 1.9, 'b': 1.5, 'v': 1.0,
        'k': 0.8, 'j': 0.15, 'x': 0.15, 'q': 0.1, 'z': 0.07
    }
    french_letter_freq = {
        'e': 14.7, 'a': 7.6, 'i': 7.5, 's': 7.2, 'n': 6.9, 'r': 6.6, 't': 6.4,
        'o': 5.4, 'l': 5.3, 'u': 5.0, 'd': 3.7, 'c': 3.3, 'p': 3.0, 'm': 2.5,
        'b': 1.9, 'v': 1.8, 'g': 1.3, 'f': 1.2, 'h': 1.1, 'q': 0.9, 'j': 0.6,
        'x': 0.4, 'y': 0.3, 'z': 0.3, 'k': 0.2, 'w': 0.1
    }
    spanish_letter_freq = {
        'e': 13.7, 'a': 12.5, 'o': 8.7, 's': 7.9, 'n': 6.7, 'i': 6.2, 'r': 6.0,
        'l': 5.0, 'd': 4.7, 'c': 4.0, 't': 3.9, 'u': 3.9, 'm': 3.2, 'p': 2.8,
        'b': 2.2, 'g': 1.7, 'v': 1.2, 'y': 1.1, 'f': 0.7, 'h': 0.7, 'q': 0.5,
        'j': 0.4, 'z': 0.4, 'x': 0.2, 'k': 0.1, 'w': 0.1
    }

    word = word.lower()
    scores = []

    # Calculer un score pour chaque langue
    for lang, freq in [("Anglais", english_letter_freq), ("Français", french_letter_freq),
                       ("Espagnol", spanish_letter_freq)]:
        score = 0

        # Caractéristique 1 : Fréquence des lettres
        letter_freq_score = sum(freq.get(char, 0) for char in word)
        score += letter_freq_score / max(1, len(word))  # Normaliser par la longueur

        # Caractéristique 2 : Nombre de voyelles
        vowels = sum(1 for char in word if char in 'aeiou')
        if 1 <= vowels <= 4 and 5 <= len(word) <= 10:
            score += 20

        # Caractéristique 3 : Pénalité pour trop de consonnes consécutives
        max_consonants = 0
        current_consonants = 0
        for char in word:
            if char not in 'aeiou':
                current_consonants += 1
                max_consonants = max(max_consonants, current_consonants)
            else:
                current_consonants = 0
        if max_consonants > 4:
            score -= 10

        # Caractéristique 4 : Pénalité pour lettres rares dans la langue
        rare_letters = sum(1 for char in word if freq.get(char, 0) < 0.5)
        score -= 5 * rare_letters

        scores.append((lang, score))

    # Retourner le meilleur score parmi les trois langues
    best_lang, best_score = max(scores, key=lambda x: x[1])
    return best_score, best_lang


def xor(text, key):
    """
    Déchiffre un texte chiffré par XOR avec une clé donnée.
    - text : texte chiffré (chaîne ou octets)
    - key : clé de déchiffrement (chaîne)
    Retourne le texte déchiffré sous forme de chaîne ou octets si non décodable.
    """
    if isinstance(text, str):
        text = text.encode('latin1')
    key = key.encode('latin1') if isinstance(key, str) else key
    key_length = len(key)
    result = [byte ^ key[i % key_length] for i, byte in enumerate(text)]
    try:
        return bytes(result).decode('utf-8')
    except UnicodeDecodeError:
        return bytes(result)


# Clé chiffrée
# ciphered_key = "TXAZCELYE"
ciphered_key = "KHOOR"

# 1. Obtenir les 25 déchiffrements
results = decipher_caesar(ciphered_key)
print("\nTous les déchiffrements possibles pour " + ciphered_key + " (décalages 1 à 25) :")
for shift, deciphered in results:
    print(f"Décalage {shift:2}: {deciphered}")

# 2. Évaluer et trier les déchiffrements
scored_results = [(shift, word, *score_word_plausibility(word)) for shift, word in results]
scored_results.sort(key=lambda x: x[2], reverse=True)

# 3. Afficher tous les déchiffrements avec leurs scores et langue probable
print("\nTous les déchiffrements avec scores de plausibilité :")
for shift, word, score, lang in scored_results:
    print(f"Décalage {shift:2}: {word:9} (Score : {score:.2f}, Langue probable : {lang})")

# 4. Afficher les 3 mots les plus probables
print("\nLes 3 mots les plus probables :")
for shift, word, score, lang in scored_results[:3]:
    print(f"Décalage {shift:2}: {word:9} (Score : {score:.2f}, Langue probable : {lang})")

# 5. Confirmation avec le décalage connu
deciphered_key = decipher_caesar(ciphered_key, 11)
print(f"\nDéchiffrement avec décalage 11 : {deciphered_key}")
print(f"Clé de chiffrement César : 11")

# 6. Déchiffrement de secret.txt
with open("secret.txt", "r", encoding="latin1") as f:
    ciphered_text = f.read()
try:
    decrypted_text = xor(ciphered_text, deciphered_key)
    print(f"\nContenu déchiffré de secret.txt :\n{decrypted_text}")
except Exception as e:
    print(f"Erreur lors du déchiffrement : {e}")

"""
1. Avec vos propres mots, expliquer la difference entre chiffrement et hashage.

Hashage impossible de le dé-hashé, contrairement au chiffrement qui est reversible.

2. Qu'est-ce que le salage, et contre quel type d'attaque permet t-il de se proteger ?
Ajouter une valeur aléatoire au mot de passe, contre les attaques de types rainbow table.

3. Que permet l'outil NMAP ?

NMAP permet de scanner un reseau, d'identifier les ports ouverts et les services qui y sont associés.

4. Se renseigner sur le chiffrement S-DES, identifier les differentes etapes.
S-DES est un algorithme de chiffrement symétrique basé sur le DES. Il utilise une clé de 10 bits et effectue 2 tours de chiffrement. Les étapes incluent la génération de clés, la permutation initiale, les substitutions et les permutations finales.

Felicitations, cette fois-ci vous etes bien arrive.e au bout !
"""
