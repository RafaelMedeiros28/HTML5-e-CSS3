import subprocess

def abrir_programa(programa):
    try:
        subprocess.Popen(programa)
        print(f"O programa '{programa}' foi aberto com sucesso.")
    except Exception as e:
        print(f"Erro ao abrir o programa '{programa}': {str(e)}")

caminho_programa = r"C:\Users\PC\AppData\Local\GitHubDesktop\GitHubDesktop.exe"
abrir_programa(caminho_programa)
