---
article_id: 9675247717911
category: RH - Rescisão
content_hash: 1f5297928f9f0af4a1750deb68e313f0b91bf7115332ecac67b82bd6187fa7d5
fetched_at: '2026-06-28T22:43:52.063417+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como efetivar cálculo simulado de Rescisão Coletiva
  para o próximo mês com mês vigente aberto da folha de pagamento
type: support-article
updated_at: '2025-09-11T01:01:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9675247717911-RH-Linha-Protheus-GPE-Como-efetivar-c%C3%A1lculo-simulado-de-Rescis%C3%A3o-Coletiva-para-o-pr%C3%B3ximo-m%C3%AAs-com-m%C3%AAs-vigente-aberto-da-folha-de-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34856803679895) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como efetivar cálculo simulado de Rescisão Coletiva para o próximo mês com mês vigente aberto da folha de pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as Versões.  
  
**Solução**

Para efetivar cálculo simulado de rescisão coletiva em mês posterior ao mês vigente da folha de pagamento, no cadastro do período do mês atual, pelo caminho**>Atualizações >Definições de cálculos >Períodos**, roteiro RES, o campo período ativo\selecionado alterar para Não.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34856803685911)

Após a alteração, acessar o cadastro do período do mês posterior, roteiro RES, o campo período ativo\selecionado alterar para Sim.

Desta forma o sistema vai considerar o mês posterior como ativo para cálculo rescisão.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34856803687447)

Em seguida acesse a rotina rescisão coletiva, em tipo de cálculo informa Efetivar e selecione o período RES Ativo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9675192970647)

**Obs:** Após efetuar a rescisão do mês posterior, voltar as informações para que não ocorra inconsistências ao efetuar o fechamento da folha do mês atual.

**Saiba mais**

[RH - Linha Protheus - GPE - Como calcular rescisão coletiva](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035614253-RH-Linha-Protheus-GPE-Como-calcular-rescis%C3%A3o-coletiva?source=search)

[RH - Linha Protheus - GPE - Como calcular Rescisão para o próximo mês com mês vigente aberto da folha de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050822613-RH-Linha-Protheus-GPE-Como-calcular-Rescis%C3%A3o-para-o-pr%C3%B3ximo-m%C3%AAs-com-m%C3%AAs-vigente-aberto-da-folha-de-pagamento?source=search)
