# Arquitetura da Plataforma de Dados para eventos

Sabendo que hoje temos serviços de aplicativos que conectam motoristas e pessoas que precisam de carona, possibilitando a criação de uma alternativa ao táxi. Imagine que temos as seguintes fontes de dados:

- **Usuários:** Contempla clientes e motoristas identificados por uma coluna tipo.
- **Corridas:** Referência cliente e motorista, também contém informações sobre a viagem realizada.

Vamos criar um desenho de solução que utiliza CDC para coletar informações de ambas as fontes e une os dados e armazena em um Data Lake.
Lembrando que não podemos ter corridas sem usuários cadastrados, então não pode haver assincronia entre os dados.

## Desenho da Arquitetura

 ![GET](image/main_mage.png)
 
## Ferramentas Utilizadas

