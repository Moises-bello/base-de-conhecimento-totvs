---
article_id: 14823862934807
category: TAF - REINF
content_hash: 5dbd9d19a3e3ae99dd12c31d63794ab8d8df27c12a20c39e52967741158c6fb7
fetched_at: '2026-06-28T22:41:33.748845+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como integrar o evento
  R-4080  manualmente no TAF.
type: support-article
updated_at: '2023-05-31T12:18:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14823862934807-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-integrar-o-evento-R-4080-manualmente-no-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00****min****Dúvida**Como gerar o evento R4080 manualmente no TAF  ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - a partir da versão 12.  
  
**Solução**O evento R4080  é relacionado  a retenção no recebimento.

Para incluir de forma manual no TAF acesse esse caminho: **Atualizações > Movimentos Reinf >  Retenção Recebimento/beneficiário Não identificado (TAFA542) > Incluir**

Campos relacionados:

Natureza da Fatura **(V4K\_INDNAT**): 1 - A receber

Código do Participante (**V4K\_CODPAR**)

Natureza de Rendimento (**V4K\_CODNAT**): Utilizar natureza de rendimento do grupo 20

Data Pagamento (**V4K\_DTPAG**): O mês/ano selecionado para apuração deve corresponder ao mês/ano de competência do pagamento.

Processos Referenciados (quando aplicável)

Id. Processo(**V9B\_IDPROC**): O ID do processo referenciado;

Suspensão (**V9B\_CODSUS**): O código da exigibilidade suspensa;

Segue o  exemplo:

![4080.png](https://centraldeatendimento.totvs.com/hc/article_attachments/14823372438295)

Após a apuração  no painel Reinf,  o evento pode ser acessado através do menu:

**Eventos REINF > Periódicos >  R-4080 - Retenção no Recebimento.**

As tabelas envolvidas para esse evento são:

V97 – R-4080 - Retenção Recebimento

V98 – R4080 Identificação Rendimento

V99 – R4080 Informação relativa rendimento

V9A – R4080 Informação Processo Referenciado
