@echo off
echo Installation des dépendances...

REM Vérifie si pip est installé
python -m ensurepip --default-pip

REM Met à jour pip
python -m pip install --upgrade pip

REM Installe les packages nécessaires
pip install requests colorama

echo Installation terminée.
pause