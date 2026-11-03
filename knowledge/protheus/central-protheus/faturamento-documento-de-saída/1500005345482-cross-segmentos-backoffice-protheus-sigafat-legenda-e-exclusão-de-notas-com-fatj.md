---
article_id: 1500005345482
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: a0d0f2a131b89fa19e80ad64721b662c5ad18808dc8fea72860a584e0e4ec63e
fetched_at: '2026-06-28T22:38:44.068197+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Legenda e exclusão de notas
  com FATJOBNFE
type: support-article
updated_at: '2024-04-29T17:02:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005345482-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Legenda-e-exclus%C3%A3o-de-notas-com-FATJOBNFE
---

**Dúvida**

O que significa as cores da Legenda de Exclusão do documento de saída?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - SIGAFAT - Todas as versões;

**Solução**

A legenda na rotina de exclusão de documento de saída (**MATA521**), só ocorre quando há o uso do Job de validação de exclusão da nota, **FATJOBNFE**, através da ativação do parâmetro **MV\_CANCNFE**, quando não há o uso do Job, não há legenda.

Sua composição é a seguinte:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007252621)

**Laranja**: Aguardando o retorno da Sefaz, sobre o cancelamento;

**Branco**: nenhuma ação tomada;

**Verde**: Cancelamento autorizado e com pendencias, avalie o status dos campos **F2\_FIMP e F2\_STATUS.**

**Vermelho**: Cancelamento não autorizado, verifique o **Campo STATUS Tabela SPED050.**

***OBSERVAÇÃO:** Caso o teste seja feito em ambiente de homologação, por ser homologação, a legenda fica "Laranja", valide se está no ambiente de produção.*

**Saiba mais:**

**[FAT0191 - Job para exclusão documento de saída (MATA521) - FATJOBNFE](https://tdn.totvs.com/x/tr44E)**
