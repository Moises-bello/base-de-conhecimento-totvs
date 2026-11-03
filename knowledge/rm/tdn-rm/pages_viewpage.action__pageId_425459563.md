---
content_hash: 64173d616f0b370ae25d7cfdc727c8204a95e0d87453b0eb1cde3b38032130c9
fetched_at: '2026-06-29T00:09:37.130831+00:00'
page_id: '425459563'
product: rm
source: tdn-rm
title: Tipos de Operações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459563
version: 11
---

**Tipos de Operações**

---

**Arredondamento**  
    
 A operação Arredondamento recebe um valor como entrada que é convertido para um decimal (Double) e então são aplicadas as operações definidas no parâmetro de "Tipo de Arredondamento".

Os parâmetros para configurar a operação são:

* **Nome:** Campo somente leitura, tem como valor o tipo da operação.
* **Casas Decimais para Arredondamento:** Número de casas decimais que para a operação de arredondamento.
* **Tipo:** Qual arredondamento. Este parâmetro pode ter como valor:  
    
  + - Arredondar: Arredonda um valor para o inteiro mais próximo. No caso do número 5, arredonda para o número par mais próximo.

**Exemplo**

Entrada = 0.6   
 Tipo = Arredondar  
 O resultado será igual a 1.  
 Exemplo 2:   
 Entrada = 10.5  
 Tipo = Arredondar  
 O resultado será igual a 10.

* + - ParaCima: Arredonda o número decimal para o inteiro mais alto.

**Exemplo**

Entrada = 10.25  
 Tipo = ParaCima   
 O resultado será igual a 11.

* + - ParaBaixo: Arredonda o número decimal para o inteiro mais baixo.

**Exemplo:**

Entrada = 1.9  
 Tipo = ParaBaixo   
 O resultado será igual a 1.

* + TruncarDecimais: Remove a parte decimal do número.

**Exemplo:**

Entrada = 10.25  
 Tipo = TruncarDecimais   
 O resultado será igual a 10.   
    
 **Auto Incremento – (RM)**  
    
 A operação Auto Incremento retorna o valor de incremento do campo. Esses campos são buscados em uma tabela que contém as informações sobre os valores de incremento de cada um deles. Os parâmetros para configurar a operação são:

* **Nome:** Campo somente leitura, tem como valor o tipo da operação.
* **Conexão:** Informe qual é a conexão para a operação de auto incremento.
* **Código Autoincremento:** Informe o código para a operação de auto incremento.

**Concatenação**  
    
 A operação Concatenação recebe duas entradas e resulta em uma saída com os dados concatenados. Os parâmetros para configurar a operação são:

* **Nome:** Nome da operação.
* **Concatenador:** Caracteres que serão incluídos entre as entradas principal e secundária, funcionando como um separador de dados.

**Conversão de Valor**  
    
 A operação Conversão permite que um dado de entrada seja transformado para o tipo de dado escolhido. Os parâmetros para configurar a operação são:

* **Nome:** Nome da operação.
* **Nome:** Campo somente leitura, tem como valor o tipo da operação.
* **Converter para:** Tipo de dados resultante da operação, que pode ser:
  + Texto (converte para String)
  + Número Inteiro (converte para int64)
  + Número Decimal (converte para Double)
  + Data/Hora (converte para DateTime)
  + Lógico (converte para TRUE ou FALSE)

**Data Atual**  
    
 A operação Data Atual retorna a data atual do sistema. Os parâmetros para configurar a operação são:

* **Nome:** Nome da operação.
* **Incluir Hora:** Selecione TRUE ou FALSE para inclusão da hora.

**Geração de Hash**  
    
 Na operação de Geração de Hash, o MD5 (Message-Digest algorithm 5) é um algoritmo de hash de 128 bits unidirecional que pode ser utilizado. A operação recebe a entrada, criptografa os dados e os envia para o campo destino.

* **Nome:** Nome da operação.
* **Algoritmo de Hash:** Informe o algoritmo que será utilizado.

**Lista de Decodificação**  
    
 Na operação Lista de Decodificação, valores de origem são convertidos para um valor de destino específico através de uma lista de conversão. Essa lista contém o valor origem e qual valor destino ele representa.  
    
 Exemplo:

1629751597168\_-1098251740

|  |  |  |
| --- | --- | --- |
| Origem | Destino | Lista |
| Sexo:M ou F | Sexo: 0 ou 1 | M=0 e F=1 |

Nesse exemplo, os valores e os tipos de dados são diferentes . Com a montagem da lista, quando for recebido da origem um valor M, o mesmo será convertido para 0 (da mesma forma para o valor F). Os parâmetros para configurar esta operação são:

* **Nome:** Nome da operação.
* **Valor Padrão**: Valor a ser utilizado caso o valor de origem não corresponda a nenhum dos valores mapeados na propriedade Valores.
* **Valores:** Valores de comparação. Ao clicar no lookup deste campo, uma visão é aberta onde deve ser criada a lista com os valores de origem e destino.

Clique em Collection, no lado esquerdo da visão estão as relações de valores referente ao campo. Abaixo estão disponíveis os botões Add e Remove, para adicionar uma relação ou remover a relação selecionada, respectivamente.   
 No lado direito estão os parâmetros para configuração, que são:

* + **Chave:** Informe a chave do campo na origem.
  + **Valor:** Informe o valor que o campo deverá ter no destino.

**Lookup**  
    
 A operação Lookup recebe um valor e retorna de acordo com as parametrizações realizadas outro valor.   
 Por exemplo, temos as tabelas abaixo:

1629838941968\_1749840403

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | **Pais** | **Pais** | **Detalhe** |  |
| COD | NOME | COD | CAPITAL |  |
| 1 | Brasil | 1 | Brasília |  |
| 2 | Inglaterra | 2 | Londres |  |

A tabela PAISDETALHE está disponível na Lista de Tabelas na Estrutura Origem, mas não foi adicionada nas Tabelas de Importação, e não aparece para realizar as Correspondências. Entretanto, é necessário buscar a capital de um país para ser entrada em um campo no Destino.

Dessa forma, a entrada na operação lookup será o código do país da tabela PAIS (campo COD). A operação irá buscar na tabela PAISDETALHE o campo COD com o valor correspondente ao informado, e retornar o valor do campo CAPITAL.

Os parâmetros para configurar a operação Lookup são:

* **Nome:** Nome da operação.
* **Conexão**: Informe o tipo de conexão de origem utilizada.
* **Entidade:** Informe ou selecione a tabela que será utilizada.
* **Chave:** Informe o campo da tabela que deve ter seu valor comparado com o campo informado na Entrada.
* **Resultado:** Informe o campo que deve ter seu valor retornado pelo lookup.

**Número Sequencial**  
    
 A operação Número Sequencial retorna número sequencial.

* **Nome:** Nome da operação.
* **Valor inicial**: Informe o valor inicial.

**Parte da Data**  
    
 A operação Parte da Data retorna uma parte da data que é recebida como entrada. Os parâmetros para configurar a operação são:

* **Nome:** Nome da operação.
* **Parte da Data:** A parte da data que deseja ser retornada. Pode ser:
  + Dia
  + Mês
  + Ano
  + Dia do ano
  + Dia da semana
  + Hora
  + Minuto
  + Segundo
  + Milisegundo

**Parte do Texto**  
    
 A operação Sub-String recebe uma entrada e retorna somente a sub-string determinada pelos parâmetros.   
 Inicia de uma posição, determinada pelo campo Inicio, e possui um tamanho especifico, retornando o número de caracteres informado no parâmetro Quantidade.  
 A posição do primeiro caractere é zero, conforme exemplo abaixo:  
 B U S I N E S S C O N E C T O R  
 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16  
 Exemplo 1:   
 Início = 0  
 Quantidade = 4  
 Resultado = BUSI  
 Exemplo 2:  
 Início = 5  
 Quantidade = 8  
 Resultado = ESS CONE

A quantidade tem de estar dentro dos limites da string de entrada. Os parâmetros para configurar esta operação são:

* **Nome:** Nome da operação.
* **Comprimento:** Número de caracteres da sub-string.
* **Posição inicial:** Ponto de entrada da operação ou campo.
