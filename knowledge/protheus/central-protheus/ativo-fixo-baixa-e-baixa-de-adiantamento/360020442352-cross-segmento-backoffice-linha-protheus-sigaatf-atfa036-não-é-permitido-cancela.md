---
article_id: 360020442352
category: Ativo Fixo - Baixa e Baixa de Adiantamento
content_hash: 60b744c220ad6efb16e0b186d225d8f8665bbfdfd624ea10d5452f22b43e64b9
fetched_at: '2026-06-28T22:41:55.543460+00:00'
product: protheus
section_id: 1500001535901
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA036 Não é permitido
  cancelar a baixa de um ativo HELP:AF036EXCNF
type: support-article
updated_at: '2021-09-14T16:46:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020442352-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA036-N%C3%A3o-%C3%A9-permitido-cancelar-a-baixa-de-um-ativo-HELP-AF036EXCNF
---

**Ocorrência**Não é permitido cancelar a baixa de um ativo HELP:AF036EXCNF

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020309192/mceclip1.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020174911/mceclip0.png)

**Ambiente**Cross Segmento - Backoffice Linha Protheus – Ativo Fixo – A partir da versão 11.80  
  
**Causa**Quando um bem é baixado pelo motivo de venda e essa venda deu origem a uma nota fiscal de saída. O cancelamento dessa baixa passa por uma validação devido ao vínculo com a NF de Saída.

**Solução**

Parâmetro MV\_ATFVLNF= .T.

Habilita (.T.) ou Desabilita (.F.) a validação da existência da nota fiscal na tabela SF2 no cancelamento da baixa do ativo.

Importante! Por default o parâmetro vem habilitado.

O controle sobre a validação do cancelamento de nota versus o vínculo com o ativo fixo deve ser analisado pelo responsável fiscal/contador.
