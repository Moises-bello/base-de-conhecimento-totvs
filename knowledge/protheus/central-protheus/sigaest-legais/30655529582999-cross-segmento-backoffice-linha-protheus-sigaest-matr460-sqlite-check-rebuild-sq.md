---
article_id: 30655529582999
category: SIGAEST - LEGAIS
content_hash: 655b70989e11417106959014a4da30c34dbf7cdc82699ff6fea3d4824a148c08
fetched_at: '2026-06-28T22:38:51.588928+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  MATR460 [SQLITE]
  **** Check / Rebuild SQLITE Tables FAILED
type: support-article
updated_at: '2025-07-15T10:58:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30655529582999-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-SQLITE-Check-Rebuild-SQLITE-Tables-FAILED
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30655529569687) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao executar o MATR460 o sistema retorna o erro **[SQLITE] \*\*\*\* Check / Rebuild SQLITE Tables FAILED \*\*\*'.** **in file C:**, como corrrigir?  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**Este erro ocorre quando a tabela é criada sem o recurso do COLLATE RTRIM quando está com os artefatos mais recentes do Harpia.  
  
**Solução**Para solucionar basta, configurar as chaves abaixo na seção [General] no appserver.ini:  
   
***SQLITE\_RebuildTables=0***  
***SQLite\_CollateRTRIM=0***  
***SQLite\_TrailSpace=1***  
   
*Documentação sobre a comparação de strings no SQLite e sobre cada chave acima:*  
[***https://tdn.totvs.com/pages/viewpage.action?pageId=664017473***](https://tdn.totvs.com/pages/viewpage.action?pageId=664017473)  
  
Após isso tente gerar o MATR460 novamente!

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre arquivos e relatórios Legais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
