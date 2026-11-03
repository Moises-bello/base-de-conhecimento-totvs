---
article_id: 4409539481367
category: RH - Relatórios Folha
content_hash: 1dcebbe944959b8139040f7168480b82f31a38bceab60901b7400a4751613a3a
fetched_at: '2026-06-28T22:43:17.496619+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - Conceito dos totalizadores de situação do relatório
  da folha de pagamento (GPER040)
type: support-article
updated_at: '2024-08-23T01:22:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409539481367-RH-Linha-Protheus-GPE-Conceito-dos-totalizadores-de-situa%C3%A7%C3%A3o-do-relat%C3%B3rio-da-folha-de-pagamento-GPER040
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25840957358231) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Conceito dos totalizadores de situação do relatório da folha de pagamento (GPER040).  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**

#### **01. VISÃO GERAL**

Apresentamos aqui o conceito de cada indicador gerado no totalizador do relatório da folha de pagamento GPER040.

#### **02. EXPLICAÇÃO**

| Totalizador | Objetivo |
| --- | --- |
| Sit. Normal | Indica a quantidade de funcionários com situação em branco de folha, ou seja, sem afastamento e sem demissão (através da verificação do campo RA\_SITFOLH em branco). |
| Admitidos | Indica a quantidade de funcionário admitidos após o início do período selecionado (através da verificação do campo RA\_ADMISSA). |
| Afastados | Indica a quantidade de funcionários afastados, ou seja, com situação "A" de folha (através da verificação do campo RA\_SITFOLH preenchido com A). |
| Demitidos | Indica a quantidade de funcionários demitidos, ou seja, com situação "D" de folha (através da verificação do campo RA\_SITFOLH preenchido com D). |
| Férias | Indica a quantidade de funcionários em férias, ou seja, com situação "F" de folha (através da verificação do campo RA\_SITFOLH preenchido com F). |
| Transferidos | Indica a quantidade de funcionários transferidos de filial ou empresa, ou seja, com situação "T" de folha (através da verificação do campo RA\_SITFOLH preenchido com T).  **Obs.**: indicador legado. |
| Outros C.Custo | Indica a quantidade de centros de custo diferente do centro de custo do cadastro do funcionário.  Por exemplo, funcionário no centro de custo A com lançamento no centro de custo B será gerado 1 nesse indicador. Se houver dois funcionários com essa situação, então será gerado 2 no indicador. **Obs.**: indicador apenas será gerado quando o relatório for impresso na ordem de Centro de Custo do Movimento. |
| Inativos | Indica a quantidade de funcionários inativos, ou seja, com situação "I" de folha (através da verificação do campo RA\_SITFOLH preenchido com I).  **Obs.**: indicador apenas para ambiente de gestão pública - SIGAGSP. |
| Total | Somatória das ocorrências dos indicadores acima. |

**Saiba mais:**

[RH - Relatórios Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)
