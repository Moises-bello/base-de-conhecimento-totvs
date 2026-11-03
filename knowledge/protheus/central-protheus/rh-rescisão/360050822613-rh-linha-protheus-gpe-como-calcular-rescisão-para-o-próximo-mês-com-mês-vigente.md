---
article_id: 360050822613
category: RH - Rescisão
content_hash: 881a7403242f56b78289c562f8453a641782f2304adc7d7ace01d6b2f0d55f06
fetched_at: '2026-06-28T22:43:52.001917+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular Rescisão para o próximo mês com mês
  vigente aberto da folha de pagamento
type: support-article
updated_at: '2025-06-12T12:31:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050822613-RH-Linha-Protheus-GPE-Como-calcular-Rescis%C3%A3o-para-o-pr%C3%B3ximo-m%C3%AAs-com-m%C3%AAs-vigente-aberto-da-folha-de-pagamento
---

**Dúvida**Como calcular Rescisão para o próximo mês com o mês vigente aberto da folha de pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da Versão 12.  
  
**Solução**Para cálculo de rescisão em mês posterior ao mês vigente da folha de pagamento, no cadastro do período do mês atual, pelo caminho **>Atualizações >Definições de cálculos >Períodos**, roteiro RES, o campo período ativo\selecionado alterar para Não.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100294613/mceclip0.png)

Após a alteração, acessar o cadastro do período do mês posterior, roteiro RES, o campo período ativo\selecionado alterar para Sim.

Desta forma o sistema vai considerar o mês posterior como ativo para cálculo rescisão.   
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098034914/mceclip1.png)

**Obs:**Após efetuar a rescisão do mês posterior, voltar as informações para que não ocorra inconsistências ao efetuar o fechamento da folha do mês atual.
