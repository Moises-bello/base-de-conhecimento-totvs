---
article_id: 29104534722711
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 0da53a487e96677fa5d07d0ad3190c32b3ff35dac48b3a9f8eb8b52feef9023c
fetched_at: '2026-06-28T22:38:55.708125+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA105 - Por que
  o campo CP_ NUMSC fica em branco mesmo gerando Solicitação de Compras a partir da
  Pré-Requisição ao Armazém?
type: support-article
updated_at: '2025-03-12T12:28:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29104534722711-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA105-Por-que-o-campo-CP-NUMSC-fica-em-branco-mesmo-gerando-Solicita%C3%A7%C3%A3o-de-Compras-a-partir-da-Pr%C3%A9-Requisi%C3%A7%C3%A3o-ao-Armaz%C3%A9m
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29104550124951) Tempo aproximado para leitura: **00:01:12 min** **Dúvida**Por que o campo CP\_ **NUMSC** fica em branco mesmo gerando Solicitação de Compras a partir da Pré-Requisição ao Armazém?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
  
**Solução**O relacionamento da Solicitação ao Armazém (**SCP**) X Solicitação de Compras (**SC1**) foi alterado desde o release **12.1.16** do Protheus.  
  
Atualmente o campo **CP\_NUMSC** não é atualizado, pois a tabela **SCP** é criada antes da SC1, sendo assim, não é um campo mais atualizado pelas rotinas do Sistema.

Hoje, se o usuário quiser identificar via tabela se houve geração de Solicitação de Compras para atender à uma Pré-Requisição ao Armazém, basta consultar pelo campo **CQ\_NUMSC**. Pois como a **SCQ** é da Pré-Requisição, ela sim tem condição de já criar a SC com seu numero.  
  
**TDN com detalhamento sobre a descontinuidade de atualização do CP\_NUMSC**  
<https://tdn.totvs.com/x/PpkTEQ>

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
