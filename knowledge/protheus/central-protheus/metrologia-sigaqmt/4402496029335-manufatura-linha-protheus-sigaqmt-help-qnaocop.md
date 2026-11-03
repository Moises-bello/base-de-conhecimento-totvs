---
article_id: 4402496029335
category: Metrologia (SIGAQMT)
content_hash: 973952539dd4df54e6ad62f5214c69b0bb3fb5ddf36c59e1b9be7a872b2b1fdb
fetched_at: '2026-06-28T22:42:24.795405+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - Help QNAOCOP
type: support-article
updated_at: '2021-06-11T20:02:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402496029335-Manufatura-Linha-Protheus-SIGAQMT-Help-QNAOCOP
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:00:00 min**  
**Ocorrência**Nas rotinas do módulo **SIGAQMT - Metrologia**, ao incluir um documento anexo, ocorre o *Help* **QNAOCOP - Não foi possível copiar o Documento Anexo**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Causa**O *Help* **QNAOCOP** ocorre quando há divergência entre o diretório destino do documento anexado e o conteúdo do parâmetro **MV\_QMTPATH - Indica o diretório de gravação de documentos do ambiente Metrologia**.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Valide o conteúdo do parâmetro **MV\_QMTPATH**. No padrão este conteúdo é **\SYSTEM\DOCS\**.  
2. Confirme se o documento que está anexado, está dentro do diretório indicado no parâmetro.  
  
**Observação**  
Quando o conteúdo do parâmetro **MV\_QMTPATH** for alterado, os documentos que já foram anexados, deverão ser copiados do diretório original para o novo diretório informado no parâmetro. A não observância desta regra ocasionará o *help* **QNAOCOP**.
