---
article_id: 1500005596862
category: Portal de Gestão de Capital Humano
content_hash: 068b4e518b6895c344b4b73644073de03dff29316ce36917b55366fabfbbe3f4
fetched_at: '2026-06-28T22:42:59.013308+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Qual a configuração para definir o período
  de manutenção das batidas/marcações no Portal Capital Humano
type: support-article
updated_at: '2021-04-07T12:57:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005596862-RH-Linha-Protheus-PORTAL-GCH-Qual-a-configura%C3%A7%C3%A3o-para-definir-o-per%C3%ADodo-de-manuten%C3%A7%C3%A3o-das-batidas-marca%C3%A7%C3%B5es-no-Portal-Capital-Humano
---

**Dúvida**Qual a configuração para definir o período de manutenção das batidas/marcações no Portal Capital Humano (GCH)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal Gestão Capital Humano – Todas as versões  
  
**Solução**

O sistema usa os parâmetros MV\_DABERTO, MV\_PAPONTA e MV\_PONMES.

**MV\_PAPONTA** - Período para apontamento das marcações.

**MV\_PONMES** - Período de Apontamento em aberto para a apuração das marcações/apontamentos no Ponto eletrônico.

**MV\_DABERTO** - Informe a quantidade de dias corridos após o fim do período para manutenção do ponto pelos funcionários.

Exemplo prático: 

Parâmetro MV\_DABERTO = 2

Período de apontamento: 26/11/2020 à 25/12/2020

O período termina em 25/12, e serão adicionados mais 2 dias, formando uma nova data de término em 27/12. Assim, os usuários poderão fazer manutenção das marcações do período até essa data. E a partir do dia 28/12/2020 não será possível realizar nenhuma manutenção.  
  
Para mais informações de como configurar os parâmetros MV\_PAPONTA e MV\_PONMES verifique o artigo:  
[MP - PON - Período de apontamento desconfigurado. Como configurar: MV\_PAPONTA e MV\_PONMES](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015809548-MP-PON-Per%C3%ADodo-de-apontamento-desconfigurado-Como-configurar-MV-PAPONTA-e-MV-PONMES)  
  
**Saiba Mais**  
[Artigos Gestão Capital Humano](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano#)
