import streamlit as st
import streamlit.components.v1 as components

# 1. Moteur de l'application
st.set_page_config(page_title="Aide Mutuelle", layout="centered")

# 2. Le Design et la Logique (HTML/JS)
# C'est ici que se trouve toute ton application
html_final = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        :root { --vert: #27ae60; --bleu: #2980b9; --fond: #f8f9fa; }
        body { font-family: 'Segoe UI', sans-serif; background: var(--fond); margin: 0; text-align: center; }
        .header { background: var(--vert); color: white; padding: 20px; font-size: 22px; font-weight: bold; }
        .card { background: white; border-radius: 15px; padding: 20px; margin: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
        .input-group { margin-bottom: 10px; text-align: left; }
        input { width: 100%; padding: 10px; margin-top: 5px; border: 1px solid #ddd; border-radius: 5px; box-sizing: border-box; }
        .btn { background: var(--vert); color: white; padding: 12px; border: none; border-radius: 50px; width: 100%; font-weight: bold; cursor: pointer; font-size: 16px; }
        .btn-parrain { background: var(--bleu); margin-top: 10px; }
        .bar-bg { background: #eee; border-radius: 10px; height: 20px; margin: 15px 0; overflow: hidden; }
        .bar-fill { background: var(--vert); width: 0%; height: 100%; transition: 1s; }
        .status-badge { background: #f1c40f; color: #000; padding: 5px 10px; border-radius: 5px; font-size: 12px; font-weight: bold; }
    </style>
</head>
<body>

<div class="header">AIDE MUTUELLE 🌍</div>

<div class="container" id="app">
    <div id="page-inscription">
        <div class="card">
            <h3>Bienvenue sur le Réseau</h3>
            <p style="font-size: 13px; color: #666;">Inscrivez-vous pour suivre votre activité.</p>
            <div class="input-group">
                <label>Nom & Prénom</label>
                <input type="text" id="nom" placeholder="Ex: Fatimata ...">
            </div>
            <div class="input-group">
                <label>Numéro de téléphone</label>
                <input type="number" id="tel" placeholder="Ex: 89062806">
            </div>
            <div class="input-group">
                <label>Mot de passe</label>
                <input type="password" id="pass" placeholder="****">
            </div>
            <button class="btn" onclick="allerAuxPacks()">S'inscrire</button>
        </div>
    </div>

    <div id="page-packs" style="display:none;">
        <h3 id="bienvenue-nom"></h3>
        <div class="card">
            <h4>Pack Bronze - 2 000 F</h4>
            <p>Retrait : 1 500 F (x2) | Gaz : 500 F</p>
            <button class="btn" onclick="activerPack('Bronze', 1500)">Choisir</button>
        </div>
        <div class="card">
            <h4>Pack Argent - 5 000 F</h4>
            <p>Retrait : 4 000 F (x2) | Gaz : 1 000 F</p>
            <button class="btn" onclick="activerPack('Argent', 4000)">Choisir</button>
        </div>
        <div class="card">
            <h4>Pack Or - 10 000 F</h4>
            <p>Retrait : 8 000 F (x2) | Gaz : 2 000 F</p>
            <button class="btn" onclick="activerPack('Or', 8000)">Choisir</button>
        </div>
    </div>

    <div id="page-suivi" style="display:none;">
        <div class="card">
            <span class="status-badge" id="etat">Attente Validation</span>
            <h2 id="pack-actif">Pack ...</h2>
            <p id="phrase-social">"L'entraide 2.0 : Ensemble on avance."</p>
            <div class="bar-bg"><div class="bar-fill" id="barre"></div></div>
            <p id="jours-info">Envoyez la capture au +227 89 06 28 06</p>
        </div>

        <div class="card">
            <strong>PARRAINAGE (Boost)</strong><br>
            <small>Réduisez votre attente de 24h par ami inscrit.</small><br>
            <button class="btn btn-parrain" onclick="parrainer()">Parrainer un ami</button>
        </div>

        <button id="btn-retrait" class="btn" style="display:none; background: #f39c12;" onclick="retrait()">Prendre mon Gain</button>
        <button id="btn-sortie" class="btn" style="display:none; background: #c0392b;" onclick="location.reload()">Cycle terminé - Sortir</button>
    </div>
</div>

<script>
    let userNom = "";
    let packNom = "";
    let gainUnitaire = 0;
    let jours = 14;
    let retraitCompteur = 0;

    function allerAuxPacks() {
        userNom = document.getElementById('nom').value;
        if(userNom == "") { alert("Entrez votre nom"); return; }
        document.getElementById('page-inscription').style.display = 'none';
        document.getElementById('page-packs').style.display = 'block';
        document.getElementById('bienvenue-nom').innerText = "Bonjour " + userNom;
    }

    function activerPack(nom, gain) {
        packNom = nom;
        gainUnitaire = gain;
        alert("Action enregistrée ! Patientez pour le couplage.");
        document.getElementById('page-packs').style.display = 'none';
        document.getElementById('page-suivi').style.display = 'block';
        document.getElementById('pack-actif').innerText = "Pack " + packNom;
        
        // Simulation Couplage (Admin Lulu)
        setTimeout(() => {
            alert("🎺 FANFARE ! Vous êtes couplé !");
            document.getElementById('etat').innerText = "EN COURS";
            document.getElementById('etat').style.background = "#2ecc71";
            document.getElementById('jours-info').innerText = "Plus que 14 jours avant retrait.";
            majBarre();
        }, 3000);
    }

    function majBarre() {
        let p = ((14 - jours) / 14) * 100;
        document.getElementById('barre').style.width = p + "%";
        if(jours <= 0) {
            document.getElementById('btn-retrait').style.display = 'block';
            document.getElementById('jours-info').innerText = "Votre gain est prêt !";
        }
    }

    function parrainer() {
        if(jours > 0) {
            jours -= 1;
            alert("Accélération ! -24h d'attente.");
            majBarre();
        }
    }

    function retrait() {
        let code = prompt("ADMIN (Lulu) : Entrez votre code secret Airtel :");
        if(code) {
            retraitCompteur++;
            alert("Gain n°" + retraitCompteur + " envoyé !");
            if(retraitCompteur >= 2) {
                document.getElementById('btn-retrait').style.display = 'none';
                document.getElementById('btn-sortie').style.display = 'block';
                document.getElementById('jours-info').innerText = "Cycle fini. Réinvestissez pour entrer.";
            } else {
                jours = 14; // Relance pour le 2ème gain
                majBarre();
            }
        }
    }
</script>
</body>
</html>
"""

# 3. Affichage
components.html(html_final, height=1000, scrolling=True)
