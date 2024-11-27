import os

def delete_jupyter_notebooks(folder_path):
    """
    Apaga todos os arquivos Jupyter Notebook (.ipynb) em uma pasta e suas subpastas.
    
    Args:
        folder_path (str): Caminho da pasta principal.
    """
    # Percorre a pasta e todas as subpastas
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.ipynb'):
                notebook_path = os.path.join(root, file)
                try:
                    # Remove o arquivo
                    os.remove(notebook_path)
                    print(f"Arquivo deletado: {notebook_path}")
                except Exception as e:
                    print(f"Erro ao deletar {notebook_path}: {e}")

# Exemplo de uso
folder = "D:\Estudos\Faculdade\codes\.vscode\Python Studies\Explorando a API da OpenAI - .py"
delete_jupyter_notebooks(folder)
