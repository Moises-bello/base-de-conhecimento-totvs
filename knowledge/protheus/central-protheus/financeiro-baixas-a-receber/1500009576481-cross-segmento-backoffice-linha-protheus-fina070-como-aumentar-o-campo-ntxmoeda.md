---
article_id: 1500009576481
category: Financeiro - Baixas a Receber
content_hash: e11f36786f1b581ff7d5bd369629571a85c7cc205ae254184038ecaf5f7253a2
fetched_at: '2026-06-28T22:37:43.678499+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - FINA070 - Como Aumentar o campo
  NTXMOEDA '
type: support-article
updated_at: '2025-07-30T15:01:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009576481-Cross-Segmento-Backoffice-Linha-Protheus-FINA070-Como-Aumentar-o-campo-NTXMOEDA
---

**Dúvida**Como Aumentar o campo **NTXMOEDA** na rotina **FINA070** ?  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus – Financeiro – A partir da versão 17  
  
**Solução**Para aumentar o tamanho das casas decimais da variável **NTXMOEDA**, é necessário realizar a alteração na tabela **SM2**, aumente o tamanho das casas decimais via **SIGACFG** (Configurador) dos campos de moeda 1,2,3 (**M2\_MOEDA2**) e etc... , a variável assumirá a mesma configuração. Também é necessário realizar os ajustes nas tabelas **SE1**, **SE2**, **SE5**, e **FK's**, nos campos que compõe a taxa da moeda.

![](https://totvssuporte.zendesk.com/attachments/token/xAtCc9XvYtTEnyXg775x7E3IO/?name=inline-209068158.png)
