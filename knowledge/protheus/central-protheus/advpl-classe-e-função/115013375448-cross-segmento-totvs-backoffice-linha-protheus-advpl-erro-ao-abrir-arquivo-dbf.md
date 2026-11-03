---
article_id: 115013375448
category: ADVPL - Classe e Função
content_hash: 40bf12088445b8cf002858148e9fe8f567de76845a4afc26abc00307261c9b2e
fetched_at: '2026-06-28T22:40:14.141934+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro ao abrir
  arquivo DBF
type: support-article
updated_at: '2021-09-01T12:52:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115013375448-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-ao-abrir-arquivo-DBF
---

**Dúvida**Erro ao abrir arquivo **DBF** "Open - Ctree Error 13 - IO Error: 0 - Unknown file type" como corrigir?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**

A versão P12 não suporta dbf  
[Migração de Versão - Para Protheus 12](https://tdn.totvs.com/pages/releaseview.action?pageId=271659404)  
  
Para ctree não temos nenhuma função especifica para converter arquivos dbf em ctree. Nesse caso será necessário utilizar o apsdu, não temos funções especificas para manipulação de arquivo ctree.  
As funções que tratam arquivos dbf são compatíveis como o ctree.  
  
Segue lista de funções para manipulação de tabelas de dados.  
[Funções genéricas](https://tdn.totvs.com/pages/viewpage.action?pageId=6063423)  
  
**Saiba mais**  
[ADV0039 Fun. DBF](http://tdn.totvs.com/display/PROT/ADV0039_FUN_DBF)
