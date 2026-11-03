---
article_id: 22179822067479
category: Controle de Documentos (SIGAQDO)
content_hash: f0e5a205f65bbaa50c55f2ca6ae81f57eb65e46f1f313915f0e83926d87a4357
fetched_at: '2026-06-28T22:42:29.162348+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help QDOENVIMPR1 ao imprimir documento
type: support-article
updated_at: '2025-07-15T13:50:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22179822067479-Manufatura-Linha-Protheus-SIGAQDO-Help-QDOENVIMPR1-ao-imprimir-documento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22179867233687) Tempo aproximado para leitura: **00:00:45 min****Ocorrência**No módulo **SIGAQDO - Controle de Documentos** ao tentar imprimir um documento ocorre o *help* **QDOENVIMPR1 - Impressão não habilitada na etapa de leitura do documento**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**O *help* **QDOENVIMPR1** é exibido porque, no Padrão, não é permitido imprimir um documento em *PDF*, quando o documento está em fase de leitura.  
  
**Solução**  
Para permitir a impressão em *PDF* de documento em fase de leitura é necessário a utilização do **PE -** **Ponto de Entrada** [QDOLPDFIMP - Ponto de Entrada para permitir ou não a impressão do documento pelo usuário corrente na etapa atual](https://tdn.totvs.com/pages/releaseview.action?pageId=708876888)**.**  
Quando usado este **PE**, o **Sistema** não exibe o *Help* que indica que o usuário atual não tem permissão para imprimir o documento, sendo possível/necessário, a implementação de uma mensagem customizada.
