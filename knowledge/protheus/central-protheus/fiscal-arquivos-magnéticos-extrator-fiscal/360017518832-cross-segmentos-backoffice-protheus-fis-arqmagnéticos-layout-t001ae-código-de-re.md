---
article_id: 360017518832
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: b42c77e2336607f65bd312e43777f8565d9cb6d2e86bc3fe1dbc6555108a9e9f
fetched_at: '2026-06-28T22:42:07.827385+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T001AE
  Código de Receita C0R_CODREC inexistente
type: support-article
updated_at: '2022-08-18T17:34:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017518832-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T001AE-C%C3%B3digo-de-Receita-C0R-CODREC-inexistente
---

**Ocorrência**Erro 1 - Linha: 1 - O valor 0462 informado na coluna 5 para o campo Código da Receita (C0R\_CODREC) não existe na base de dados.   
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, pois o código de receita utilizado esta incorreto, logo não existe na tabela autocontida**C6R (Receitas Para Doc. Arrecadação)**. O código correto é: **"046-2", "Regime Periódico de Apuração"**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Ajuste o código de receita informado para a GNRE;  
2. Execute o Extrator Fiscal selecionando o **Layout T001AE** novamente;  
3. Efetue o Processamento para que o dado seja integrado ao TAF.
