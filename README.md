# Caixa Eletrônico API

## Descrição

Esta API simula o funcionamento de um caixa eletrônico. Ela recebe um valor de saque desejado e retorna a quantidade de cédulas de cada valor necessárias para compor esse saque, utilizando a menor quantidade de cédulas possível.

### Rotas

### `/api/saque` (POST)

- **Entrada**:
  - `valor`: Inteiro positivo que representa o valor do saque desejado.
  - Exemplo:
    ```json
    {
      "valor": 380
    }
    ```

- **Saída**:
  - JSON contendo a quantidade de cédulas de cada valor.
  - Exemplo:
    ```json
    {
      "100": 3,
      "50": 1,
      "20": 1,
      "10": 1,
      "5": 0,
      "2": 0
    }
    ```

## Principais Desafios

Durante o desenvolvimento deste projeto, um desafio enfrentado foi ao testar a API utilizando o comando curl com o endereço localhost. O comando:

curl -X POST -H "Content-Type: application/json" -d '{"valor": 380}' http://localhost:5000/api/saque

não retornava nenhuma resposta. Após investigar, optei por utilizar o endereço IP padrão 127.0.0.1 como padrão para testes, o que resolveu o problema, ainda não está claro por que localhost não funcionava.

## Instruções para Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/LuisEduardo39/Desafio-T-cnico-Morada.ai.git
   ```
   ```bash
   cd Desafio-T-cnico-Morada.ai
   ```
2.	Instale as dependências:
   ```bash
    pip install -r requirements.txt
   ```
3.	Execute a aplicação:
   ```bash
    python3 app.py
   ```
4.  Em outro terminal, enviar uma solicitação POST com o valor do saque:
   ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"valor": 380}' http://127.0.0.1:5000/api/saque
   ```
5.	Execute os testes:
   ```bash
    python3 -m unittest discover tests
   ```