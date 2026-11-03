---
article_id: 4421902992279
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 4367ad59e703416b7dbf41d7ca6bd519e506b2dba4f5caea2871c1c6046d01b8
fetched_at: '2026-06-28T22:38:43.925261+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Utilizar a mesma
  série com espécies diferentes no Documento de Saída
type: support-article
updated_at: '2022-02-07T16:43:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421902992279-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Utilizar-a-mesma-s%C3%A9rie-com-esp%C3%A9cies-diferentes-no-Documento-de-Sa%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como utilizar a mesma série em espécies diferentes no Documento de Saída?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**No padrão do sistema não é possível utilizar a mesma série com espécies diferentes, o sistema não valida a espécie na geração do documento de saída.

Para que o sistema permita e não gere erro na emissão do documento de saída, adicione um zero à esquerda no número da nova série.

**Exemplo:**

Série existente = 1

Nova série = 01 --> Adicionando um zero à esquerda

**Saiba Mais:** [Criação de série de NFs para utilizar em Documentos de Saída](https://tdn.totvs.com/x/WU1tDQ)
