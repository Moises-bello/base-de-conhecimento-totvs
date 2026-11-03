---
article_id: 9632614506007
category: Materiais - Compras (SIGACOM)
content_hash: 197ac5dabad8b5897f7869cb80ad50fca7400f16ac637d3075325709580f7a90
fetched_at: '2026-06-28T22:41:25.512912+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Solicitação Recebida] Cross Segmentos - Totvs Backoffice Protheus - SIGACOM
  - Invalid Macro Source
type: support-article
updated_at: '2022-10-18T17:41:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9632614506007-Solicita%C3%A7%C3%A3o-Recebida-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Invalid-Macro-Source
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02 min**

**Ocorrência**

O que fazer quando o sistema gerar erro de**invalid macro source (SSYacc0105e: Error token failed, no valid token)?**

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus-SIGACOM - Versão 12

**Causa**

A causa deste tipo de erro geralmente está relacionada a validação de usuário nos campos de estrutura sx3, exemplo **x3\_relação, x3\_pictvar, x3\_when ou x3\_inibrw**de algum campo de tabela.

Também pode estar relacionada ao cadastro de fórmulas, geralmente quando a query está incompleta.

**Solução**

1. Se os campos**x3\_relação, x3\_pictvar, x3\_when ou x3\_inibrw,**da tabela informada no erro, se há alguma informação que não esteja entre aspas duplas, ou está com aspas duplas e simples ao mesmo tempo. Para corrigir, acerte a informação colocando entre aspas duplas .

Exemplo:**"1"**;

2. Se alguma informação do tipo numérica sendo passada sem uso de aspas (" "), visto que o campos**x3\_relação, x3\_pictvar, x3\_when ou x3\_inibrw**são do tipo carácter. Para corrigir, acerte a informação colocando entre aspas duplas;

Exemplo:**"2";**

3. Se está sendo passado uma instrução ADVPL e não está fechando adequadamente parênteses, chaves e colchetes, para corrigir, acerte a expressão Advpl colocando os devidos  parênteses, chaves e colchetes que estão faltando.

**SAIBA MAIS EM :**

[PÁGINA CENTRALIZADORA DE COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
