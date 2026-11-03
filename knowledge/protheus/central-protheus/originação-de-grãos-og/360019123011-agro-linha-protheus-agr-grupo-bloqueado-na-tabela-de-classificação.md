---
article_id: 360019123011
category: Originação de Grãos (OG)
content_hash: 7ae280bba1880164ad145034ae6d4c9e64a939de4d19e271a8ac7d3925ac9491
fetched_at: '2026-06-28T22:45:39.587068+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Grupo bloqueado na tabela de classificação
type: support-article
updated_at: '2025-04-09T19:40:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019123011-Agro-Linha-Protheus-AGR-Grupo-bloqueado-na-tabela-de-classifica%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20354869755927)*** Tempo aproximado para leitura: **00:00:30 min  
  
Dúvida**Ao incluir um registro no **AGRA035 -****Tabela de Classificação** o campo **Grupo** aparece bloqueado, mas é necessário usar o **Grupo de Produto** no cadastro. Como fazer para que o campo **Grupo** seja desbloqueado?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Para que o campo **Grupo** seja desbloqueado é necessário acessar o parâmetro **MV\_AGRDES** e alterar o conteúdo. Ao preencher o parâmetro **MV\_AGRDES** com o conteúdo **1**, o código do produto torna-se obrigatório no cadastro da **Tabela de Classificação** e o campo **Grupo é Bloqueado**. Ao informar o conteúdo **2** no parâmetro, o código do produto não é obrigatório e o campo **Grupo é Desbloqueado**.
