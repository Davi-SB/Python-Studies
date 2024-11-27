import os
from nbconvert import PythonExporter
import nbformat

def convert_notebooks_to_python(folder_path):
    """
    Converte todos os arquivos Jupyter Notebook (.ipynb) para arquivos Python (.py) em uma pasta e suas subpastas.
    
    Args:
        folder_path (str): Caminho da pasta principal.
    """
    # Percorre a pasta e todas as subpastas
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.ipynb'):
                notebook_path = os.path.join(root, file)
                python_file_path = os.path.join(root, file.replace('.ipynb', '.py'))

                try:
                    # Lê o arquivo notebook
                    with open(notebook_path, 'r', encoding='utf-8') as f:
                        notebook_content = nbformat.read(f, as_version=4)

                    # Converte o notebook para Python usando nbconvert
                    python_exporter = PythonExporter()
                    python_code, _ = python_exporter.from_notebook_node(notebook_content)

                    # Escreve o código Python no novo arquivo
                    with open(python_file_path, 'w', encoding='utf-8') as f:
                        f.write(python_code)
                    
                    print(f"Convertido: {notebook_path} -> {python_file_path}")
                except Exception as e:
                    print(f"Erro ao converter {notebook_path}: {e}")

# Exemplo de uso
folder = "D:\Estudos\Faculdade\codes\.vscode\Python Studies\Explorando a API da OpenAI - .py"
convert_notebooks_to_python(folder)