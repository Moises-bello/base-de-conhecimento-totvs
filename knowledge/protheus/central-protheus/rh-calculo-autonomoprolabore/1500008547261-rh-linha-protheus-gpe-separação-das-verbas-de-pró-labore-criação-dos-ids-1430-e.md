---
article_id: 1500008547261
category: RH - Calculo Autonomo/Prolabore
content_hash: 9bc027280dd5bfd74d0fe86506c41032a8bfcce87ee6331d1b78acdbe0c7996d
fetched_at: '2026-06-28T22:43:15.263706+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Separação das verbas de Pró-Labore (Criação dos
  ID's 1430 e 1431)
type: support-article
updated_at: '2025-04-15T18:04:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008547261-RH-Linha-Protheus-GPE-Separa%C3%A7%C3%A3o-das-verbas-de-Pr%C3%B3-Labore-Cria%C3%A7%C3%A3o-dos-ID-s-1430-e-1431
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25676267657751)**Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Separação das verbas de pro-labore por categoria do eSocial.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Causa**  
Sistema não permite a distinção de rubrica dos pró-labores pois gera o pagamento na mesma verba de cálculo.  
  
**Solução**Ajuste para efetuar separação das verbas na geração do pagamento de pró-labore (categoria **P**), conforme categoria do eSocial:

- Categoria eSocial **721** ou categoria **em branco** ou outras categorias diferente de **722** e **723**: gravação no ID de cálculo**0217 - Pro-Labore**;

- Categoria eSocial **722**: gravação no código do ID de cálculo **1430 - Pro-Labore - Diretores não empregados.**Para facilitar o cadastro, copiar a configuração da verba de ID de cálculo **0217**;

- Categoria eSocial **723**: gravação no código de ID de cálculo **1431** **- Pro-Labore - Proprietários ou sócios**. Para facilitar o cadastro, copiar a configuração da verba de ID de cálculo **0217**.

**Saiba Mais:**

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
