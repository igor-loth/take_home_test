# ETL em PySpark

Também utilizando os dados de viagens de táxi realizadas em New York, agora vamos construir um processo ETL, este será responsável por escrever um output com as seguintes informações e características:

- Qual vendor mais viajou de táxi em cada ano (**Critério de desempate:** quem percorreu o maior percurso, ordem alfabética dos nomes)
- Qual a semana de cada ano que mais teve viagens de táxi.
- Quantas viagens o vendor com mais viagens naquele ano fez na semana com mais viagens de táxi no ano.

## Pré-Work 
- Clonar o repositório Git em ambiente local.
- Instalar as dependências ```pyspark``` e ```java```:
  
    ```bash
        java -version
        openjdk version "11.0.24" 2024-07-16
        OpenJDK Runtime Environment (build 11.0.24+8-post-Ubuntu-1ubuntu322.04)
        OpenJDK 64-Bit Server VM (build 11.0.24+8-post-Ubuntu-1ubuntu322.04, mixed mode, sharing)
        
        pip list | grep pyspark
        pyspark == 3.5.0
  ```

## Hands-On

- O primeiro passo é acessar o link do dataset e baixá-lo na pasta **dataset/** - [Link do dataset](https://kanastra.notion.site/Take-Home-Test-93ed920a63994d86a8090a9cba3fd08f)
- Ajustar o código [etl_code.py](etl/etl_code.py), incluindo o diretório local que foi salvo o repositório:

  ```python
  # Execução do processo ETL
  if __name__ == "__main__":
      # Passar o diretório local que está salvo o projeto
      etl = SparkETL(dataset_path="{LOCAL DIR}/dataset")
      
      # Carregamento e processamento dos dados
      df = etl.load_data()
      result = etl.transform(df)
      
      # Exportando os resultados - Alterar o LOCAL DIR para o diretório local que está salvo o projeto
      etl.export(result, "{LOCAL DIR}/output/")
  ```

## Resultado

![GET](images/tree_orquestracao.png)
