---
content_hash: ed611ca72ecc9a851c3a52c1d28efc9f570a2d5e8a30ff2a144173997def9d64
fetched_at: '2026-06-29T00:09:34.802352+00:00'
page_id: '425459251'
product: rm
source: tdn-rm
title: Correspondência - Lookup e Lookup CRM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459251
version: 2
---

**Correspondência - Lookup e Lookup CRM**

---

**Lookup**  
    
 A operação Lookup recebe um valor e retorna de acordo com as parametrizações realizadas outro valor.

Por exemplo, temos as tabelas abaixo:

|  |  |
| --- | --- |
| **Tabela:** | **PAIS** |
| COD | NOME |
| 1 | Brasil |
| 2 | Inglaterra |

|  |  |
| --- | --- |
| **Tabela:** | **PAISDETALHE** |
| COD | CAPITAL |
| 1 | Brasília |
| 2 | Londres |

A tabela PAISDETALHE está disponível na Lista de Tabelas na Estrutura Origem, mas não foi adicionada nas Tabelas de Importação, e não aparece para realizar as Correspondências.   
    
 Entretanto, é necessário buscar a capital de um país para ser entrada em um campo no Destino.   
    
 Dessa forma, a entrada na operação lookup será o código do país da tabela PAIS (campo COD). A operação irá buscar na tabela PAISDETALHE o campo COD com o valor correspondente ao informado, e retornar o valor do campo CAPITAL.  
 Os parâmetros para configurar a operação Lookup são:

*Alimentação*

* **Entrada:** Ponto de entrada da operação ou campo.

*Diversos*

* **Campo Chave:** Informe o campo da tabela que deve ter seu valor comparado com o campo informado na Entrada.
* **Campo Valor:** Informe o campo que deve ter seu valor retornado pelo lookup.
* **Nome da Conexão:** Informe o nome da conexão de origem utilizada.
* **Nome da Tabela ou Query:** Informe o nome da tabela ou query que será utilizada para o lookup (tabela ou query cujo campo foi informado na prorpiedade "CampoValor").

*Identificação*

* **Nome:** Nome da operação.
* **Nome:** Campo somente leitura, tem como valor o tipo da operação**.**

**Lookup CRM**  
    
 A operação Lookup CRM recebe um valor e retorna de acordo com as parametrizações realizadas outro valor.   
 Funciona da mesma forma que a operação Lookup, exceto que os dados são buscados na base CRM.  
    
 Os parâmetros para configurar a operação são:

*Alimentação*

* **Entrada:** Ponto de entrada da operação ou campo.

*Diversos*

* **Campo Chave:** Informe o campo da tabela que deve ter seu valor comparado com o campo informado na Entrada.
* **Campo Valor:** Informe o campo que deve ter seu valor retornado pelo lookup.
* **Connection Name:** Informe o nome da conexão de origem utilizada.
* **Entity Name:** Informe o nome da entidade da base CRM.

*Identificação*

* **Nome:** Nome da operação.
* **Nome:** Campo somente leitura, tem como valor o tipo da operação.

---

**Recursos Adicionais**

Acesse o boletim técnico abaixo para ver um exemplo da operação lookup:

[Conceito utilizando Operação Lookup](http://totvsconnect.blogspot.com/2011/06/como-fazer-conceito-utilizando-operacao_2026)
