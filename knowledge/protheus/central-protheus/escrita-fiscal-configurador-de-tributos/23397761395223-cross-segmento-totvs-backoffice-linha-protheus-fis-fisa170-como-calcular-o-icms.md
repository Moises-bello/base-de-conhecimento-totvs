---
article_id: 23397761395223
category: Escrita Fiscal - Configurador de Tributos
content_hash: 5f62eab51f5b856fe22857147cf2b393f564dd7e558474a82718dd2f01e061b0
fetched_at: '2026-06-28T22:39:17.364468+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como calcular
  o ICMS próprio em operações de entrada e saída?
type: support-article
updated_at: '2025-11-03T17:12:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23397761395223-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-o-ICMS-pr%C3%B3prio-em-opera%C3%A7%C3%B5es-de-entrada-e-sa%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23397761345175) Tempo aproximado para leitura: **00****:05:00min** **Dúvida**Como calcular o ICMS próprio em operações de entrada e saída?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

**Parâmetro**

MV\_ESTADO= SP

**Cliente**

UF= MG

Tipo cliente= Solidário

**Fornecedor**

UF= SP

Tipo cliente= Solidário

**TES**

Cod. Fiscal = Conforme necessidade da empresa

Para calculo dos impostos no Configurador de Tributos a única validação realizada dentro do MATA080 - Tipo de entrada e saída é o CFOP.

Acesse a rotina do FISA170 - Configurador de Tributos - Regras Fiscais > Tributo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23397761346583)

Regras Fiscais > Perfis

Perfil de Produto

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23397750172183)

Perfil de Participante

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23397761352599)

Regras de Calculo Documento Fiscal > Regra de Base de Calculo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23397750176407)

Regra de Alíquota

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23397761360023)

Regra de Escrituração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23397750180247)

Regra de Calculo - Documentos Fiscais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23397761362839)

Lançamento do pedido de venda (MATA410)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23397750185623)

Lançamento do documento de entrada (MATA103)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23397750187287)
