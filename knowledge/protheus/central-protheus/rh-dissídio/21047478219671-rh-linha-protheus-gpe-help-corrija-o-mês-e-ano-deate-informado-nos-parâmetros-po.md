---
article_id: 21047478219671
category: RH - Dissídio
content_hash: 6e9f48891b6239b6a118acc5712e69f60b1b906d74f5f6e6d53cbaf92e14532f
fetched_at: '2026-06-28T22:43:43.595716+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: 'RH - Linha Protheus - GPE - HELP: Corrija o mês e ano De/Ate informado nos
  parâmetros pois ambos devem pertencer a períodos fechados'
type: support-article
updated_at: '2025-09-09T12:22:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21047478219671-RH-Linha-Protheus-GPE-HELP-Corrija-o-m%C3%AAs-e-ano-De-Ate-informado-nos-par%C3%A2metros-pois-ambos-devem-pertencer-a-per%C3%ADodos-fechados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21047511345559) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**HELP: Corrija o mês e ano De/Ate informado nos parâmetros pois ambos devem pertencer a períodos fechados  
![](https://totvssuporte.zendesk.com/attachments/token/khCagF7lw7n8D2bIN6vsEkCFq/?name=image.png)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**

A configuração da pergunta Mês ano de (MMAAAA) / Mês Ano Até (MMAAAA) possui uma competência com o período FOL aberto.   
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. A rotina de dissídio só considera o roteiro FOL  após o fechamento de períodos para tratar o cálculo do período e suas respectivas diferenças. Desta forma verifique se os períodos compreendidos na pergunta para cálculo estão fechados.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21052924145559)  
  
**IMPORTANTE:**Não serão apresentadas diferenças no cálculo de dissídio quando ocorrer apenas o roteiro 132 fechado na competência 12. A rotina valida apenas no cadastro de períodos o roteiro FOLHA como fechado. 

**Saiba Mais:**  
[Página Centralizadora do Dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
