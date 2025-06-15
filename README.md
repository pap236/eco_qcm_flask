# eco_qcm_flask


# Embedding_Eco_QCM_Triche

Analyse sémantique des questions à choix multiples (QCM) en économie à l'aide de modèles de transformation de phrases (`SentenceTransformer`).  
Le projet propose une interface web simple construite avec Flask, permettant de déterminer automatiquement l'option de réponse la plus pertinente selon une question donnée.

## Fonctionnalités

- Saisie d’une question et de ses options via une interface web
- Analyse sémantique avec le modèle `all-MiniLM-L6-v2`
- Affichage de l’option la plus proche sémantiquement
- Calcul du score de similarité cosine
- Interface légère (HTML + CSS minimal)

## Technologies utilisées

- Python 3.x
- Flask
- SentenceTransformers (`all-MiniLM-L6-v2`)
- PyTorch
- HTML/CSS

## Installation

```bash
git clone https://github.com/ton_utilisateur/eco_qcm_flask.git
cd eco_qcm_flask
pip install -r requirements.txt

