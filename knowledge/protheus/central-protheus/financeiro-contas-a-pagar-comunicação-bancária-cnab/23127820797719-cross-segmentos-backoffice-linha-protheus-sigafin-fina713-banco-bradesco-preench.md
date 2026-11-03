---
article_id: 23127820797719
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: a6612c3656405aa9a0f3d3c7d8a926a359c9b595943d65fd45abaa9a92f630a2
fetched_at: '2026-06-28T22:37:56.294420+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Banco Bradesco
  preenchimento das tags idProduto e nuNegociacao do XML
type: support-article
updated_at: '2024-04-29T17:35:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23127820797719-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Banco-Bradesco-preenchimento-das-tags-idProduto-e-nuNegociacao-do-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23127820769943) Tempo aproximado para leitura: **00:05:00min** **Dúvida**Como alterar o conteúdo das tags idProduto e nuNegociacao do XML que é enviado ao banco Bradesco?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - A partir da release 12.1.33  
  
**Solução**

O **idProduto** recebe o conteúdo do **EE\_CODCART** dos **Parâmetros de Banco(FINA130)**. **ID Produto** **(código da carteira/modalidade de cobrança. Ex 09 Cobrança escritural, 05 Cobrança de Seguros)**

O **nuNegociacao** recebe por padrão a agência informada na **SEE (parâmetros de banco - FINA130)** + **0000000 + Conta (7 posições)**.

**Exemplo**  
**nuNegocicao** com conteúdo -> 519000000000084180 -> 5190 seria a **agência**, depois tem o sequencial de zeros e as últimas 7 posições são referente a **Conta**.
