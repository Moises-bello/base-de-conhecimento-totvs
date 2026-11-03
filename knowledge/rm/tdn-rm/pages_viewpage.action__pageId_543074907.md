---
content_hash: 6c0efec85ef163013e0ad91e74c5f8fff104dba21c7bb925420e61387d4b4a5b
fetched_at: '2026-06-29T00:10:38.029526+00:00'
page_id: '543074907'
product: rm
source: tdn-rm
title: Gestão - Funções de Fórmulas - Contratos de Venda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=543074907
version: 63
---

TOTALITEMCOMPOSICAOQTDECOMISSIOANDOSCOMISSAOTABCOMISSOESITEM

**1. CONDVENDA**  
Busca informações da condição da venda

**2.1. Contexto**   
Contrato de venda/aluguel

****SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234****

**2.2. Sintaxe**  
CONDVENDA ( VALOR1, VALOR2, STRING1, STRING2 )  
A sintaxe da função CONDVENDA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR1 – Código do grupo
  + VALOR2 – Código do componente
  + STRING1 – Nome do campo da tabela de regra da venda
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**2.3. Exemplo**  
CODVENDA(1,1,'QTD\_PARC','I')

**3. CONTEXTO**  
Tabela de Contexto do Reajuste Mensal

**3.1. Contexto**  
Reajuste contratual de venda/aluguel

**3.2. Sintaxe**  
CONTEXTO ( STRING )  
A sintaxe da função CONTEXTO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING – Nome do campo da tabela carregada no contexto

**4. CUSTOINCORRIDO**  
Busca o valor do custo incorrido

**4.1. Contexto**  
Apuração de resultado contábil pelo POC (Resolução 963)

**4.2. Sintaxe**  
CUSTOINCORRIDO ( VALOR1, VALOR2, VALOR3, VALOR4, DATA, STRING ).

A sintaxe da função CUSTOINCORRIDO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR1 – Código da coligada
  + VALOR2 – Código do projeto
  + VALOR3 – Código da obra
  + VALOR4 – Código da etapa
  + DATA – Data da apuração
  + STRING – Código do usuário

**5. CUSTOORCADO**  
Busca o valor do custo orçado

**5.1. Contexto**  
Apuração de resultado contábil pelo POC (Resolução 963)

**5.2. Sintaxe**  
CUSTOORCADO ( VALOR1, VALOR2, VALOR3, VALOR4, DATA, STRING ).  
A sintaxe da função CUSTOORCADO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR1 – Código da coligada
  + VALOR2 – Código do projeto
  + VALOR3 – Código da obra
  + VALOR4 – Código da etapa
  + DATA – Data da apuração
  + STRING – Código do usuário

**6. CUSTOORCADOREMANESCENTE**  
Busca o valor do custo orçado remanescente

**6.1. Contexto**  
Apuração de resultado contábil pelo POC (Resolução 963)

**6.2. Sintaxe**  
CUSTOORCADOREMANESCENTE ( VALOR1, VALOR2, VALOR3, VALOR4, DATA, STRING)  
A sintaxe da função CUSTOORCADOREMANESCENTE tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR1 – Código da coligada
  + VALOR2 – Código do projeto
  + VALOR3 – Código da obra
  + VALOR4 – Código da etapa
  + DATA – Data da apuração
  + STRING – Código do usuário

**7. DATBASE**  
Retorna a data base do componente

**7.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**7.2. Sintaxe**  
DATBASE

**8. DATREAJUSTE**  
Retorna a data do Reajuste da Parcela

**8.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**8.2. Sintaxe**  
DATREAJUSTE

**9. EXTENSODATA**  
Retorna uma data por extenso

**9.1. Contexto**  
Independente do contexto

**9.2. Sintaxe**  
EXTENSODATA ( DATA )  
A sintaxe da função EXTENSODATA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + DATA – Data a ser retorna por extenso

**9.3. Exemplo**  
EXTENSODATA('20/03/2010')

**10. TABSECURITIZACAO**  
Retorna o valor de um campo da tabela de Securitização

**10.1. Contexto**  
Securitização

**SELECT \* FROM XSECURITIZACAO** **WHERE ID= 1234**

**10.2. Sintaxe**

TABSECURITIZACAO( STRING1, STRING2 )  
A sintaxe da função TABSECURITIZACAO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela de venda
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**10.3. Exemplo**  
TABSECURITIZACAO('ID','I')

**11. TABSECURITIZACAOCOMPL**  
Retorna o valor de um campo da tabela complementar de Securitização

**11.1. Contexto**

Securitização

**SELECT \* FROM XSECURITIZACAOCOMPL****WHERE ID= 1234**

**11.2. Sintaxe**

TABSECURITIZACAOCOMPL( STRING1, STRING2 )  
A sintaxe da função TABSECURITIZACAOCOMPL tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela de venda
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**11.3. Exemplo**  
TABSECURITIZACAOCOMPL('ID','I')

**12. EXTENSONUMERO**  
Retorna um número por extenso

**12.1. Contexto**  
Independente do contexto

**12.2. Sintaxe**  
EXTENSONUMERO ( VALOR )  
A sintaxe da função EXTENSONUMERO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR – Número a ser retornado por extenso

**12.3. Exemplo**  
EXTENSONUMERO(1453)

**13. EXTENSOVALOR**  
Retorna um valor por extenso

**13.1. Contexto**  
Independente do contexto

**13.2. Sintaxe**  
EXTENSOVALOR ( VALOR )  
A sintaxe da função EXTENSOVALOR tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR – Valor a ser retornado por extenso

**13.3. Exemplo**  
EXTENSOVALOR(156.14)

**14. FORMATANUMERO**  
Retorna um número formatado em inteiro

**14.1. Contexto**  
Independente do contexto

**14.2. Sintaxe**  
FORMATANUMERO ( VALOR )  
A sintaxe da função FORMATANUMERO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR – Valor a ser formatado para o padrão inteiro

**14.3. Exemplo**  
FORMATANUMERO(156.14)

**15. FORMATAVALOR**  
Retorna um valor formatado em moeda

**15.1. Contexto**  
Independente do contexto

**15.2. Sintaxe**  
FORMATAVALOR ( VALOR )  
A sintaxe da função FORMATAVALOR tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR – Valor a ser formatado para o padrão moeda

**15.3. Exemplo**  
FORMATAVALOR(152.6)

**16. GPCODCOMPN**  
Retorna o código do componente de Juros ou CM

**16.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**16.2. Sintaxe**  
GPCODCOMPN

**17. GPCODCOMPNPRINCIPAL**  
Retorna o código do componente principal

**17.1. Contexto**  
Geração do plano de financiamento

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**17.2. Sintaxe**  
GPCODCOMPNPRINCIPAL

**18. GPCODGRUPO**  
Retorna o código do grupo

**18.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**18.2. Sintaxe**  
GPCODGRUPO

**19. GPCODTIPOCOMPN**  
Retorna o código do tipo de Componente dos Juros ou CM

**19.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**19.2. Sintaxe**  
GPCODTIPOCOMPN

**20. GPCODTIPOPARC**  
Retorna o código do tipo da parcela

**20.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**20.2. Sintaxe**  
GPCODTIPOPARC

**22. GPGETDATABASE**  
Retorna a data de referência de reajuste (Data de início do componente)

**22.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**22.2. Sintaxe**  
GPGETDATABASE

**23. GPGETDATAENTREGA**  
Retorna a data de entrega do empreendimento

**23.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**23.2. Sintaxe**  
GPGETDATAENTREGA

**24. GPGETPERIODOMESES**  
Retorna o Período em meses da data base até o vencimento da parcela

**24.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**24.2. Sintaxe**  
GPGETPERIODOMESES

**25. GPGETSALDODEVEDORAMORTIZADO**  
Retorna o saldo devedor amortizado até o vencimento da parcela

**25.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**25.2. Sintaxe**  
GPGETSALDODEVEDORAMORTIZADO

**26. GPNUMPARC**  
Retorna o número da parcela

**26.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**26.2. Sintaxe**  
GPNUMPARC

**27. GPNUMVENDA**  
Retorna o número da venda

**27.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**27.2. Sintaxe**  
GPNUMVENDA

**29. GPXPARCELAPAGAMENTO**  
Acessa os campos da parcela

**29.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM **XPARCELAPAGAMENTO**WHERE NUM\_VENDA = 1234**

**29.2. Sintaxe**  
GPXPARCELAPAGAMENTO ( STRING )  
A sintaxe da função GPXPARCELAPAGAMENTO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING – Campo que se deseja ter acesso da parcela

**30. GPXREGRACOMPONENTEVENDA**  
Acesso aos campos da Regra no Grupo

**30.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XREGRACOMPONENTEVENDA WHERE NUM\_VENDA = 1234**

**30.2. Sintaxe**  
GPXREGRACOMPONENTEVENDA ( STRING )  
A sintaxe da função GPXREGRACOMPONENTEVENDA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING - Campo que se deseja ter acesso da regra no grupo

**31. GPXREGRACOMPONENTEVENDAPRINCIPAL**  
Acesso aos campos da Regra Principal

**31.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**31.2. Sintaxe**  
GPXREGRACOMPONENTEVENDAPRINCIPAL ( STRING )  
A sintaxe da função GPXREGRACOMPONENTEVENDAPRINCIPAL tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING - Campo que se deseja ter acesso da regra principal

**32. GPXVENDA**  
Acesso aos campos da venda

**32.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**32.2. Sintaxe**  
GPXVENDA ( STRING )  
A sintaxe da função GPXVENDA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING - Campo que se deseja ter acesso da venda

**33. JUROSMORA**  
Retorna o valor de juros de mora por atraso, de todas as parcelas em aberto ou parcialmente quitadas, vencidas de um contrato.

**33.1. Contexto**  
Contrato de venda/aluguel

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**33.2. Sintaxe**  
JUROSMORA ( VALOR1, VALOR2, DATA, STRING )  
A sintaxe da função JUROSMORA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR1 – Código da coligada
  + VALOR2 – Número da venda
  + DATA – Data referência
  + STRING – Código do usuário

**33.3. Exemplo**  
JUROSMORA(1,1,'24/06/2001','mestre')

**34. MULTA**  
Retorna o valor de multa por atraso, de todas as parcelas em aberto ou parcialmente quitadas, vencidas de um contrato.

**34.1. Contexto**  
Contrato de venda/aluguel

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**34.2. Sintaxe**  
MULTA ( VALOR1, VALOR2, DATA, STRING )  
A sintaxe da função MULTA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR1 – Código da coligada
  + VALOR2 – Número da venda
  + DATA – Data referência
  + STRING – Código do usuário

**34.3. Exemplo**  
MULTA(1,3,'24/06/2001','mestre')

**35. NUMPARC**  
Retorna o número de uma parcela.

**35.1. Contexto**  
Reajuste contratual de venda/aluguel.

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**35.2. Sintaxe**  
NUMPARC

**36. NUMVENDA**  
Retorna o número de uma venda/aluguel.

**36.1. Contexto**  
Reajuste contratual de venda/aluguel.

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**36.2. Sintaxe**  
NUMVENDA

**37. CODGRUPO**  
Retorna o código de um grupo.

**37.1. Contexto**  
Reajuste contratual de venda/aluguel.

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**37.2. Sintaxe**  
CODGRUPO

**38. CODCOMPN**  
Retorna o código do componente de reajuste

**38.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**38.2. Sintaxe**  
CODCOMPN

**39. CODTIPOCOMPN**  
Retorna o código do tipo do componente de reajuste

**39.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**39.2. Sintaxe**  
CODTIPOCOMPN

**40. CODTIPOPARC**  
Retorna o código do tipo de uma parcela

**40.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**40.2. Sintaxe**  
CODTIPOPARC

**41. PERIODOANUAL**  
Retorna o período anual entre a data base até o vencimento da parcela retornando a diferença de anos.

**41.1. Contexto**  
Reajuste contratual de venda/aluguel.

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**41.2. Sintaxe**  
PERIODOANUAL

**42. PERIODOMENSAL**  
Retorna o período mensal entre a data base até o vencimento da parcela retornando a diferença de meses.

**42.1. Contexto**  
Reajuste contratual de venda/aluguel.

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**42.2. Sintaxe**  
PERIODOMENSAL

**43. DIFERENCADIAS**  
Retorna a Diferença de dias entre duas datas

**43.1. Contexto**  
Independente do contexto

**43.2. Sintaxe**  
DIFERENCADIAS ( DATA1, DATA2 )  
A sintaxe da função DIFERENCADIAS tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + DATA1 – Primeira Data
  + DATA2 – Segunda Data

**43.3. Exemplo**  
DIFERENCADIAS('10/03/2012','10/02/2012')

**44. DIFERENCAMESES**  
Retorna a Diferença de meses entre duas datas

**44.1. Contexto**  
Independente do contexto

**44.2. Sintaxe**  
DIFERENCAMESES ( DATA1, DATA2 )  
A sintaxe da função DIFERENCAMESES tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + DATA1 – Primeira Data
  + DATA2 – Segunda Data

**44.3. Exemplo**  
DIFERENCAMESES('10/03/2012','10/02/2012')

**45. ADICIONADIAS**  
Adiciona Dias a uma Data

**45.1. Contexto**  
Independente do contexto

**45.2. Sintaxe**  
ADICIONADIAS ( STRING, DATA1, DATA2, DATA3, VALOR1, VALOR2 )  
A sintaxe da função ADICIONADIAS tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + DATA – Data para adicionar dias
  + DIAS – Dias a ser adicionado a uma data

**45.3. Exemplo**  
ADICIONADIAS('10/03/2012',10)

**46. ADICIONAMESES**  
Adiciona Meses a uma Data

**46.1. Contexto**  
Independente do contexto

**46.2. Sintaxe**  
ADICIONAMESES ( DATA, MESES)  
A sintaxe da função ADICIONAMESES tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + DATA – Data para adicionar dias
  + MESES – Meses a ser adicionado a uma data

**46.3. Exemplo**  
ADICIONAMESES('10/03/2012',10)

**47. ADICIONAANOS**  
Adiciona Anos a uma Data

**47.1. Contexto**  
Independente do contexto

**47.2. Sintaxe**  
ADICIONAANOS ( DATA, ANOS )  
A sintaxe da função ADICIONAANOS tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* DATA – Data para adicionar anos
* ANOS – Anos a ser adicionado a uma data

**47.3. Exemplo**  
ADICIONAANOS('10/03/2012',10)

**48. RECALCULACORRECAOMONETARIA**  
Calcula a Variação da Correção Monetária em memória  (Utiliza o índice acumulado)

**48.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**48.2. Sintaxe**  
RECALCULACORRECAOMONETARIA ( STRING, DATA1, DATA2, DATA3, VALOR1, VALOR2 )  
A sintaxe da função RECALCULACORRECAOMONETARIA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING – Moeda
  + DATA1 – Data Inicial
  + DATA2 – Data Final
  + DATA3 – Data de vencimento da parcela
  + VALOR1 – Periodicidade
  + VALOR2 – Meses de defasagem

**49. REXPARCELACOMPONENTE**  
Retorna o valor de um campo de uma parcela do componente em memória (sem acesso ao banco de dados)

**49.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**49.2. Sintaxe**  
REXPARCELACOMPONENTE ( VALOR, STRING )  
A sintaxe da função REXPARCELACOMPONENTE tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* VALOR – Código do componente
* STRING - Campo que se deseja ter acesso da parcela

**50. REXPARCELAPAGAMENTO**  
Retorna o valor de um campo de uma parcela de pagamento em memória (sem acesso ao banco de dados)

**50.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**50.2. Sintaxe**  
REXPARCELAPAGAMENTO ( STRING )  
A sintaxe da função REXPARCELAPAGAMENTO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* STRING - Campo que se deseja ter acesso da parcela

**51. REXREGRACOMPONENTEVENDA**  
Acesso aos campos da Regra no Grupo em memória (sem acesso ao banco de dados)

**51.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM **XREGRACOMPONENTEVENDA**WHERE NUM\_VENDA = 1234**

**51.2. Sintaxe**  
REXREGRACOMPONENTEVENDA ( VALOR, STRING )  
A sintaxe da função REXREGRACOMPONENTEVENDA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* VALOR – Código do componente
* STRING – Campo que se deseja ter acesso da regra no grupo

**52. REXVENDA**  
Acesso aos campos da venda em memória (sem acesso ao banco de dados)

**52.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**52.2. Sintaxe**  
REXVENDA ( STRING )  
A sintaxe da função REXVENDA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING – Campo que se deseja ter acesso da venda

**53. SALDONEGATIVOVENDA**  
Retorna o saldo negativo de uma venda.

**53.1. Contexto**  
Contrato de Venda/Aluguel

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**53.2. Sintaxe**  
SALDONEGATIVOVENDA ( VALOR )  
A sintaxe da função SALDONEGATIVOVENDA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* VALOR – Número da venda

**53.3. Exemplo**  
SALDONEGATIVOVENDA(1)

**54. SOMATIPOCOMPN**  
Soma o valor de um tipo de componente

**54.1. Contexto**  
Contrato de Venda/Aluguel

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**54.2. Sintaxe**  
SOMATIPOCOMPN ( STRING1, STRING2 )  
A sintaxe da função SOMATIPOCOMPN tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* STRING1 – Tipo do componente
* STRING2 – Situação da parcela

**54.3. Exemplo**  
SOMATIPOCOMPN('1','2')

**55. SOMATIPOPARCELA**  
Soma o valor de um tipo de parcela

**55.1. Contexto**  
Contrato de Venda/Aluguel

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**55.2. Sintaxe**  
SOMATIPOPARCELA ( STRING1, STRING2 )  
A sintaxe da função SOMATIPOPARCELA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* STRING1 – Tipo de parcela
* STRING2 – Situação da parcela

**55.3. Exemplo**  
SOMATIPOPARCELA('2','2')

**56. TABCOMISSAO**  
Retorna o valor de um campo qualquer da tabela de comissão (XCOMISSAO)

**56.1. Contexto**  
Contrato de venda/aluguel

**56.2. Sintaxe**  
TABCOMISSAO ( STRING1, STRING2 )  
A sintaxe da função TABCOMISSAO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela comissão
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**56.3. Exemplo**  
TABCOMISSAO('NUMVENDA','I')

**57. TABCOMISSAOPARCELA**  
Retorna o valor de um campo qualquer da tabela de comissão (XCOMISSAOPARCELAMENTO)

**57.1. Contexto**  
Contrato de venda/aluguel

**57.2. Sintaxe**  
TABCOMISSAOPARCELA( STRING1, STRING2 )  
A sintaxe da função TABCOMISSAOPARCELA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela comissão
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**57.3. Exemplo**  
TABCOMISSAOPARCELA('NUMVENDA','I')

**58. TABCOMISSAOCOMPL**  
Retorna o valor de um campo qualquer da tabela de campo complementar de comissão (XCOMISSAOCOMPL)

**58.1. Contexto**  
Contrato de venda/aluguel

**58.2. Sintaxe**  
TABCOMISSAOCOMPL ( STRING1, STRING2 )  
A sintaxe da função TABCOMISSAOCOMPL tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* STRING1 – Nome do campo da tabela de campo complementar de comissão
* STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**58.3. Exemplo**  
TABCOMISSAOCOMPL('CODCOMISSAO','V')

**59. TABDISTRATO**  
Retorna o valor de um campo qualquer da tabela de distrato (XDISTRATO).

**59.1. Contexto**  
Contrato de venda/aluguel

**59.2. Sintaxe**  
TABDISTRATO ( STRING1, STRING2 )  
A sintaxe da função TABDISTRATO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* STRING1 – Nome do campo da tabela de distrato
* STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**59.3. Exemplo**  
TABDISTRATO('NUMVENDA','I')

**60. TABDISTRATOCOMPL**  
Retorna o valor de um campo qualquer da tabela de campo complementar de distrato (XDISTRATOCOMPL).

**60.1. Contexto**  
Contrato de venda/aluguel

**60.2. Sintaxe**  
TABDISTRATOCOMPL ( STRING1, STRING2 )  
A sintaxe da função TABDISTRATOCOMPL tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* STRING1 – Nome do campo da tabela de campo complementar de distrato
* STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**60.3. Exemplo**  
TABDISTRATOCOMPL('NUMVENDA','I')

**61. TABITEMVENDA**  
Retorna o valor de um campo qualquer da tabela de item da venda (XITEMVENDA).

**61.1. Contexto**  
Contrato de venda/aluguel

**61.2. Sintaxe**  
TABITEMVENDA ( STRING1, STRING2 )  
A sintaxe da função TABITEMVENDA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela de item de venda
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**61.3. Exemplo**  
TABITEMVENDA('VR\_ITEM','V')

**62. TABREGRA**  
Retorna o valor de um campo qualquer da tabela de regras da venda/aluguel (XREGRACOMPONENTEVENDA).

**62.1. Contexto**  
Regra da Venda/Aluguel.

**SELECT \* FROM XREGRACOMPONENTEVENDA WHERE NUM\_VENDA = 1234**

**62.2. Sintaxe**  
TABREGRA ( STRING1, STRING2 )  
A sintaxe da função TABREGRA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela de regra da venda
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**62.3. Exemplo**  
TABREGRA('COD\_TIPO\_PER','S')

**63. CODEMPREENDIMENTO**  
Retorna o código do empreendimento da venda.

**63.1. Contexto**

Contrato de venda/aluguel e POC

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**63.2. Sintaxe**  
CODEMPREENDIMENTO

**64. TABVENDA**  
Retorna o valor de um campo qualquer da tabela de venda (XVENDA).

**64.1. Contexto**  
Contrato de venda/aluguel

Para o contexto de clientes que usam o novo reajuste foi disponibilizado uma coluna **TABVENDA('DATAREFERENCIA', D)** que retorna a data do parâmetro que foi passada no processo ou que foi executada

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**64.2. Sintaxe**  
TABVENDA ( STRING1, STRING2 )  
A sintaxe da função TABVENDA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela de venda
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**64.3. Exemplo**  
TABVENDA('DAT\_VENDA','D')

**65. TOTALDIASANO**  
Retorna o total de dias de um determinado ano.

**65.1. Contexto**  
Independente do contexto

**65.2. Sintaxe**  
TOTALDIASANO ( VALOR )  
A sintaxe da função TOTALDIASANO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR – Ano que deseja calcular os dias

**65.3. Exemplo**  
TOTALDIASANO('2012')

**66. TOTALDIASMES**  
Retorna o total de dias de um determinado mês de um ano.

**66.1. Contexto**  
Independente do contexto

**66.2. Sintaxe**  
TOTALDIASMES ( VALOR1, VALOR2 )  
A sintaxe da função TOTALDIASMES tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR1 – Mês que deseja calcular os dias
  + VALOR2 – Ano

**66.3. Exemplo**  
TOTALDIASMES('12','2012')

**67. TOTALPAGO**  
Retorna o valor total pago de um contrato.

**67.1. Contexto**  
Contrato de venda/aluguel

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**67.2. Sintaxe**  
TOTALPAGO ( VALOR1, VALOR2 )  
A sintaxe da função TOTALPAGO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR1 – Código da coligada
  + VALOR2 – Número da venda

**68. DATVCTO**  
Retorna a data de vencimento de uma parcela.

**68.1. Contexto**  
Reajuste contratual de venda/aluguel.

**SELECT \* FROM **XPARCELAPAGAMENTO**WHERE NUM\_VENDA = 1234**

**68.2. Sintaxe**  
DATVCTO

**69. UNIDADE**  
Retorna o código da unidade de um contrato.

**69.1. Contexto**  
Contrato de venda/aluguel e POC

**SELECT \* FROM XVENDA JOIN XITEMVENDA ON XVENDA.NUM\_VENDA = XITEMVENDA.NUM\_VENDA WHERE NUM\_VENDA = 1234**

**69.2. Sintaxe**  
UNIDADE

**70. SUBUNIDADE**  
Retorna o código da subunidade de um contrato.

**70.1. Contexto**  
Contrato de venda/aluguel e POC

**SELECT \* FROM XVENDA JOIN XITEMVENDA ON XVENDA.NUM\_VENDA = XITEMVENDA.NUM\_VENDA WHERE NUM\_VENDA = 1234**

**70.2. Sintaxe**  
SUBUNIDADE

**70. SUBUNIDADE**  
Retorna o código da subunidade de um contrato.

**70.1. Contexto**  
Contrato de venda/aluguel e POC

**SELECT \* FROM XVENDA JOIN XITEMVENDA ON XVENDA.NUM\_VENDA = XITEMVENDA.NUM\_VENDA WHERE NUM\_VENDA = 1234**

**70.2. Sintaxe**  
SUBUNIDADE

**71. NUMADIT**  
Retorna o código do aditivo do contrato.

**71.1. Contexto**  
Aditivo de venda/aluguel

**SELECT \* FROM XADIT WHERE NUMVENDA = 1234**

**71.2. Sintaxe**  
NUMADIT

**71. GETDIFERENCAVALORADITIVO**  
Retorna o código da subunidade de um contrato.

**71.1. Contexto**  
Aditivo de venda/aluguel

**SELECT \* FROM XADIT WHERE NUMVENDA = 1234**

**71.2. Sintaxe**  
GETDIFERENCAVALORADITIVO(NUMADIT)

A sintaxe da função GETDIFERENCAVALORADITIVO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento):

* + NUMADIT– NÚMERO DO ADITIVO.

**71. REXSALDODEVEDORAMORTIZADO**  
Retorna o saldo devedor amortizado teórico até o vencimento da parcela

**25.1. Contexto**  
Geração do reajuste em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**25.2. Sintaxe**  
REXGETSALDODEVEDORAMORTIZADO

**72. SALDODEVEDORAMORTIZADO**  
Retorna o saldo devedor amortizado do grupo da parcela

**25.1. Contexto**  
Geração do reajuste em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**25.2. Sintaxe**  
SALDODEVEDORAMORTIZADO

**73. GETVALORCMMENSAL**  
Retorna a Variação da Correção Monetária em memória  (Utiliza o índice moeda)

**48.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**48.2. Sintaxe**  
GETVALORCMMENSAL( STRING, DATA1, DATA2, VALOR1)  
A sintaxe da função GETVALORCMMENSAL tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING – Moeda
  + DATA1 – Data Inicial
  + DATA2 – Data Final
  + VALOR1 – Meses de defasagem
* EX. GETVALORCMMENSAL('IGPMI',ADICIONAMESES(DATREAJUSTE,-1),DATREAJUSTE,0);

**74. FORMATARESULTADO**  
Formata o valor para um tipo específico.

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1. Contexto**  
Independente do contexto

**2. Sintaxe**  
FORMATARESULTADO( object, string )  
A sintaxe da função tem os seguintes argumentos

* + object – Conteúdo a ser formatado
  + string–Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**3. Exemplo**

FORMATARESULTADO('01/01/2020','D');

**75. PRIMEIRODIAMES**  
Retorna a data no primeiro dia do mês.

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1. Contexto**  
Independente do contexto

**2. Sintaxe**  
PRIMEIRODIAMES( data )  
A sintaxe da função tem os seguintes argumentos

* + data– data a ser formatada

**3. Exemplo**

PRIMEIRODIAMES('11/01/2020');

**76. GETTABPARCELANUMPARCELA**  
Retorna o valor de um campo da tabela de parcela para um número da parcela dentro do grupo da venda do contexto

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1. Contexto**

contexto da parcela

**SELECT \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**2. Sintaxe**  
GETTABPARCELANUMPARCELA( parcela ,campo, string )  
A sintaxe da função tem os seguintes argumentos

* + parcela– número da parcela
  + campo– nome do ampo
  + string–Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**3. Exemplo**

GETTABPARCELANUMPARCELA(10, 'NUN\_VENDA', 'S');

**77. SETRESIDUODISTRIBUIDOLIMPA**  
Limpa os campos de código do grupo do resíduo e a data de distribuição do resíduo. Tabela XVendaParcela

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1. Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**2. Sintaxe**  
SETRESIDUODISTRIBUIDOLIMPA( parcela)  
A sintaxe da função tem os seguintes argumentos

* + parcela– número da parcela

**3. Exemplo**

SETRESIDUODISTRIBUIDOLIMPA(10);

**78. SETRESIDUODISTRIBUIDOMARCAR**  
Marca os campos de código do grupo do resíduo e a data de distribuição do resíduo com os dados do grupo do contexto da parcela e o período do reajuste.  Tabela XVendaParcela

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1. Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**2. Sintaxe**  
SETRESIDUODISTRIBUIDOMARCAR( parcela)  
A sintaxe da função tem os seguintes argumentos

* + parcela– número da parcela

**3. Exemplo**

SETRESIDUODISTRIBUIDOMARCAR(10);

**78. SETVALORRESIDUO**  
Armazena o valor calculado no campo Valor Resíduo. Tabela XVendaParcela

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1. Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**2. Sintaxe**  
SETVALORRESIDUO( valor)  
A sintaxe da função tem os seguintes argumentos

* + valor– valor do resíduo calculado

**3. Exemplo**

SETVALORRESIDUO(100.01);

**79. SETVALORRESIDUOCMANTES**  
Armazena o valor calculado no campo Valor Resíduo CM Antes da tabela XVendaParcela e sumariza esse valor no campo Valor Resíduo

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1. Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**2. Sintaxe**  
SETVALORRESIDUOCMANTES( valor)  
A sintaxe da função tem os seguintes argumentos

* + valor– valor do resíduo calculado

**3. Exemplo**

SETVALORRESIDUOCMANTES(100.01);

**80. SETVALORRESIDUOCMAPOS**  
Armazena o valor calculado no campo Valor Resíduo CM Após da tabela XVendaParcela e sumariza esse valor no campo Valor Resíduo

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1. Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**2. Sintaxe**  
SETVALORRESIDUOCMAPOS( valor)  
A sintaxe da função tem os seguintes argumentos

* + valor– valor do resíduo calculado

**3. Exemplo**

SETVALORRESIDUOCMAPOS(100.01);

**81. SETVALORRESIDUOJUROSANTES**  
Armazena o valor calculado no campo Valor Resíduo Juros Antes da tabela XVendaParcela e sumariza esse valor no campo Valor Resíduo

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1. Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**2. Sintaxe**  
SETVALORRESIDUOJUROSANTES( valor)  
A sintaxe da função tem os seguintes argumentos

* + valor– valor do resíduo calculado

**3. Exemplo**

SETVALORRESIDUOJUROSANTES(100.01);

**82. SETVALORRESIDUOJUROSAPOS**  
Armazena o valor calculado no campo Valor Resíduo Juros Após da tabela XVendaParcela e sumariza esse valor no campo Valor Resíduo

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**2.Sintaxe**  
SETVALORRESIDUOJUROSAPOS( valor)  
A sintaxe da função tem os seguintes argumentos

* + valor– valor do resíduo calculado

**3.Exemplo**

SETVALORRESIDUOJUROSAPOS(100.01);

**83. REAJUSTARCOMPONENTEREGRAPERIODOREAJUSTE**  
Retorna 1 para verdadeiro e 0 para false, caso o período do reajuste em relação a database e a data do reajsute é para reajustar Juros/CM

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELACOMPONENTE JOIN  XPARCELAPAGAMENTO  WHERE NUM\_VENDA = 1234 AND COD\_COMPN = 4**

**2.Sintaxe**  
REAJUSTARCOMPONENTEREGRAPERIODOR

**3.Exemplo**

SE REAJUSTARCOMPONENTEREGRAPERIODOR = 1 ENTAO ... FIMSE

**84. REAJUSTARCOMPONENTEREGRAVENCIMENTO**  
Retorna 1 para verdadeiro e 0 para false, caso o período do reajuste em relação ao vencimento é para reajustar Juros/CM.

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELACOMPONENTE JOIN  XPARCELAPAGAMENTO  WHERE NUM\_VENDA = 1234 AND COD\_COMPN = 4**

**2.Sintaxe**  
REAJUSTARCOMPONENTEREGRAVENCIMENTO

**3.Exemplo**

SE REAJUSTARCOMPONENTEREGRAVENCIMENTO= 1 ENTAO ... FIMSE

**85. GETSALDODEVEDORTEORICOREGRARESIDUO**  
Retorna o valor do saldo devedor téorico do componente principal do valor financiado da regra até o vencimento do contexto da parcela atual. Valor do Financiamento do grupo da parcela do contexto +(mais) valor sumarizado do campo Valor Resíduo somente da parcelas que tenham o vencimento até a data do reajuste - (menos) os valores sumarizados dos campos de valor original mais CM mais juros que tenham o vencimento até a data do reajuste.

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELACOMPONENTE JOIN  XPARCELAPAGAMENTO  WHERE NUM\_VENDA = 1234 AND COD\_COMPN = 4**

**2.Sintaxe**  
GETSALDODEVEDORTEORICOREGRARESIDUO

**3.Exemplo**

GETSALDODEVEDORTEORICOREGRARESIDUO

**86. GETSALDODEVEDORTEORICOVENDARESIDUO**  
Retorna o valor do saldo devedor téorico da venda até o vencimento do contexto da parcela atual. Valor do Financiamento do grupo da parcela do contexto +(mais) valor sumarizado do campo Valor Resíduo somente da parcelas que tenham o vencimento até a data do reajuste - (menos) os valores sumarizados dos campos de valor original mais CM mais juros que tenham o vencimento até a data do reajuste.

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELACOMPONENTE JOIN  XPARCELAPAGAMENTO  WHERE NUM\_VENDA = 1234 AND COD\_COMPN = 4**

**2.Sintaxe**  
GETSALDODEVEDORTEORICOVENDARESIDUO

**3.Exemplo**

GETSALDODEVEDORTEORICOVENDARESIDUO

**87. GETNUMPARCELAMESANIVERSARIOREAJUSTE**  
Retorna o numero da parcela que tenha o vencimento que fez aniversário no mesmo mês da data do reajuste.

Através desta parcela será definido o limite entre o período do reajuste anual anterior e o novo período.

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELACOMPONENTE JOIN  XPARCELAPAGAMENTO  WHERE NUM\_VENDA = 1234 AND COD\_COMPN = 4**

**2.Sintaxe**  
GETNUMPARCELAMESANIVERSARIOREAJUSTE

**3.Exemplo**

GETNUMPARCELAMESANIVERSARIOREAJUSTE

**88. GETNUMPARCELAPORDATAVENCIMENTO**  
Retorna o numero da parcela que tenha o vencimento que fez aniversário no mesmo mês da data do reajuste.

Através desta parcela será definido o limite entre o período do reajuste anual anterior e o novo período.

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELAPAGAMENTO  WHERE NUM\_VENDA = 1234**

**2.Sintaxe**  
GETNUMPARCELAPORDATAVENCIMENTO(Data, diaExato)

A sintaxe da função tem os seguintes argumentos

* + Data– data a ser pesquisada
  + diaExato - 1 - para pesquisar da data exata e 0 para pesquisar somente mês e ano da data

**3.Exemplo**

GETNUMPARCELAPORDATAVENCIMENTO('01/01/2020', 1)

**89. ADICIONADIASPRORATA**  
Adiciona número de dias Pro-Rata a uma data passada por parâmetro. Ou Seja, não deixa a data mudar de mês.

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto GERAL

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**2.Sintaxe**  
ADICIONADIASPRORATA(Data, dias)

A sintaxe da função tem os seguintes argumentos

* + Data– data base
  + dias -  número de dias que deseja adionar na data

**3.Exemplo**

ADICIONADIASPRORATA('01/01/2020', 10)

**90. DIADOCONTRATO**  
Retorna o dia do aniversário do contrato (Data da Venda)

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto da venda

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**2.Sintaxe**  
DIADOCONTRATO

**3.Exemplo**

DIADOCONTRATO

**91. DATACONTRATOREAJUSTE**  
Retorna a data do reajuste com base no dia do aniversário do contrato e a defasagem para Correção Monetária com moeda diária.

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELAPAGAMENTO  WHERE NUM\_VENDA = 1234**

**2.Sintaxe**  
DATACONTRATOREAJUSTE

**3.Exemplo**

DATACONTRATOREAJUSTE

**92. TABCOMISSOES**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\***

Retorna o valor de um campo da tabela de Comissões

**92.1. Contexto**  
Comissões

**SELECT \* FROM XCOMISSOES **(NOLOCK)**** **WHERE IDCOMISSAO= 1234**

**92.2. Sintaxe**

TABCOMISSOES( STRING1, STRING2 )  
A sintaxe da função TABCOMISSOES tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela de comissoes
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**92.3. Exemplo**  
TABCOMISSOES('IDCOMISSAO','I')

**93. TABCOMISSOESCOMPL**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\***  
Retorna o valor de um campo da tabela complementar de Comissões

**93.1. Contexto**Comissões Campos Complementares

**SELECT \* FROM XCOMISSOESCOMPL **(NOLOCK)******WHERE IDCOMISSAO= 1234**

**93.2. Sintaxe**

TABCOMISSOESCOMPL( STRING1, STRING2 )  
A sintaxe da função TABCOMISSOESCOMPL tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela complementar de comissoes
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**93.3. Exemplo**  
TABCOMISSOESCOMPL('IDCOMISSAO','I')

**94. TABCOMISSOESITEM**Retorna o valor de um campo da tabela de Comissões Item

**94.1. Contexto**  
Comissões Item

**SELECT \* FROM XCOMISSOESITEM **(NOLOCK)**** **WHERE IDCOMISSAO= 1234**

**94.2. Sintaxe**

TABCOMISSOESITEM( STRING1, STRING2 )  
A sintaxe da função TABCOMISSOESITEM tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela de comissoes item
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**94.3. Exemplo**  
TABCOMISSOESITEM('IDCOMISSAO','I')

**95. TABCOMISSOESITEMPARCELA**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\***Retorna o valor de um campo da tabela de Comissões Item Parcela

**95.1. Contexto**  
Comissões Item Parcela (Item = para quem vai o pagamento da comissão)

**SELECT \* FROM XCOMISSOESITEMPARCELA **(NOLOCK)******WHERE IDCOMISSAO= 1234 AND IDITEMCOMISSAO = 1234**

**95.2. Sintaxe**TABCOMISSOESITEMPARCELA( STRING1, STRING2 )  
A sintaxe da função TABCOMISSOESITEMPARCELA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela de comissoes item parcela
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**95.3. Exemplo**  
TABCOMISSOESITEMPARCELA('IDCOMISSAO','I')

**95. VALORTOTALCOMISSAO**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\***

Retorna o valor total da comissão gravada.

**95.1. Contexto**  
Comissões geradas

**SELECT \* FROM XCOMISSOES **(NOLOCK)******WHERE IDCOMISSAO= 1234**

**95.2. Sintaxe**VALORTOTALCOMISSAO 

**95.3. Exemplo**  
VALORTOTALCOMISSAO

**95. VALORSALDOCOMISSAO**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\***

Retorna o valor do saldo de comissão que ainda não teve o valor gerado em parcela, para geração de integração.

**95.1. Contexto**  
Comissões geradas

**SELECT \* FROM **XCOMISSOES** (NOLOCK)** **WHERE IDCOMISSAO= 1234**

**95.2. Sintaxe**VALORSALDOCOMISSAO

**95.3. Exemplo**  
VALORSALDOCOMISSAO

**95. PERCENTUALTOTALCOMISSAO**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\***

Retorna o percentual total da comissão, somatório de todos os percentuais encontrados correspondentes a cada parcela já gerada da comissão.

**95.1. Contexto**  
Comissões geradas

**SELECT \* FROM **XCOMISSOES** (NOLOCK)** **WHERE IDCOMISSAO= 1234**

**95.2. Sintaxe**PERCENTUALTOTALCOMISSAO

**95.3. Exemplo**  
PERCENTUALTOTALCOMISSAO

**96. QTDECOMISSIOANDOSCOMISSAO**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\***

Retorna a quantidade de comissionados da comissão.

**96.1. Contexto**  
Comissões geradas

**SELECT \* FROM **XCOMISSOES** (NOLOCK)** **WHERE IDCOMISSAO= 1234**

**96.2. Sintaxe**QTDECOMISSIOANDOSCOMISSAO

**96.3. Exemplo**  
QTDECOMISSIOANDOSCOMISSAO

**97. PERCENTUALCOMISSIONADO**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\***

Retorna o percentual do comissionado (empresa + cliente) da comissão

**97.1. Contexto**  
Comissões geradas

**SELECT \* FROM **XCOMISSOES** (NOLOCK)** **WHERE IDCOMISSAO= 1234**

**97.2. Sintaxe**PERCENTUALCOMISSIONADO

**97.3. Exemplo**  
PERCENTUALCOMISSIONADO

**98.0 VALORCOMISSIONADO**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\***

Retorna o valor do comissionado (empresa + cliente) da comissão

**98.1. Contexto**  
Comissões geradas

**SELECT \* FROM **XCOMISSOES** (NOLOCK) JOIN **XCOMISSOESITEM ON XCOMISSOES.IDCOMISSAO = XCOMISSOESITEM.IDCOMISSAO******WHERE **XCOMISSOES.**IDCOMISSAO= 1234**

**98.2. Sintaxe**VALORCOMISSIONADO

**98.3. Exemplo**  
VALORCOMISSIONADO

**98.1 SALDOCOMISSIONADO**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\* Somente versão 12.1.2310**

Retorna o saldo que falta gerar das parcelas do comissionado (empresa + cliente) da comissão

**98.1. Contexto**  
Comissões geradas

**SELECT \* FROM **XCOMISSOES** (NOLOCK) JOIN **XCOMISSOESITEM ON XCOMISSOES.IDCOMISSAO = XCOMISSOESITEM.IDCOMISSAO******WHERE **XCOMISSOES.**IDCOMISSAO= 1234**

**98.2. Sintaxe**SALDOCOMISSIONADO

**98.3. Exemplo**  
SALDOCOMISSIONADO

**99. VALORLIQUIDOPFTIN**  
Retorna o valor líquido do lançamento com origem no TOTVS Incorporação, calculado sob a mesma regra da Ficha Financeira do TOTVS Incorporação

**99.1 - Contexto**

A fórmula não depende de um contexto específico pois recebe todas as informações necessárias para o cálculo nos parâmetros

**99.2 - Sintaxe**  
VALORLIQUIDOPFTIN(COLIGADA, IDLAN, DATABASE)

* + COLIGADA e IDLAN indicam qual lançamento deve ter o valor líquido calculado
  + DATABASE - indica qual a data de referência para cálculo dos valores financeiros, como multa e juros

**100 VALORLIQUIDODESAGIOPFTIN**  
Retorna o valor líquido, com deságio, do lançamento com origem no TOTVS Incorporação, calculado sob a mesma regra da Ficha Financeira do TOTVS Incorporação

**100.1 - Contexto**

A fórmula não depende de um contexto específico pois recebe todas as informações necessárias para o cálculo nos parâmetros

**100.2 - Sintaxe**  
VALORLIQUIDODESAGIOPFTIN(COLIGADA, IDLAN, DATABASE)

* + COLIGADA e IDLAN indicam qual lançamento deve ter o valor líquido calculado
  + DATABASE - indica qual a data de referência para cálculo dos valores financeiros, como multa e juros

**101. GETVALORVENDASALDODEVEDORDATABASE**  
Retorna o valor líquido da venda de todos os lançamentos em aberto, calculado sob a mesma regra da Ficha Financeira do TOTVS Incorporação

**101.1 - Contexto**

A fórmula não depende de um contexto específico pois recebe todas as informações necessárias para o cálculo nos parâmetros

**101.2 - Sintaxe**  
GETVALORVENDASALDODEVEDORDATABASE(DATABASE)

* + DATABASE - indica qual a data de referência para cálculo dos valores financeiros, como multa e juros

**102. GETVALORVENDASALDODEVEDORDATABASE**  
Retorna o valor líquido, com deságio,  da venda de todos os lançamentos em aberto, calculado sob a mesma regra da Ficha Financeira do TOTVS Incorporação

**102.1 - Contexto**

A fórmula não depende de um contexto específico pois recebe todas as informações necessárias para o cálculo nos parâmetros

**102.2 - Sintaxe**  
GETVALORVENDASALDODEVEDORDATABASE(DATABASE)

* + DATABASE - indica qual a data de referência para cálculo dos valores financeiros, como multa e juros

**103. COMISSAOMETAVALOR**  
Retorna o valor de todas as vendas no mês da comissão. Primeiro argumento o tipo de cálculo da meta da comissão nome do campo.

**103.1 - Contexto**

Usa como contexto a chave da tabela "XCOMISSOESITEM".

**103.2 - Sintaxe**  
COMISSAOMETAVALOR(TipoComissaoCalculoMeta)

* + TipoComissaoCalculoMeta- (0 = Todas as Coligadas;   1 = Coligada da Comissão; 2 = Empreendimento da Comissão; 3 = Meta da Comissão)

**104. COMISSAOMETAQTD**  
Retorna a quantidade de todas as vendas no mês da comissão. Primeiro argumento o tipo de cálculo da meta da comissão nome do campo.

**104.1- Contexto**

Usa como contexto a chave da tabela "XCOMISSOESITEM".

**104.2 - Sintaxe**  
COMISSAOMETAQTD(TipoComissaoCalculoMeta)

* + TipoComissaoCalculoMeta- (0 = Todas as Coligadas;   1 = Coligada da Comissão; 2 = Empreendimento da Comissão; 3 = Meta da Comissão)

**1. CONDVENDA**  
Busca informações da condição da venda

**2.1. Contexto**   
Contrato de venda/aluguel

****SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234****

**2.2. Sintaxe**  
CONDVENDA ( VALOR1, VALOR2, STRING1, STRING2 )  
A sintaxe da função CONDVENDA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR1 – Código do grupo
  + VALOR2 – Código do componente
  + STRING1 – Nome do campo da tabela de regra da venda
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**2.3. Exemplo**  
CODVENDA(1,1,'QTD\_PARC','I')

**3. CONTEXTO**  
Tabela de Contexto do Reajuste Mensal

**3.1. Contexto**  
Reajuste contratual de venda/aluguel

**3.2. Sintaxe**  
CONTEXTO ( STRING )  
A sintaxe da função CONTEXTO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING – Nome do campo da tabela carregada no contexto

**4. CUSTOINCORRIDO**  
Busca o valor do custo incorrido

**4.1. Contexto**  
Apuração de resultado contábil pelo POC (Resolução 963)

**4.2. Sintaxe**  
CUSTOINCORRIDO ( VALOR1, VALOR2, VALOR3, VALOR4, DATA, STRING ).

A sintaxe da função CUSTOINCORRIDO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR1 – Código da coligada
  + VALOR2 – Código do projeto
  + VALOR3 – Código da obra
  + VALOR4 – Código da etapa
  + DATA – Data da apuração
  + STRING – Código do usuário

**5. CUSTOORCADO**  
Busca o valor do custo orçado

**5.1. Contexto**  
Apuração de resultado contábil pelo POC (Resolução 963)

**5.2. Sintaxe**  
CUSTOORCADO ( VALOR1, VALOR2, VALOR3, VALOR4, DATA, STRING ).  
A sintaxe da função CUSTOORCADO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR1 – Código da coligada
  + VALOR2 – Código do projeto
  + VALOR3 – Código da obra
  + VALOR4 – Código da etapa
  + DATA – Data da apuração
  + STRING – Código do usuário

**6. CUSTOORCADOREMANESCENTE**  
Busca o valor do custo orçado remanescente

**6.1. Contexto**  
Apuração de resultado contábil pelo POC (Resolução 963)

**6.2. Sintaxe**  
CUSTOORCADOREMANESCENTE ( VALOR1, VALOR2, VALOR3, VALOR4, DATA, STRING)  
A sintaxe da função CUSTOORCADOREMANESCENTE tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR1 – Código da coligada
  + VALOR2 – Código do projeto
  + VALOR3 – Código da obra
  + VALOR4 – Código da etapa
  + DATA – Data da apuração
  + STRING – Código do usuário

**7. DATBASE**  
Retorna a data base do componente

**7.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**7.2. Sintaxe**  
DATBASE

**8. DATREAJUSTE**  
Retorna a data do Reajuste da Parcela

**8.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**8.2. Sintaxe**  
DATREAJUSTE

**9. EXTENSODATA**  
Retorna uma data por extenso

**9.1. Contexto**  
Independente do contexto

**9.2. Sintaxe**  
EXTENSODATA ( DATA )  
A sintaxe da função EXTENSODATA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + DATA – Data a ser retorna por extenso

**9.3. Exemplo**  
EXTENSODATA('20/03/2010')

**10. TABSECURITIZACAO**  
Retorna o valor de um campo da tabela de Securitização

**10.1. Contexto**  
Securitização

**SELECT \* FROM XSECURITIZACAO** **WHERE ID= 1234**

**10.2. Sintaxe**

TABSECURITIZACAO( STRING1, STRING2 )  
A sintaxe da função TABSECURITIZACAO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela de venda
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**10.3. Exemplo**  
TABSECURITIZACAO('ID','I')

**11. TABSECURITIZACAOCOMPL**  
Retorna o valor de um campo da tabela complementar de Securitização

**11.1. Contexto**

Securitização

**SELECT \* FROM XSECURITIZACAOCOMPL****WHERE ID= 1234**

**11.2. Sintaxe**

TABSECURITIZACAOCOMPL( STRING1, STRING2 )  
A sintaxe da função TABSECURITIZACAOCOMPL tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela de venda
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**11.3. Exemplo**  
TABSECURITIZACAOCOMPL('ID','I')

**12. EXTENSONUMERO**  
Retorna um número por extenso

**12.1. Contexto**  
Independente do contexto

**12.2. Sintaxe**  
EXTENSONUMERO ( VALOR )  
A sintaxe da função EXTENSONUMERO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR – Número a ser retornado por extenso

**12.3. Exemplo**  
EXTENSONUMERO(1453)

**13. EXTENSOVALOR**  
Retorna um valor por extenso

**13.1. Contexto**  
Independente do contexto

**13.2. Sintaxe**  
EXTENSOVALOR ( VALOR )  
A sintaxe da função EXTENSOVALOR tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR – Valor a ser retornado por extenso

**13.3. Exemplo**  
EXTENSOVALOR(156.14)

**14. FORMATANUMERO**  
Retorna um número formatado em inteiro

**14.1. Contexto**  
Independente do contexto

**14.2. Sintaxe**  
FORMATANUMERO ( VALOR )  
A sintaxe da função FORMATANUMERO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR – Valor a ser formatado para o padrão inteiro

**14.3. Exemplo**  
FORMATANUMERO(156.14)

**15. FORMATAVALOR**  
Retorna um valor formatado em moeda

**15.1. Contexto**  
Independente do contexto

**15.2. Sintaxe**  
FORMATAVALOR ( VALOR )  
A sintaxe da função FORMATAVALOR tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR – Valor a ser formatado para o padrão moeda

**15.3. Exemplo**  
FORMATAVALOR(152.6)

**16. GPCODCOMPN**  
Retorna o código do componente de Juros ou CM

**16.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**16.2. Sintaxe**  
GPCODCOMPN

**17. GPCODCOMPNPRINCIPAL**  
Retorna o código do componente principal

**17.1. Contexto**  
Geração do plano de financiamento

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**17.2. Sintaxe**  
GPCODCOMPNPRINCIPAL

**18. GPCODGRUPO**  
Retorna o código do grupo

**18.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**18.2. Sintaxe**  
GPCODGRUPO

**19. GPCODTIPOCOMPN**  
Retorna o código do tipo de Componente dos Juros ou CM

**19.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**19.2. Sintaxe**  
GPCODTIPOCOMPN

**20. GPCODTIPOPARC**  
Retorna o código do tipo da parcela

**20.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**20.2. Sintaxe**  
GPCODTIPOPARC

**22. GPGETDATABASE**  
Retorna a data de referência de reajuste (Data de início do componente)

**22.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**22.2. Sintaxe**  
GPGETDATABASE

**23. GPGETDATAENTREGA**  
Retorna a data de entrega do empreendimento

**23.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**23.2. Sintaxe**  
GPGETDATAENTREGA

**24. GPGETPERIODOMESES**  
Retorna o Período em meses da data base até o vencimento da parcela

**24.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**24.2. Sintaxe**  
GPGETPERIODOMESES

**25. GPGETSALDODEVEDORAMORTIZADO**  
Retorna o saldo devedor amortizado até o vencimento da parcela

**25.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**25.2. Sintaxe**  
GPGETSALDODEVEDORAMORTIZADO

**26. GPNUMPARC**  
Retorna o número da parcela

**26.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**26.2. Sintaxe**  
GPNUMPARC

**27. GPNUMVENDA**  
Retorna o número da venda

**27.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**27.2. Sintaxe**  
GPNUMVENDA

**29. GPXPARCELAPAGAMENTO**  
Acessa os campos da parcela

**29.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM **XPARCELAPAGAMENTO**WHERE NUM\_VENDA = 1234**

**29.2. Sintaxe**  
GPXPARCELAPAGAMENTO ( STRING )  
A sintaxe da função GPXPARCELAPAGAMENTO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING – Campo que se deseja ter acesso da parcela

**30. GPXREGRACOMPONENTEVENDA**  
Acesso aos campos da Regra no Grupo

**30.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XREGRACOMPONENTEVENDA WHERE NUM\_VENDA = 1234**

**30.2. Sintaxe**  
GPXREGRACOMPONENTEVENDA ( STRING )  
A sintaxe da função GPXREGRACOMPONENTEVENDA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING - Campo que se deseja ter acesso da regra no grupo

**31. GPXREGRACOMPONENTEVENDAPRINCIPAL**  
Acesso aos campos da Regra Principal

**31.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**31.2. Sintaxe**  
GPXREGRACOMPONENTEVENDAPRINCIPAL ( STRING )  
A sintaxe da função GPXREGRACOMPONENTEVENDAPRINCIPAL tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING - Campo que se deseja ter acesso da regra principal

**32. GPXVENDA**  
Acesso aos campos da venda

**32.1. Contexto**  
Geração do plano de financiamento em memória (sem acesso a banco de dados)

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**32.2. Sintaxe**  
GPXVENDA ( STRING )  
A sintaxe da função GPXVENDA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING - Campo que se deseja ter acesso da venda

**33. JUROSMORA**  
Retorna o valor de juros de mora por atraso, de todas as parcelas em aberto ou parcialmente quitadas, vencidas de um contrato.

**33.1. Contexto**  
Contrato de venda/aluguel

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**33.2. Sintaxe**  
JUROSMORA ( VALOR1, VALOR2, DATA, STRING )  
A sintaxe da função JUROSMORA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR1 – Código da coligada
  + VALOR2 – Número da venda
  + DATA – Data referência
  + STRING – Código do usuário

**33.3. Exemplo**  
JUROSMORA(1,1,'24/06/2001','mestre')

**34. MULTA**  
Retorna o valor de multa por atraso, de todas as parcelas em aberto ou parcialmente quitadas, vencidas de um contrato.

**34.1. Contexto**  
Contrato de venda/aluguel

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**34.2. Sintaxe**  
MULTA ( VALOR1, VALOR2, DATA, STRING )  
A sintaxe da função MULTA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR1 – Código da coligada
  + VALOR2 – Número da venda
  + DATA – Data referência
  + STRING – Código do usuário

**34.3. Exemplo**  
MULTA(1,3,'24/06/2001','mestre')

**35. NUMPARC**  
Retorna o número de uma parcela.

**35.1. Contexto**  
Reajuste contratual de venda/aluguel.

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**35.2. Sintaxe**  
NUMPARC

**36. NUMVENDA**  
Retorna o número de uma venda/aluguel.

**36.1. Contexto**  
Reajuste contratual de venda/aluguel.

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**36.2. Sintaxe**  
NUMVENDA

**37. CODGRUPO**  
Retorna o código de um grupo.

**37.1. Contexto**  
Reajuste contratual de venda/aluguel.

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**37.2. Sintaxe**  
CODGRUPO

**38. CODCOMPN**  
Retorna o código do componente de reajuste

**38.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**38.2. Sintaxe**  
CODCOMPN

**39. CODTIPOCOMPN**  
Retorna o código do tipo do componente de reajuste

**39.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**39.2. Sintaxe**  
CODTIPOCOMPN

**40. CODTIPOPARC**  
Retorna o código do tipo de uma parcela

**40.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**40.2. Sintaxe**  
CODTIPOPARC

**41. PERIODOANUAL**  
Retorna o período anual entre a data base até o vencimento da parcela retornando a diferença de anos.

**41.1. Contexto**  
Reajuste contratual de venda/aluguel.

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**41.2. Sintaxe**  
PERIODOANUAL

**42. PERIODOMENSAL**  
Retorna o período mensal entre a data base até o vencimento da parcela retornando a diferença de meses.

**42.1. Contexto**  
Reajuste contratual de venda/aluguel.

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**42.2. Sintaxe**  
PERIODOMENSAL

**43. DIFERENCADIAS**  
Retorna a Diferença de dias entre duas datas

**43.1. Contexto**  
Independente do contexto

**43.2. Sintaxe**  
DIFERENCADIAS ( DATA1, DATA2 )  
A sintaxe da função DIFERENCADIAS tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + DATA1 – Primeira Data
  + DATA2 – Segunda Data

**43.3. Exemplo**  
DIFERENCADIAS('10/03/2012','10/02/2012')

**44. DIFERENCAMESES**  
Retorna a Diferença de meses entre duas datas

**44.1. Contexto**  
Independente do contexto

**44.2. Sintaxe**  
DIFERENCAMESES ( DATA1, DATA2 )  
A sintaxe da função DIFERENCAMESES tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + DATA1 – Primeira Data
  + DATA2 – Segunda Data

**44.3. Exemplo**  
DIFERENCAMESES('10/03/2012','10/02/2012')

**45. ADICIONADIAS**  
Adiciona Dias a uma Data

**45.1. Contexto**  
Independente do contexto

**45.2. Sintaxe**  
ADICIONADIAS ( STRING, DATA1, DATA2, DATA3, VALOR1, VALOR2 )  
A sintaxe da função ADICIONADIAS tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + DATA – Data para adicionar dias
  + DIAS – Dias a ser adicionado a uma data

**45.3. Exemplo**  
ADICIONADIAS('10/03/2012',10)

**46. ADICIONAMESES**  
Adiciona Meses a uma Data

**46.1. Contexto**  
Independente do contexto

**46.2. Sintaxe**  
ADICIONAMESES ( DATA, MESES)  
A sintaxe da função ADICIONAMESES tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + DATA – Data para adicionar dias
  + MESES – Meses a ser adicionado a uma data

**46.3. Exemplo**  
ADICIONAMESES('10/03/2012',10)

**47. ADICIONAANOS**  
Adiciona Anos a uma Data

**47.1. Contexto**  
Independente do contexto

**47.2. Sintaxe**  
ADICIONAANOS ( DATA, ANOS )  
A sintaxe da função ADICIONAANOS tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* DATA – Data para adicionar anos
* ANOS – Anos a ser adicionado a uma data

**47.3. Exemplo**  
ADICIONAANOS('10/03/2012',10)

**48. RECALCULACORRECAOMONETARIA**  
Calcula a Variação da Correção Monetária em memória  (Utiliza o índice acumulado)

**48.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**48.2. Sintaxe**  
RECALCULACORRECAOMONETARIA ( STRING, DATA1, DATA2, DATA3, VALOR1, VALOR2 )  
A sintaxe da função RECALCULACORRECAOMONETARIA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING – Moeda
  + DATA1 – Data Inicial
  + DATA2 – Data Final
  + DATA3 – Data de vencimento da parcela
  + VALOR1 – Periodicidade
  + VALOR2 – Meses de defasagem

**49. REXPARCELACOMPONENTE**  
Retorna o valor de um campo de uma parcela do componente em memória (sem acesso ao banco de dados)

**49.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**49.2. Sintaxe**  
REXPARCELACOMPONENTE ( VALOR, STRING )  
A sintaxe da função REXPARCELACOMPONENTE tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* VALOR – Código do componente
* STRING - Campo que se deseja ter acesso da parcela

**50. REXPARCELAPAGAMENTO**  
Retorna o valor de um campo de uma parcela de pagamento em memória (sem acesso ao banco de dados)

**50.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XPARCELACOMPONENTE WHERE NUM\_VENDA = 1234**

**50.2. Sintaxe**  
REXPARCELAPAGAMENTO ( STRING )  
A sintaxe da função REXPARCELAPAGAMENTO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* STRING - Campo que se deseja ter acesso da parcela

**51. REXREGRACOMPONENTEVENDA**  
Acesso aos campos da Regra no Grupo em memória (sem acesso ao banco de dados)

**51.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM **XREGRACOMPONENTEVENDA**WHERE NUM\_VENDA = 1234**

**51.2. Sintaxe**  
REXREGRACOMPONENTEVENDA ( VALOR, STRING )  
A sintaxe da função REXREGRACOMPONENTEVENDA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* VALOR – Código do componente
* STRING – Campo que se deseja ter acesso da regra no grupo

**52. REXVENDA**  
Acesso aos campos da venda em memória (sem acesso ao banco de dados)

**52.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**52.2. Sintaxe**  
REXVENDA ( STRING )  
A sintaxe da função REXVENDA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING – Campo que se deseja ter acesso da venda

**53. SALDONEGATIVOVENDA**  
Retorna o saldo negativo de uma venda.

**53.1. Contexto**  
Contrato de Venda/Aluguel

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**53.2. Sintaxe**  
SALDONEGATIVOVENDA ( VALOR )  
A sintaxe da função SALDONEGATIVOVENDA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* VALOR – Número da venda

**53.3. Exemplo**  
SALDONEGATIVOVENDA(1)

**54. SOMATIPOCOMPN**  
Soma o valor de um tipo de componente

**54.1. Contexto**  
Contrato de Venda/Aluguel

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**54.2. Sintaxe**  
SOMATIPOCOMPN ( STRING1, STRING2 )  
A sintaxe da função SOMATIPOCOMPN tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* STRING1 – Tipo do componente
* STRING2 – Situação da parcela

**54.3. Exemplo**  
SOMATIPOCOMPN('1','2')

**55. SOMATIPOPARCELA**  
Soma o valor de um tipo de parcela

**55.1. Contexto**  
Contrato de Venda/Aluguel

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**55.2. Sintaxe**  
SOMATIPOPARCELA ( STRING1, STRING2 )  
A sintaxe da função SOMATIPOPARCELA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* STRING1 – Tipo de parcela
* STRING2 – Situação da parcela

**55.3. Exemplo**  
SOMATIPOPARCELA('2','2')

**56. TABCOMISSAO**  
Retorna o valor de um campo qualquer da tabela de comissão (XCOMISSAO)

**56.1. Contexto**  
Contrato de venda/aluguel

**56.2. Sintaxe**  
TABCOMISSAO ( STRING1, STRING2 )  
A sintaxe da função TABCOMISSAO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela comissão
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**56.3. Exemplo**  
TABCOMISSAO('NUMVENDA','I')

**57. TABCOMISSAOPARCELA**  
Retorna o valor de um campo qualquer da tabela de comissão (XCOMISSAOPARCELAMENTO)

**57.1. Contexto**  
Contrato de venda/aluguel

**57.2. Sintaxe**  
TABCOMISSAOPARCELA( STRING1, STRING2 )  
A sintaxe da função TABCOMISSAOPARCELA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela comissão
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**57.3. Exemplo**  
TABCOMISSAOPARCELA('NUMVENDA','I')

**58. TABCOMISSAOCOMPL**  
Retorna o valor de um campo qualquer da tabela de campo complementar de comissão (XCOMISSAOCOMPL)

**58.1. Contexto**  
Contrato de venda/aluguel

**58.2. Sintaxe**  
TABCOMISSAOCOMPL ( STRING1, STRING2 )  
A sintaxe da função TABCOMISSAOCOMPL tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* STRING1 – Nome do campo da tabela de campo complementar de comissão
* STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**58.3. Exemplo**  
TABCOMISSAOCOMPL('CODCOMISSAO','V')

**59. TABDISTRATO**  
Retorna o valor de um campo qualquer da tabela de distrato (XDISTRATO).

**59.1. Contexto**  
Contrato de venda/aluguel

**59.2. Sintaxe**  
TABDISTRATO ( STRING1, STRING2 )  
A sintaxe da função TABDISTRATO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* STRING1 – Nome do campo da tabela de distrato
* STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**59.3. Exemplo**  
TABDISTRATO('NUMVENDA','I')

**60. TABDISTRATOCOMPL**  
Retorna o valor de um campo qualquer da tabela de campo complementar de distrato (XDISTRATOCOMPL).

**60.1. Contexto**  
Contrato de venda/aluguel

**60.2. Sintaxe**  
TABDISTRATOCOMPL ( STRING1, STRING2 )  
A sintaxe da função TABDISTRATOCOMPL tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* STRING1 – Nome do campo da tabela de campo complementar de distrato
* STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**60.3. Exemplo**  
TABDISTRATOCOMPL('NUMVENDA','I')

**61. TABITEMVENDA**  
Retorna o valor de um campo qualquer da tabela de item da venda (XITEMVENDA).

**61.1. Contexto**  
Contrato de venda/aluguel

**61.2. Sintaxe**  
TABITEMVENDA ( STRING1, STRING2 )  
A sintaxe da função TABITEMVENDA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela de item de venda
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**61.3. Exemplo**  
TABITEMVENDA('VR\_ITEM','V')

**62. TABREGRA**  
Retorna o valor de um campo qualquer da tabela de regras da venda/aluguel (XREGRACOMPONENTEVENDA).

**62.1. Contexto**  
Regra da Venda/Aluguel.

**SELECT \* FROM XREGRACOMPONENTEVENDA WHERE NUM\_VENDA = 1234**

**62.2. Sintaxe**  
TABREGRA ( STRING1, STRING2 )  
A sintaxe da função TABREGRA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela de regra da venda
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**62.3. Exemplo**  
TABREGRA('COD\_TIPO\_PER','S')

**63. CODEMPREENDIMENTO**  
Retorna o código do empreendimento da venda.

**63.1. Contexto**

Contrato de venda/aluguel e POC

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**63.2. Sintaxe**  
CODEMPREENDIMENTO

**64. TABVENDA**  
Retorna o valor de um campo qualquer da tabela de venda (XVENDA).

**64.1. Contexto**  
Contrato de venda/aluguel

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**64.2. Sintaxe**  
TABVENDA ( STRING1, STRING2 )  
A sintaxe da função TABVENDA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela de venda
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**64.3. Exemplo**  
TABVENDA('DAT\_VENDA','D')

**65. TOTALDIASANO**  
Retorna o total de dias de um determinado ano.

**65.1. Contexto**  
Independente do contexto

**65.2. Sintaxe**  
TOTALDIASANO ( VALOR )  
A sintaxe da função TOTALDIASANO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR – Ano que deseja calcular os dias

**65.3. Exemplo**  
TOTALDIASANO('2012')

**66. TOTALDIASMES**  
Retorna o total de dias de um determinado mês de um ano.

**66.1. Contexto**  
Independente do contexto

**66.2. Sintaxe**  
TOTALDIASMES ( VALOR1, VALOR2 )  
A sintaxe da função TOTALDIASMES tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR1 – Mês que deseja calcular os dias
  + VALOR2 – Ano

**66.3. Exemplo**  
TOTALDIASMES('12','2012')

**67. TOTALPAGO**  
Retorna o valor total pago de um contrato.

**67.1. Contexto**  
Contrato de venda/aluguel

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**67.2. Sintaxe**  
TOTALPAGO ( VALOR1, VALOR2 )  
A sintaxe da função TOTALPAGO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + VALOR1 – Código da coligada
  + VALOR2 – Número da venda

**68. DATVCTO**  
Retorna a data de vencimento de uma parcela.

**68.1. Contexto**  
Reajuste contratual de venda/aluguel.

**SELECT \* FROM **XPARCELAPAGAMENTO**WHERE NUM\_VENDA = 1234**

**68.2. Sintaxe**  
DATVCTO

**69. UNIDADE**  
Retorna o código da unidade de um contrato.

**69.1. Contexto**  
Contrato de venda/aluguel e POC

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**69.2. Sintaxe**  
UNIDADE

**70. SUBUNIDADE**  
Retorna o código da subunidade de um contrato.

**70.1. Contexto**  
Contrato de venda/aluguel e POC

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**70.2. Sintaxe**  
SUBUNIDADE

**70. SUBUNIDADE**  
Retorna o código da subunidade de um contrato.

**70.1. Contexto**  
Contrato de venda/aluguel e POC

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**70.2. Sintaxe**  
SUBUNIDADE

**71. NUMADIT**  
Retorna o código do aditivo do contrato.

**71.1. Contexto**  
Aditivo de venda/aluguel

**SELECT \* FROM XADIT WHERE NUMVENDA = 1234**

**71.2. Sintaxe**  
NUMADIT

**71. GETDIFERENCAVALORADITIVO**  
Retorna o código da subunidade de um contrato.

**71.1. Contexto**  
Aditivo de venda/aluguel

**SELECT \* FROM XADIT WHERE NUMVENDA = 1234**

**71.2. Sintaxe**  
GETDIFERENCAVALORADITIVO(NUMADIT)

A sintaxe da função GETDIFERENCAVALORADITIVO tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento):

* + NUMADIT– NÚMERO DO ADITIVO.

**71. REXSALDODEVEDORAMORTIZADO**  
Retorna o saldo devedor amortizado teórico até o vencimento da parcela

**25.1. Contexto**  
Geração do reajuste em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**25.2. Sintaxe**  
REXGETSALDODEVEDORAMORTIZADO

**72. SALDODEVEDORAMORTIZADO**  
Retorna o saldo devedor amortizado do grupo da parcela

**25.1. Contexto**  
Geração do reajuste em memória (sem acesso a banco de dados)

**SELECT \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**25.2. Sintaxe**  
SALDODEVEDORAMORTIZADO

**73. GETVALORCMMENSAL**  
Retorna a Variação da Correção Monetária em memória  (Utiliza o índice moeda)

**48.1. Contexto**  
Reajuste contratual de venda/aluguel

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**48.2. Sintaxe**  
GETVALORCMMENSAL( STRING, DATA1, DATA2, VALOR1)  
A sintaxe da função GETVALORCMMENSAL tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING – Moeda
  + DATA1 – Data Inicial
  + DATA2 – Data Final
  + VALOR1 – Meses de defasagem
* EX. GETVALORCMMENSAL('IGPMI',ADICIONAMESES(DATREAJUSTE,-1),DATREAJUSTE,0);

**74. FORMATARESULTADO**  
Formata o valor para um tipo específico.

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1. Contexto**  
Independente do contexto

**2. Sintaxe**  
FORMATARESULTADO( object, string )  
A sintaxe da função tem os seguintes argumentos

* + object – Conteúdo a ser formatado
  + string–Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**3. Exemplo**

FORMATARESULTADO('01/01/2020','D');

**75. PRIMEIRODIAMES**  
Retorna a data no primeiro dia do mês.

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1. Contexto**  
Independente do contexto

**2. Sintaxe**  
PRIMEIRODIAMES( data )  
A sintaxe da função tem os seguintes argumentos

* + data– data a ser formatada

**3. Exemplo**

PRIMEIRODIAMES('11/01/2020');

**76. GETTABPARCELANUMPARCELA**  
Retorna o valor de um campo da tabela de parcela para um número da parcela dentro do grupo da venda do contexto

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1. Contexto**

contexto da parcela

**SELECT \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**2. Sintaxe**  
GETTABPARCELANUMPARCELA( parcela ,campo, string )  
A sintaxe da função tem os seguintes argumentos

* + parcela– número da parcela
  + campo– nome do ampo
  + string–Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**3. Exemplo**

GETTABPARCELANUMPARCELA(10, 'NUN\_VENDA', 'S');

**77. SETRESIDUODISTRIBUIDOLIMPA**  
Limpa os campos de código do grupo do resíduo e a data de distribuição do resíduo. Tabela XVendaParcela

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1. Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**2. Sintaxe**  
SETRESIDUODISTRIBUIDOLIMPA( parcela)  
A sintaxe da função tem os seguintes argumentos

* + parcela– número da parcela

**3. Exemplo**

SETRESIDUODISTRIBUIDOLIMPA(10);

**78. SETRESIDUODISTRIBUIDOMARCAR**  
Marca os campos de código do grupo do resíduo e a data de distribuição do resíduo com os dados do grupo do contexto da parcela e o período do reajuste.  Tabela XVendaParcela

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1. Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**2. Sintaxe**  
SETRESIDUODISTRIBUIDOMARCAR( parcela)  
A sintaxe da função tem os seguintes argumentos

* + parcela– número da parcela

**3. Exemplo**

SETRESIDUODISTRIBUIDOMARCAR(10);

**78. SETVALORRESIDUO**  
Armazena o valor calculado no campo Valor Resíduo. Tabela XVendaParcela

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1. Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**2. Sintaxe**  
SETVALORRESIDUO( valor)  
A sintaxe da função tem os seguintes argumentos

* + valor– valor do resíduo calculado

**3. Exemplo**

SETVALORRESIDUO(100.01);

**79. SETVALORRESIDUOCMANTES**  
Armazena o valor calculado no campo Valor Resíduo CM Antes da tabela XVendaParcela e sumariza esse valor no campo Valor Resíduo

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1. Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**2. Sintaxe**  
SETVALORRESIDUOCMANTES( valor)  
A sintaxe da função tem os seguintes argumentos

* + valor– valor do resíduo calculado

**3. Exemplo**

SETVALORRESIDUOCMANTES(100.01);

**80. SETVALORRESIDUOCMAPOS**  
Armazena o valor calculado no campo Valor Resíduo CM Após da tabela XVendaParcela e sumariza esse valor no campo Valor Resíduo

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1. Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**2. Sintaxe**  
SETVALORRESIDUOCMAPOS( valor)  
A sintaxe da função tem os seguintes argumentos

* + valor– valor do resíduo calculado

**3. Exemplo**

SETVALORRESIDUOCMAPOS(100.01);

**81. SETVALORRESIDUOJUROSANTES**  
Armazena o valor calculado no campo Valor Resíduo Juros Antes da tabela XVendaParcela e sumariza esse valor no campo Valor Resíduo

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1. Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**2. Sintaxe**  
SETVALORRESIDUOJUROSANTES( valor)  
A sintaxe da função tem os seguintes argumentos

* + valor– valor do resíduo calculado

**3. Exemplo**

SETVALORRESIDUOJUROSANTES(100.01);

**82. SETVALORRESIDUOJUROSAPOS**  
Armazena o valor calculado no campo Valor Resíduo Juros Após da tabela XVendaParcela e sumariza esse valor no campo Valor Resíduo

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELAPAGAMENTO WHERE NUM\_VENDA = 1234**

**2.Sintaxe**  
SETVALORRESIDUOJUROSAPOS( valor)  
A sintaxe da função tem os seguintes argumentos

* + valor– valor do resíduo calculado

**3.Exemplo**

SETVALORRESIDUOJUROSAPOS(100.01);

**83. REAJUSTARCOMPONENTEREGRAPERIODOREAJUSTE**  
Retorna 1 para verdadeiro e 0 para false, caso o período do reajuste em relação a database e a data do reajsute é para reajustar Juros/CM

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELACOMPONENTE JOIN  XPARCELAPAGAMENTO  WHERE NUM\_VENDA = 1234 AND COD\_COMPN = 4**

**2.Sintaxe**  
REAJUSTARCOMPONENTEREGRAPERIODOR

**3.Exemplo**

SE REAJUSTARCOMPONENTEREGRAPERIODOR = 1 ENTAO ... FIMSE

**84. REAJUSTARCOMPONENTEREGRAVENCIMENTO**  
Retorna 1 para verdadeiro e 0 para false, caso o período do reajuste em relação ao vencimento é para reajustar Juros/CM.

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELACOMPONENTE JOIN  XPARCELAPAGAMENTO  WHERE NUM\_VENDA = 1234 AND COD\_COMPN = 4**

**2.Sintaxe**  
REAJUSTARCOMPONENTEREGRAVENCIMENTO

**3.Exemplo**

SE REAJUSTARCOMPONENTEREGRAVENCIMENTO= 1 ENTAO ... FIMSE

**85. GETSALDODEVEDORTEORICOREGRARESIDUO**  
Retorna o valor do saldo devedor téorico do componente principal do valor financiado da regra até o vencimento do contexto da parcela atual. Valor do Financiamento do grupo da parcela do contexto +(mais) valor sumarizado do campo Valor Resíduo somente da parcelas que tenham o vencimento até a data do reajuste - (menos) os valores sumarizados dos campos de valor original mais CM mais juros que tenham o vencimento até a data do reajuste.

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELACOMPONENTE JOIN  XPARCELAPAGAMENTO  WHERE NUM\_VENDA = 1234 AND COD\_COMPN = 4**

**2.Sintaxe**  
GETSALDODEVEDORTEORICOREGRARESIDUO

**3.Exemplo**

GETSALDODEVEDORTEORICOREGRARESIDUO

**86. GETSALDODEVEDORTEORICOVENDARESIDUO**  
Retorna o valor do saldo devedor téorico da venda até o vencimento do contexto da parcela atual. Valor do Financiamento do grupo da parcela do contexto +(mais) valor sumarizado do campo Valor Resíduo somente da parcelas que tenham o vencimento até a data do reajuste - (menos) os valores sumarizados dos campos de valor original mais CM mais juros que tenham o vencimento até a data do reajuste.

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELACOMPONENTE JOIN  XPARCELAPAGAMENTO  WHERE NUM\_VENDA = 1234 AND COD\_COMPN = 4**

**2.Sintaxe**  
GETSALDODEVEDORTEORICOVENDARESIDUO

**3.Exemplo**

GETSALDODEVEDORTEORICOVENDARESIDUO

**87. GETNUMPARCELAMESANIVERSARIOREAJUSTE**  
Retorna o numero da parcela que tenha o vencimento que fez aniversário no mesmo mês da data do reajuste.

Através desta parcela será definido o limite entre o período do reajuste anual anterior e o novo período.

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELACOMPONENTE JOIN  XPARCELAPAGAMENTO  WHERE NUM\_VENDA = 1234 AND COD\_COMPN = 4**

**2.Sintaxe**  
GETNUMPARCELAMESANIVERSARIOREAJUSTE

**3.Exemplo**

GETNUMPARCELAMESANIVERSARIOREAJUSTE

**88. GETNUMPARCELAPORDATAVENCIMENTO**  
Retorna o numero da parcela que tenha o vencimento que fez aniversário no mesmo mês da data do reajuste.

Através desta parcela será definido o limite entre o período do reajuste anual anterior e o novo período.

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELAPAGAMENTO  WHERE NUM\_VENDA = 1234**

**2.Sintaxe**  
GETNUMPARCELAPORDATAVENCIMENTO(Data, diaExato)

A sintaxe da função tem os seguintes argumentos

* + Data– data a ser pesquisada
  + diaExato - 1 - para pesquisar da data exata e 0 para pesquisar somente mês e ano da data

**3.Exemplo**

GETNUMPARCELAPORDATAVENCIMENTO('01/01/2020', 1)

**89. ADICIONADIASPRORATA**  
Adiciona número de dias Pro-Rata a uma data passada por parâmetro. Ou Seja, não deixa a data mudar de mês.

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto GERAL

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**2.Sintaxe**  
ADICIONADIASPRORATA(Data, dias)

A sintaxe da função tem os seguintes argumentos

* + Data– data base
  + dias -  número de dias que deseja adionar na data

**3.Exemplo**

ADICIONADIASPRORATA('01/01/2020', 10)

**90. DIADOCONTRATO**  
Retorna o dia do aniversário do contrato (Data da Venda)

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto da venda

**SELECT \* FROM XVENDA WHERE NUM\_VENDA = 1234**

**2.Sintaxe**  
DIADOCONTRATO

**3.Exemplo**

DIADOCONTRATO

**91. DATACONTRATOREAJUSTE**  
Retorna a data do reajuste com base no dia do aniversário do contrato e a defasagem para Correção Monetária com moeda diária.

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  \*\*\*\*\*\***

**1.Contexto**

contexto do reajuste

**SELECT '01/01/2020'DatReajuste, \* FROM XPARCELAPAGAMENTO  WHERE NUM\_VENDA = 1234**

**2.Sintaxe**  
DATACONTRATOREAJUSTE

**3.Exemplo**

DATACONTRATOREAJUSTE

**92. TABCOMISSOES**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\***

Retorna o valor de um campo da tabela de Comissões

**92.1. Contexto**  
Comissões

**SELECT \* FROM XCOMISSOES **(NOLOCK)**** **WHERE IDCOMISSAO= 1234**

**92.2. Sintaxe**

TABCOMISSOES( STRING1, STRING2 )  
A sintaxe da função TABCOMISSOES tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela de comissoes
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**92.3. Exemplo**  
TABCOMISSOES('IDCOMISSAO','I')

**93. TABCOMISSOESCOMPL**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\***  
Retorna o valor de um campo da tabela complementar de Comissões

**93.1. Contexto**Comissões Campos Complementares

**SELECT \* FROM XCOMISSOESCOMPL **(NOLOCK)******WHERE IDCOMISSAO= 1234**

**93.2. Sintaxe**

TABCOMISSOESCOMPL( STRING1, STRING2 )  
A sintaxe da função TABCOMISSOESCOMPL tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela complementar de comissoes
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**93.3. Exemplo**  
TABCOMISSOESCOMPL('IDCOMISSAO','I')

**94. TABCOMISSOESITEM**Retorna o valor de um campo da tabela de Comissões Item

**94.1. Contexto**  
Comissões Item

**SELECT \* FROM XCOMISSOESITEM **(NOLOCK)**** **WHERE IDCOMISSAO= 1234**

**94.2. Sintaxe**

TABCOMISSOESITEM( STRING1, STRING2 )  
A sintaxe da função TABCOMISSOESITEM tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela de comissoes item
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**94.3. Exemplo**  
TABCOMISSOESITEM('IDCOMISSAO','I')

**95. TABCOMISSOESITEMPARCELA**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\***Retorna o valor de um campo da tabela de Comissões Item Parcela

**95.1. Contexto**  
Comissões Item Parcela (Item = para quem vai o pagamento da comissão)

**SELECT \* FROM XCOMISSOESITEMPARCELA **(NOLOCK)******WHERE IDCOMISSAO= 1234 AND IDITEMCOMISSAO = 1234**

**95.2. Sintaxe**TABCOMISSOESITEMPARCELA( STRING1, STRING2 )  
A sintaxe da função TABCOMISSOESITEMPARCELA tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + STRING1 – Nome do campo da tabela de comissoes item parcela
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**95.3. Exemplo**  
TABCOMISSOESITEMPARCELA('IDCOMISSAO','I')

**95. VALORTOTALCOMISSAO**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\***

Retorna o valor total da comissão gravada.

**95.1. Contexto**  
Comissões geradas

**SELECT \* FROM XCOMISSOES **(NOLOCK)******WHERE IDCOMISSAO= 1234**

**95.2. Sintaxe**VALORTOTALCOMISSAO 

**95.3. Exemplo**  
VALORTOTALCOMISSAO

**95. VALORSALDOCOMISSAO**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\***

Retorna o valor do saldo de comissão que ainda não teve o valor gerado em parcela, para geração de integração.

**95.1. Contexto**  
Comissões geradas

**SELECT \* FROM **XCOMISSOES** (NOLOCK)** **WHERE IDCOMISSAO= 1234**

**95.2. Sintaxe**VALORSALDOCOMISSAO

**95.3. Exemplo**  
VALORSALDOCOMISSAO

**95. PERCENTUALTOTALCOMISSAO**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\***

Retorna o percentual total da comissão, somatório de todos os percentuais encontrados correspondentes a cada parcela já gerada da comissão.

**95.1. Contexto**  
Comissões geradas

**SELECT \* FROM **XCOMISSOES** (NOLOCK)** **WHERE IDCOMISSAO= 1234**

**95.2. Sintaxe**PERCENTUALTOTALCOMISSAO

**95.3. Exemplo**  
PERCENTUALTOTALCOMISSAO

**96. QTDECOMISSIOANDOSCOMISSAO**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\***

Retorna a quantidade de comissionados da comissão.

**96.1. Contexto**  
Comissões geradas

**SELECT \* FROM **XCOMISSOES** (NOLOCK)** **WHERE IDCOMISSAO= 1234**

**96.2. Sintaxe**QTDECOMISSIOANDOSCOMISSAO

**96.3. Exemplo**  
QTDECOMISSIOANDOSCOMISSAO

**97. PERCENTUALCOMISSIONADO**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\***

Retorna o percentual do comissionado (empresa + cliente) da comissão

**97.1. Contexto**  
Comissões geradas

**SELECT \* FROM **XCOMISSOES** (NOLOCK)** **WHERE IDCOMISSAO= 1234**

**97.2. Sintaxe**PERCENTUALCOMISSIONADO

**97.3. Exemplo**  
PERCENTUALCOMISSIONADO

**98. VALORCOMISSIONADO**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\***

Retorna o valor do comissionado (empresa + cliente) da comissão

**98.1. Contexto**  
Comissões geradas

**SELECT \* FROM **XCOMISSOES** (NOLOCK) JOIN **XCOMISSOESITEM ON XCOMISSOES.IDCOMISSAO = XCOMISSOESITEM.IDCOMISSAO******WHERE **XCOMISSOES.**IDCOMISSAO= 1234**

**98.2. Sintaxe**VALORCOMISSIONADO

**98.3. Exemplo**  
VALORCOMISSIONADO

**99. VALORLIQUIDOPFTIN**  
Retorna o valor líquido do lançamento com origem no TOTVS Incorporação, calculado sob a mesma regra da Ficha Financeira do TOTVS Incorporação

**99.1 - Contexto**

A fórmula não depende de um contexto específico pois recebe todas as informações necessárias para o cálculo nos parâmetros

**99.2 - Sintaxe**  
VALORLIQUIDOPFTIN(COLIGADA, IDLAN, DATABASE)

* + COLIGADA e IDLAN indicam qual lançamento deve ter o valor líquido calculado
  + DATABASE - indica qual a data de referência para cálculo dos valores financeiros, como multa e juros

**100 VALORLIQUIDODESAGIOPFTIN**  
Retorna o valor líquido, com deságio, do lançamento com origem no TOTVS Incorporação, calculado sob a mesma regra da Ficha Financeira do TOTVS Incorporação

**100.1 - Contexto**

A fórmula não depende de um contexto específico pois recebe todas as informações necessárias para o cálculo nos parâmetros

**100.2 - Sintaxe**  
VALORLIQUIDODESAGIOPFTIN(COLIGADA, IDLAN, DATABASE)

* + COLIGADA e IDLAN indicam qual lançamento deve ter o valor líquido calculado
  + DATABASE - indica qual a data de referência para cálculo dos valores financeiros, como multa e juros

**101. GETVALORVENDASALDODEVEDORDATABASE**  
Retorna o valor líquido da venda de todos os lançamentos em aberto, calculado sob a mesma regra da Ficha Financeira do TOTVS Incorporação

**101.1 - Contexto**

A fórmula não depende de um contexto específico pois recebe todas as informações necessárias para o cálculo nos parâmetros

**101.2 - Sintaxe**  
GETVALORVENDASALDODEVEDORDATABASE(DATABASE)

* + DATABASE - indica qual a data de referência para cálculo dos valores financeiros, como multa e juros

**102. GETVALORVENDASALDODEVEDORDATABASE**  
Retorna o valor líquido, com deságio,  da venda de todos os lançamentos em aberto, calculado sob a mesma regra da Ficha Financeira do TOTVS Incorporação

**102.1 - Contexto**

A fórmula não depende de um contexto específico pois recebe todas as informações necessárias para o cálculo nos parâmetros

**102.2 - Sintaxe**  
GETVALORVENDASALDODEVEDORDATABASE(DATABASE)

* + DATABASE - indica qual a data de referência para cálculo dos valores financeiros, como multa e juros

**103. COMISSAOMETAEMPRVALOR \*12.12310**  
Retorna o valor de todas as vendas no mês da comissão para o empreendimento filtrado. Primeiro argumento o tipo de cálculo da meta da comissão nome do campo.

**103.1 - Contexto**

Usa como contexto a chave da tabela "XCOMISSOESITEM".

**103.2 - Sintaxe**  
COMISSAOMETAEMPRVALOR(CodEmpreendimento)

* + CodEmpreendimento - Código do empreendimento que deseja filtrar as vendas

**104. COMISSAOMETAEMPRQTD \*12.12310**  
Retorna a quantidade de todas as vendas no mês da comissão para o empreendimento filtrado. Primeiro argumento o tipo de cálculo da meta da comissão nome do campo.

**104.1- Contexto**

Usa como contexto a chave da tabela "XCOMISSOESITEM".

**104.2 - Sintaxe**  
COMISSAOMETAEMPRQTD(CodEmpreendimento)

* + CodEmpreendimento - Código do empreendimento que deseja filtrar as vendas

**105. DATAGERACAOPARCELACOMISSAO \*12.12310**  
Retorna a data do último dia da geração da parcela na comissão

**105.1- Contexto**

Usa como contexto a chave da tabela "XCOMISSOESITEM".

**105.2 - Sintaxe**  
DATAGERACAOPARCELACOMISSAO

**106. EXISTEPARCELACOMISSAODATAGERADA \*12.12310**  
Existe parcela gerada na competência pesquisada

**106.1- Contexto**

Usa como contexto a chave da tabela "XCOMISSOESITEM".

**106.2 - Sintaxe**  
COMISSAOMETAEMPRQTD(Data)

* + Data - Data Pesquisada, mas a comparação é somente competência

**106.3 - Retorno**

* + 1 Verdadeiro e 0 Falso

**107. TOTALPAGOVENDAORIGINAL  \*12.12310**  
Retorna o valor total original baixado da venda

**107.1- Contexto**

Usa como contexto a chave da tabela "XVENDA".

**107.2 - Sintaxe**  
TOTALPAGOVENDAORIGINAL

**108. VALORVENDACOMPONENTE  \*12.12310**  
Retorna o valor total de um componente da venda

**1- Contexto**

Usa como contexto a chave da tabela "XVENDA".

**2 - Sintaxe**  
VALORVENDACOMPONENTE

**109. SETCOMISSIONADO   \*12.12310**  
Define o comissionado no momento da geração da comissão, só pode ser usado nas fórmulas de calcular valor ou percentual do comissionado. Essa função é usada quando um determinada pessoa está vinculada a equipe/imobiliária.

**1- Contexto**

Usa como contexto a chave da tabela "XCOMISSOESITEM".

**2 - Sintaxe**  
SETCOMISSIONADO(codcolCFO, codCFO)

* + codcolCFO - Coligada do comissionado a ser trocado na regra
  + codCFO - Código do comissionado a ser trocado na regra

**110. SETCOMISSIONADOFORNECEDOR  \*12.12310**  
Define a empresa que o comissionado irá receber no momento da validação da integração da comissão. Essa função é usada quando um determinada pessoa tem um empresa e a gestão da comissão é feita com a pessoa física e o pagamento para a pessoa jurídica.   

**1- Contexto**

Usa como contexto a chave da tabela "XCOMISSOESITEM".

**2 - Sintaxe**  
SETCOMISSIONADOFORNECEDOR(codcolCFO, codCFO)

* + codcolCFO - Coligada do comissionado a ser trocado na regra
  + codCFO - Código do comissionado a ser trocado na regra

**111. SETCOMISSIONADOMETA\*12.12310**  
Define a a meta que o comissionado irá receber no momento da geração da comissão.  Só pode ser usado nas fórmulas de calcular valor ou percentual do comissionado. Essa função é usada quando um determinada pessoa está vinculada a equipe/imobiliária e deseja troca a meta no momento da geração da comissão

**1- Contexto**

Usa como contexto a chave da tabela "XCOMISSOESITEM".

**2 - Sintaxe**  
SETCOMISSIONADOMETA(idMeta)

* + idMeta- Id da Meta

**112. SETDELETACOMISSIONADO\*12.12310**  
Apaga a comissão de um comissionado no momento da geração da comissão.  Só pode ser usado nas fórmulas de calcular valor ou percentual do comissionado. Essa função é usada quando um determinada pessoa não terá comissão por uma condição, então apagamos ela no momento da geração da comissão

**1- Contexto**

Usa como contexto a chave da tabela "XCOMISSOESITEM".

**2 - Sintaxe**  
SETDELETACOMISSIONADO

**113. TIPORECALCULOCOMISSAO   \*12.12310**  
Retorna o tipo de recálculo que a comissão está executando: 1 - Para recálculo padrão , 2- Para recálculo por competência

**1- Contexto**

Usa como contexto a chave da tabela "XCOMISSOESITEM".

**2 - Sintaxe**  
TIPORECALCULOCOMISSAO

**114. QTDECOMISSIOANDOSCOMISSAOFUNCAO**

**\*\*\*\*\*\*Somente para o novo reajuste revitalizado 4.0  e Clientes Piloto da Nova Comissão 2.0\*\*\*\*\*\***

Retorna a quantidade de comissionados da comissão.

**96.1. Contexto**  
Comissões geradas

**SELECT \* FROM **XCOMISSOES** (NOLOCK)** **WHERE IDCOMISSAO= 1234**

**96.2. Sintaxe**QTDECOMISSIOANDOSCOMISSAOFUNCAO(Cod. Função)

**96.3. Exemplo**  
QTDECOMISSIOANDOSCOMISSAOFUNCAO(1)

**115. TABCOMISSOESITEM**Retorna o valor de um campo da tabela de Comissões Item

**1. Contexto**  
Comissões Item

**SELECT \* FROM XCOMISSOESITEM **(NOLOCK)**** **WHERE IDCOMISSAO= 1234**

**2. Sintaxe**

TABCOMISSOESITENS( INT, STRING1, STRING2 )  
A sintaxe da função TABCOMISSOESITENS tem os seguintes argumentos (argumento: um valor que fornece informações a uma ação, um evento, um método, uma função ou um procedimento.):

* + INT - Código da Função
  + STRING1 – Nome do campo da tabela de comissões item
  + STRING2 – Tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**3. Exemplo**  
TABCOMISSOESITENS(1,'IDCOMISSAO','I')

**116. TABCOMISSOESITEMCOMPL**Retorna o valor de um campo da tabela de Comissões Item

**1. Contexto**  
Item da Comissão

Retorna o valor de um campo da tabela de campos complementares da comissão da venda. Primeiro argumento nome do campo. Segundo argumento tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora)

**2. Sintaxe**

TABCOMISSOESITEMCOMPL ( STRING,STRING )    INDEFINIDO

**117. TABVENDACOMPL**Retorna o valor de um campo da tabela de Comissões Item

**1. Contexto**  
Venda

 Retorna o valor de um campo da tabela de venda complementar. Primeiro argumento nome do campo

**2. Sintaxe**

TABVENDACOMPL ( STRING,STRING )    INDEFINIDO

**118. TABEMPREENDIMENTOCOMPL**Retorna o valor de um campo da tabela de Comissões Item

**1. Contexto**  
Venda

Retorna o valor de um campo da tabela de empreendimento complementar. | Primeiro argumento nome do campo. Segundo argumento tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora).

**2. Sintaxe**

ABEMPREENDIMENTOCOMPL ( STRING,STRING )    INDEFINIDO

| GETTIPOCALCULOJUROSCMREAJUSTE | Retorna o tipo de cálculo do juros sobre o CM e o oposto também. Retorno (0 = Principal 1 = Principal + Mês Anterior (CM ou Juros), 2 = Principal + Atual (CM ou Juros)) |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | GETTIPOCALCULOJUROSCMREAJUSTE |

| GETPROXIMOANIVERSARIO | Retorna a data do próximo aniversario para o cálculo do reajuste de juros/CM. |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | GETPROXIMOANIVERSARIO |

| DATAPERIODOATUALREAJUSTE | Retorna a data do loop do período do reajuste/geração do plano da parcela do contexto. |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | DATAPERIODOATUALREAJUSTE |

| VALORBASEREAJUSTE | Retorna o base da parcela para o cálculo do reajuste/geração de plano do contexto de juros/CM |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | VALORBASEREAJUSTE |

| VALORCOMPONENTEREAJUSTE | Retorna o valor do reajuste da parcela para o cálculo do reajuste/geração de plano do contexto de juros/CM |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | VALORCOMPONENTEREAJUSTE |

| VALORINDICEREAJUSTE | Retorna o índice da parcela para o cálculo do reajuste/geração de plano do contexto de juros/CM |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | VALORINDICEREAJUSTE |

| GETVALORCMACUMULADA | Calcula a Variação da Correção Monetária (Índice Acumulado). Primeiro argumento moeda. Segundo argumento data início correção. Terceiro argumento data fim correção. Quarto argumento defasagem do índice. |
| --- | --- |
| **CONTEXTO** | Usa como contexto o reajuste. |
| **SINTAXE** | GETVALORCMACUMULADA('IGPM', '01/01/2020', '01/09/2020', 2) |

| GETVALORCMACUMULADAPARAM | Calcula a Variação da Correção Monetária (Índice Acumulado). Primeiro argumento moeda. Segundo argumento data fim correção. Terceiro argumento defasagem do índice. Quarto argumento periodicidade que será retirado da data final para acumular o índice. Quinto argumento ignorar deflação 0 para não e 1 para sim. |
| --- | --- |
| **CONTEXTO** | Usa como contexto o reajuste. |
| **SINTAXE** | GETVALORCMACUMULADAPARAM('IGPM', '01/12/2020', 2, 12, 1) |

| GETVALORCMMENSAL | Calcula a Variação da Correção Monetária (Índice Mensal). Primeiro argumento moeda. Segundo argumento data início correção. Terceiro argumento data fim correção. Quarto argumento defasagem do índice. |
| --- | --- |
| **CONTEXTO** | Usa como contexto o reajuste. |
| **SINTAXE** | GETVALORCMMENSAL('IGPM', '01/01/2020', '01/09/2020', 2) |

| GETVALORCMMENSALPARAM | Calcula a Variação da Correção Monetária (Índice Mensal). Primeiro argumento moeda. Segundo argumento data fim correção. Terceiro argumento defasagem do índice. Quarta argumento periodicidade que será retirado da data final para acumular o índice. Quinto argumento ignorar deflação 0 para não e 1 para sim. |
| --- | --- |
| **CONTEXTO** | Usa como contexto o reajuste. |
| **SINTAXE** | GETVALORCMMENSALPARAM('IGPM', '01/12/2020', 2, 12, 1) |

| SETAPLICARVALORFORMULAFINANCEIRO | Define se é para enviar o valor para o financeiro ou não. Primeiro argumento 1 ou 0. |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | SETAPLICARVALORFORMULAFINANCEIRO(0) |

| GETPROXIMOANIVERSARIOPERIODOATUAL | Retorna a data do próximo aniversario em relação ao período atual para o cálculo do reajuste de juros/CM |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | GETPROXIMOANIVERSARIOPERIODOATUAL |

| GETVALORINCIDENCIACONTABILVENDA | Sistema: (TCGI) | Contexto: (Venda) | Contabilidade | Retorno o valor a contabilizar dos processos de Venda, Aditivo, Distrato e Reajuste. TDN: |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" e seus tipo de contexto |
| **SINTAXE** | GETVALORINCIDENCIACONTABILVENDA('ValorVendaCurtoPrazo') |

| GETVALORCORRECAOACUMULADOCONTABIL | Sistema: (TCGI) | Contexto: (Venda) | Retorna o valor contábil de correção monetária da venda  reajustada. Para não reajustar ate o dia do vencimento, preencher o 2º parâmetro com o valor FALSE |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | GETVALORCORRECAOACUMULADOCONTABIL(data\_reajsute, true) |

| GETVALORCORRECAOCONTABIL | Sistema: (TCGI) | Contexto: (Venda) | Retorna o valor contábil de correção monetária da venda  reajustada do período informado. Para não reajustar ate o dia do vencimento, preencher o 3º parâmetro com o valor FALSE |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | GETVALORCORRECAOCONTABIL(data\_ninico, data\_final, true) |

| GETVALORJUROSACUMULADOCONTABIL | Sistema: (TCGI) | Contexto: (Venda) | Retorna o valor contábil de juros da venda  reajustada. Para não reajustar ate o dia do vencimento, preencher o 2º parâmetro com o valor FALSE |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | GETVALORJUROSACUMULADOCONTABIL(data\_reajsute, true) |

| GETVALORJUROSCONTABIL | Sistema: (TCGI) | Contexto: (Venda) | Retorna o valor contábil de juros da venda  reajustada do período informado. Para não reajustar ate o dia do vencimento, preencher o 3º parâmetro com o valor FALSE |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | GETVALORJUROSCONTABIL(data\_ninico, data\_final, true) |

| CUSTOINCORRIDOSOLUN | Sistema: (TCGI) | Contexto: (Geral) | Retorna o valor  do custo incorrdo do Solum |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | CUSTOINCORRIDOSOLUN(int codColigada, int idPrj, int idObra, int idEtapa, string codUsuario) |

| VALORCONTA | Sistema: (TCGI) | Contexto: (POC) | Retorna o valor de uma Conta Contábil. | Primeiro argumento Codigo da Conta Contábil. Segundo argumento Tipo do Saldo a retornar. Legenda: (0 = Debito, 1 = Credito, 2 = MovimentacaoConta, 3 = SaldoAnterior, 4 = SaldoAtual). Terceiro argumento Codigo do Centro de Custo |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | VALORCONTA(string CodConta, string ValRetorno, string CodCentroCusto) |

| VALORCONTACONTABIL | Sistema: (TCGI) | Contexto: (POC) | Retorna o valor de uma Conta Contábil. | Primeiro argumento Codigo da Conta. Segundo argumento tipo do campo. Legenda: (0 = Debito, 1 = Credito, 2 = MovimentacaoConta, 3 = SaldoAnterior, 4 = SaldoAtual). Terceiro argumento Coligada Historico Padrão. Quarto argumento Codigo Historico Padrão. Quinto argumento Codigo Centro de Custo |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | VALORCONTACONTABIL |

| VALORCONTACONTABILPERIODO | Sistema: (TCGI) | Contexto: (POC) | Retorna o valor de uma Conta Contábil dentro de um período. | Primeiro argumento Codigo da Conta. Segundo argumento tipo do campo. Legenda: (0 = Debito, 1 = Credito, 2 = MovimentacaoConta, 3 = SaldoAnterior, 4 = SaldoAtual). Terceiro argumento Coligada Historico Padrão. Quarto argumento Codigo Historico Padrão. Quinto argumento Codigo Centro de Custo. Sexto argumento Data Início Apuração. Sétimo argumento Data Fim Apuração |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | VALORCONTACONTABILPERIODO |

| DATAFIMPERIODO | Sistema: (TCGI) | Contexto: (POC) | Retorna o valor da data final do período corrente |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | DATAFIMPERIODO |

| DATAINICIOAPURACAO | Sistema: (TCGI) | Contexto: (POC) | Retorna o valor da data inicial do período corrente |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | DATAINICIOAPURACAO |

| DATATERMINOAPURACAO | Sistema: (TCGI) | Contexto: (POC) | Retorna o valor da data final do período corrente |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | DATATERMINOAPURACAO |

| IDANDAMENTOAPURACAO | Sistema: (TCGI) | Contexto: (POC) | Retorna o Id Andamento Apuração |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | IDANDAMENTOAPURACAO |

| IDAVANCOAPURACAO | Sistema: (TCGI) | Contexto: (POC) | Retorna o Id Avanço Apuração |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | IDAVANCOAPURACAO |

| RESULTADOAPURACAOSUBUNIDADE | Sistema: (TCGI) | Contexto: (POC) | Retorna o resultado da apuração por subunidade |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | RESULTADOAPURACAOSUBUNIDADE |

| RESULTADOAPURACAOEMPREENDIMENTO | Sistema: (TCGI) | Contexto: (POC) | Retorna o resultado da apuração por empreendimento |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | RESULTADOAPURACAOEMPREENDIMENTO |

| TOTALITEMCOMPOSICAO | Sistema: (TCGI) | Contexto: (POC) | Retorna o valor do item de composição da base de calculo |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | TOTALITEMCOMPOSICAO(int CodEvento) |

| POC | Sistema: (TCGI) | Contexto: (POC) | Retorna o valor do POC |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | POC |

| POCACUMULADO | istema: (TCGI) | Contexto: (POC) | Retorna o valor do POC acumulado |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | POCACUMULADO |

| PRECOVENDA | Sistema: (TCGI) | Contexto: (POC) | Retorna o valor da venda da subunidade |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | PRECOVENDA |

| DATAVENDA | Sistema: (TCGI) | Contexto: (POC/Venda) | Retorna a data da venda da subunidade |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | DATAVENDA |

| VALORDISTRATO | Sistema: (TCGI) | Contexto: (POC) | Retorna o valor da venda da subunidade no distrato |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | VALORDISTRATO |
