---
article_id: 5252885737623
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 597c9303ea020eea0e4021764ab86050486a50fb648542c021ad2d4cbc5040d2
fetched_at: '2026-06-28T22:37:55.398380+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA130 Como é gerado
  o numero de lote nas baixas via retorno CNAB E5_LOTE
type: support-article
updated_at: '2022-05-26T20:42:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5252885737623-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA130-Como-%C3%A9-gerado-o-numero-de-lote-nas-baixas-via-retorno-CNAB-E5-LOTE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 Min****Dúvida**Como é gerado o número de lote nas baixas via retorno CNAB para as carteiras do Pagar e Receber?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**O número de lote é gerado pela rotina de **Parâmetros de Bancos** ( **FINA130** ) onde é possível informar um número inicial que será incrementando após geração de novos lotes, para adicionar a numeração inicial do lote, deve preencher os campo abaixo.

**EE\_LOTE** ( **Lote Cnab** ) **Carteira Contas a Receber**  
**EE\_LOTECP** ( **Lote Cnab CP** ) **Carteira Contas a Pagar**

![LOTE.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5252856796439/LOTE.png)

**Saiba mais:**  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - CNAB - Qual a estrutura do CNAB modelo 2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004893528-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Qual-a-estrutura-do-CNAB-modelo-2)
