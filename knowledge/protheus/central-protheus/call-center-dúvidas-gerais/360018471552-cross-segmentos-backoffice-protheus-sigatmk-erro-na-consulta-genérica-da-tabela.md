---
article_id: 360018471552
category: Call Center - Dúvidas Gerais
content_hash: 0cf0cd1cae16462ed6f2b7cda3118385f0ba0d1c31363c26d7564150b58f6d2d
fetched_at: '2026-06-28T22:41:26.669765+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Erro na consulta genérica
  da tabela SU5
type: support-article
updated_at: '2024-04-29T13:07:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018471552-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Erro-na-consulta-gen%C3%A9rica-da-tabela-SU5
---

**Ocorrência**

Ao efetuar a consulta genérica da tabela SU5, gera o erro: type mismatch on + on {||Posicione("SX5",1,xFilial("SX5")+'AX'+M->U5\_TRATA,"X5\_DESCRI")  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12

**Causa**

O erro ocorre por que na estrutura do posicione, contida no X3\_INIBRW e X3\_RELAÇÂO do campo U5\_TRATADE, existe uma variável de memória (M) para atribuição de campo U5\_TRATA, só é possível utilizar uma variável de memória, quando se está dentro da tabela, neste caso em específico, é preciso utilizar a chamada da própria tabela SU5 para não gerar o erro na consulta genérica.  
  
**Solução**

A correção encontra-se em dicionário de dados disponibilizado no portal do cliente, basta efetuar o download do dicionário, descompactar o arquivo na pasta system e rodar o upddistr no programa inicial do Protheus.

De forma paliativam efetue a seguinte alteração:

* De: posicione("SX5",1,XFILIAL("SX5")+"AX"+M->U5\_TRATA,"U5\_DESCRI")
* Para: **posicione("SX5",1,XFILIAL("SX5")+"AX"+****SU5->U5\_TRATA,"U5\_DESCRI")**

A informação deverá ser alterada tanto no X3\_INIBRW quanto no X3\_RELAÇÂO da tabela.
