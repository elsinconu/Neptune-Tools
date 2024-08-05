@echo off

REM Vérifier si Python est déjà installé
python --version >nul 2>&1
if errorlevel 1 (
    echo Python n'est pas installé. Installation en cours...
    
    REM Télécharger l'installateur Python
    powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe', 'python_installer.exe')"
    
    REM Exécuter l'installateur Python
    start /wait python_installer.exe /quiet TargetDir=C:\Python310 PrependPath=1 Include_launcher=1
    del python_installer.exe
    
    REM Vérifier à nouveau si Python est installé
    python --version >nul 2>&1
    if errorlevel 1 (
        echo Installation de Python a échoué. Veuillez installer Python manuellement.
        pause
        exit /b
    )
)

REM Installer les modules Python
echo Installation des modules Python...
python -m pip install requests colorama numpy pandas scipy matplotlib

REM Vérifier si l'installation des modules a réussi
python -c "import requests" >nul 2>&1
if errorlevel 1 (
    echo Une erreur s'est produite lors de l'installation du module requests.
    pause
    exit /b
)
python -c "from colorama import init, Fore, Style" >nul 2>&1
if errorlevel 1 (
    echo Une erreur s'est produite lors de l'installation du module colorama.
    pause
    exit /b
)
python -c "import numpy" >nul 2>&1
if errorlevel 1 (
    echo Une erreur s'est produite lors de l'installation du module numpy.
    pause
    exit /b
)


python -c "import requests" >nul 2>&1
if errorlevel 1 (
    echo Une erreur s'est produite lors de l'installation du module numpy.
    pause
    exit /b
)



python -c "import pandas" >nul 2>&1
if errorlevel 1 (
    echo Une erreur s'est produite lors de l'installation du module pandas.
    pause
    exit /b
)
python -c "import scipy" >nul 2>&1
if errorlevel 1 (
    echo Une erreur s'est produite lors de l'installation du module scipy.
    pause
    exit /b
)
python -c "import matplotlib" >nul 2>&1
if errorlevel 1 (
    echo Une erreur s'est produite lors de l'installation du module matplotlib.
    pause
    exit /b
)

echo Installation terminée avec succès.
pause
