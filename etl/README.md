# ETL em PySpark

Também utilizando os dados de viagens de táxi realizadas em New York, agora vamos construir um processo ETL, este será responsável por escrever um output com as seguintes informações e características:

- Qual vendor mais viajou de táxi em cada ano (**Critério de desempate:** quem percorreu o maior percurso, ordem alfabética dos nomes)
- Qual a semana de cada ano que mais teve viagens de táxi.
- Quantas viagens o vendor com mais viagens naquele ano fez na semana com mais viagens de táxi no ano.

# Hands-On

(**Pré-Work:** Clonar o repositório Git em ambiente local.)

- O primeiro passo é acessar o link do dataset e baixá-lo na pasta **dataset/** - [Link do dataset](https://kanastra.notion.site/Take-Home-Test-93ed920a63994d86a8090a9cba3fd08f)
- Ajustar o código etl_code.py incluindo o diretório local que foi salvo o repositório:
  ```python
      # Construir as imagens 
      docker-compose build

      # Subir o ambiente
      docker-compose up -d
  ```
