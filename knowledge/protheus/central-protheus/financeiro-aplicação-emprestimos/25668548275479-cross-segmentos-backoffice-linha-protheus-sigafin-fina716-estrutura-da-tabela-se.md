---
article_id: 25668548275479
category: Financeiro - Aplicação / Emprestimos
content_hash: 6b7ed473573eea731f5e3dca2fdf3f013084ab7475e7205f044d08888ed508cb
fetched_at: '2026-06-28T22:37:59.521608+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA716 - Estrutura
  da tabela SEI
type: support-article
updated_at: '2024-08-15T18:00:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25668548275479-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA716-Estrutura-da-tabela-SEI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25668503578647) Tempo aproximado para leitura: **02:00 min** **Dúvida**Qual é a estrutura da tabela SEI (FINA716)?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**

Segue abaixo a estrutura de movimentações da tabela **SEI**.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Passo a passo:** | | Tipo Movimentação  EI\_APLEMP | Tipo Documento  EI\_TIPODOC | Motivo  EI\_MOTBX | Item Lancto Modulo  PCO INCLUSAO | Item Lancto Modulo  PCO CANCELAMENTO | Descritivo do Item | | --- | --- | --- | --- | --- | --- | | APL | BP | NOR | 02 | 16 | Baixa Valor do Principal | | APL | I1 | NOR | 05 | 19 | Valor do IRRF | | APL | I1 | APR | 11 | 25 | Apropriação IRF | | APL | I2 | NOR | 06 | 20 | Valor do IOF | | APL | I2 | APR | 12 | 26 | Apropriação do IOF | | APL | I3 | NOR | 08 | 22 | Valor do IRRF s/SWAP | | APL | I3 | APR | 13 | 27 | Apropriação do IRF s/SWAP | | APL | I4 | NOR | 09 | 23 | Valor de Despesas | | APL | I4 | APR | 14 | 28 | Apropriação de despesas | | APL | I6 | APR | 02 | 04 | Valor do IR (inclusao) | | APL | I7 | APR | 03 | 05 | Valor do Rendimento na Retencao IR | | APL | JR | NOR | 03 | 17 | Valor dos Juros | | APL | JR | APR | 15 | 29 | Apropriação dos juros | | APL | RG | NOR | 04 | 18 | Baixa do Valor do Resgate | | APL | SW | NOR | 07 | 21 | Valor do SWAP | | APL | VL | NOR | 10 | 24 | Valor do crédito |  | Tipo Movimentação  EI\_APLEMP | Tipo Documento  EI\_TIPODOC | Motivo  EI\_MOTBX | Item Lancto Modulo  PCO INCLUSAO | Item Lancto Modulo  PCO CANCELAMENTO | Descritivo do Item | | --- | --- | --- | --- | --- | --- | | EMP | JR | NOR | 31 | 46 | Valor dos Juros | | EMP | V1 | NOR | 32 | 47 | Variação cambial a Longo Prazo | | EMP | V2 | NOR | 33 | 48 | Variação cambial a curto Prazo | | EMP | V3 | NOR | 34 | 49 | Variação cambial dos juros | | EMP | BL | NOR | 35 | 50 | Baixa do Longo Prazo | | EMP | BC | NOR | 36 | 51 | Baixa do Curto Prazo | | EMP | BJ | NOR | 37 | 52 | Baixa do Juro | | EMP | I1 | NOR | 38 | 53 | Pagamento do Valor do IRF | | EMP | I2 | NOR |  |  | Valor do IOF | | EMP | I4 | NOR | 39 | 54 | Pagamento das Despesas | | EMP | I5 | NOR | 40 | 55 | Pagamento do GAP | | EMP | VL | NOR | 41 | 56 | Valor do débito | | EMP | JR | APR | 42 | 57 | Apropriação dos Juros | | EMP | V1 | APR | 43 | 58 | Apropriação da variação cambial a Longo Prazo | | EMP | V2 | APR | 44 | 59 | Apropriação da variação cambial a Curto Prazo | | EMP | V3 | APR | 45 | 60 | Apropriação da variação cambial dos Juros | |
