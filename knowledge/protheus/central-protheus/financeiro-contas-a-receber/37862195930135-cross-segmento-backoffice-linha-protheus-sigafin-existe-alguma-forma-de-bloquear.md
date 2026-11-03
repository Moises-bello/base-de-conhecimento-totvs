---
article_id: 37862195930135
category: Financeiro - Contas a Receber
content_hash: 5f0f4a19509db6dbd4a02e416250ae7dc23ed46d3173b0d3f9841447a2a05a73
fetched_at: '2026-06-28T22:38:12.493578+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Existe alguma forma
  de bloquear movimentos contabilizados
type: support-article
updated_at: '2026-01-23T16:24:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37862195930135-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Existe-alguma-forma-de-bloquear-movimentos-contabilizados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37862195889687) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Existe alguma forma de bloquear movimentos contabilizados?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Por padrão, no módulo Financeiro, o sistema não possui parâmetro específico ou ponto de entrada destinado ao bloqueio de títulos contabilizados.

As rotinas de Contas a Receber e Contas a Pagar (FINA040 e FINA050), responsáveis pelas operações de inclusão, exclusão e alteração de títulos, utilizam parâmetros específicos para controle das movimentações financeiras.

O parâmetro **MV\_DATAFIN** define a data a partir da qual as movimentações financeiras passam a ser permitidas no sistema.

**Por sua vez**, o parâmetro **MV\_BXDTFIN** determina se as operações de baixa de títulos a pagar e a receber devem considerar a data configurada no parâmetro **MV\_DATAFIN**.

[Cross Segmentos - Backoffice Linha Protheus - HELP - DTMOVFIN e utilização dos parâmetros MV\_DATAFIN e MV\_BXDTFIN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020859271-Cross-Segmentos-Backoffice-Linha-Protheus-HELP-DTMOVFIN-e-utiliza%C3%A7%C3%A3o-dos-par%C3%A2metros-MV-DATAFIN-e-MV-BXDTFIN)

Outra alternativa de bloqueio por processo é o **bloqueio contábil**, disponível na documentação:  
[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA010 - Como funciona a funcionalidade - Bloqueio por Processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035066073-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA010-Como-funciona-a-funcionalidade-Bloqueio-por-Processo)
