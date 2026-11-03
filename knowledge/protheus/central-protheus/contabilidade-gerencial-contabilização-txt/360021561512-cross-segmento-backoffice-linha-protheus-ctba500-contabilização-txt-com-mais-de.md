---
article_id: 360021561512
category: Contabilidade Gerencial - Contabilização txt
content_hash: 585c621e27fa42e8730eb6bafbbc1d7af79295f6a85862aec8fafe74c4c24b53
fetched_at: '2026-06-28T22:40:55.424880+00:00'
product: protheus
section_id: 1500001537521
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - CTBA500 - Contabilização TXT com
  mais de uma data
type: support-article
updated_at: '2021-10-25T13:54:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021561512-Cross-Segmento-Backoffice-Linha-Protheus-CTBA500-Contabiliza%C3%A7%C3%A3o-TXT-com-mais-de-uma-data
---

**Dúvida**É possível realizar Contabilização TXT com mais de uma Data (Dia) informada no arquivo  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**

O sistema possibilita criar em um arquivo txt mais de um data ao utilizar o  **LerData** e informar "SIM" no parâmetro **![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018570432/mceclip1.png)**

Arquivo .TXT    
200  X 123456   123456 Lançamento de NF. n. 00001  1000,25        ddmmaa ou ddmmaaaa  
|        |         |        |            |                                                |  
|        |         |        |            |                                                |->Valor (posição 50 tam 6)  
|        |         |        |            |  
|        |         |        |            |->Descricao (posição 24 tam 24)  
|        |         |        |  
|        |         |        |->Conta Credito (posição 17 tam 6)  
|        |         |  
|        |         | ->Conta Debito (posição 8 tam 6)  
|        |  
|        |-> Informativo para o TXT  
|  
|->Número do lancto padronizado (posição 1 tam 3)  
  
Informações que devem estar contidas nos campos respectivos do Lançamento Padrão.   
Código: 200  
Conta Debito : LerStr(8,6)  
Conta Credito: LerStr(17,6)  
Histórico : LerStr(24,24)   
Valor : LerVal(50,6)  
Data : **LerData**(70,6) para ddmmaa, ou lerdata(70,8) para ddmmaaaa.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018448811/mceclip0.png)

Veja mais :

[MP - SIGACTB: Qual e a funcionalidade da função Lerdata?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018755391-MP-SIGACTB-Qual-e-a-funcionalidade-da-fun%C3%A7%C3%A3o-Lerdata-?source=search)
