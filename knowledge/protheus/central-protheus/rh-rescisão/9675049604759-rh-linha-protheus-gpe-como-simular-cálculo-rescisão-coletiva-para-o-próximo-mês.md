---
article_id: 9675049604759
category: RH - Rescisão
content_hash: 1a54d0d2d82546ebe343db0a61de6c3250c72c2ad4c3a1909e7980cc6149c265
fetched_at: '2026-06-28T22:43:52.123205+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como simular cálculo Rescisão Coletiva para o próximo
  mês com mês vigente aberto da folha de pagamento
type: support-article
updated_at: '2025-09-11T01:02:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9675049604759-RH-Linha-Protheus-GPE-Como-simular-c%C3%A1lculo-Rescis%C3%A3o-Coletiva-para-o-pr%C3%B3ximo-m%C3%AAs-com-m%C3%AAs-vigente-aberto-da-folha-de-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34844319987735) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como simular cálculo Rescisão Coletiva para o próximo mês com mês vigente aberto da folha de pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as Versões.  
  
**Solução**

Para simular cálculo de rescisão coletiva em mês posterior ao mês vigente da folha de pagamento, no cadastro do período do mês atual, pelo caminho**>Atualizações >Definições de cálculos >Períodos**, roteiro RES, o campo período ativo\selecionado alterar para Não.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34844319988247)

Após a alteração, acessar o cadastro do período do mês posterior, roteiro RES, o campo período ativo\selecionado alterar para Sim.

Desta forma o sistema vai considerar o mês posterior como ativo para cálculo rescisão.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34844334739991)

Em seguida acesse a rotina rescisão coletiva, em tipo de cálculo informa Simular e selecione o período RES Ativo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9675044435479)

**Obs:** Após efetuar a rescisão do mês posterior, voltar as informações para que não ocorra inconsistências ao efetuar o fechamento da folha do mês atual.

**Saiba mais**

[RH - Linha Protheus - GPE - Como calcular rescisão coletiva](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035614253-RH-Linha-Protheus-GPE-Como-calcular-rescis%C3%A3o-coletiva?source=search)

[RH - Linha Protheus - GPE - Como calcular Rescisão para o próximo mês com mês vigente aberto da folha de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050822613-RH-Linha-Protheus-GPE-Como-calcular-Rescis%C3%A3o-para-o-pr%C3%B3ximo-m%C3%AAs-com-m%C3%AAs-vigente-aberto-da-folha-de-pagamento?source=search)
