import json
#import os

try:
    with open('answeredQuestions.json', 'r', encoding="utf8") as f:
        answeredQuestions = json.load(f)
except Exception as e:
    print(f"erro 1: {e}")
    raise

try:
    with open('answeredQuestions.jsonl', 'w', encoding="utf8") as f:
        for message in answeredQuestions:
            # messages é uma chave de um dicionário. está associada com as mensagens
            # as mensagens são dicionários de role e content armazenados numa lista
            line = {"messages": 
                        [
                            {"role": "user", "content": message["question"]},
                            {"role": "assistant", "content": message["answer"]}
                        ]
                }
            # ensure_ascii = False preserva os caracteres especiais
            f.write(json.dumps(line, ensure_ascii=False) + '\n')
except Exception as e:
    print(f"erro 2: {e}")
    raise
    
print("Formatacao concluida com sucesso")