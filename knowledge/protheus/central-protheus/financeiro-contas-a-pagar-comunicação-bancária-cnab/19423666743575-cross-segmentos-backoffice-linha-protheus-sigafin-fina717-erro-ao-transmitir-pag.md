---
article_id: 19423666743575
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 77d44a28e2d4141eddbf3d64c0cfb4f123e478c9705aab2a2369aaee4a319af3
fetched_at: '2026-06-28T22:37:56.357197+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA717 - Erro ao transmitir
  pagamento "Código da Receita do tributo não informado"
type: support-article
updated_at: '2023-11-29T17:32:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19423666743575-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA717-Erro-ao-transmitir-pagamento-C%C3%B3digo-da-Receita-do-tributo-n%C3%A3o-informado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19423658948759) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar a transmissão de pagamentos (FINA717), ocorre a mensagem **"Código da Receita do tributo não informado"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19423675334423)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - a partir da release 12.1.2210  
  
**Causa**Esse incidente ocorre, pois ao gerar os títulos de pagamento, não possui código de retenção **(E2\_CODRET)** ou o código informado está invalido  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o título gerado para transmissão de pagamento na **FINA050**  
2. Na aba de **impostos** e alterar o campo **E2\_DIRF = Sim** e informar no campo **Cod. Retenção** **(E2\_CODRET)** o código da receita.

3. Realize a transmissão dos títulos rejeitados através do botão "**Transmitir Rejeitados**"   
  
**Saiba mais:**

#### [Contas a pagar (Comunicação bancária online)](https://tdn.totvs.com/pages/viewpage.action?pageId=734394071)

#### [Novo Gestor Financeiro - (FINA710 - SIGAFIN)](https://tdn.totvs.com/pages/viewpage.action?pageId=611007335)
