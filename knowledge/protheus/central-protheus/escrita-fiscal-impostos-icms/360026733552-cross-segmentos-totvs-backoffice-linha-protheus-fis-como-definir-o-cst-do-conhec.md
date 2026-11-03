---
article_id: 360026733552
category: Escrita Fiscal - Impostos - ICMS
content_hash: 8db9d87222d1882f71822e42608fae3bc9ccd313f6af41ac59ae74044bf120ae
fetched_at: '2026-06-28T22:39:24.180735+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como definir o CST
  do conhecimento de frete?
type: support-article
updated_at: '2021-07-28T02:21:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026733552-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-definir-o-CST-do-conhecimento-de-frete
---

**Dúvida**Como Definir se o CST do Conhecimento de Frete será considerado pelo B1\_ORIGEM ou ou se iniciará em 0 (zero) mesmo sendo uma importação ?  
  
**Ambiente**Protheus - a partir 11.8  
  
**Solução**Configurar:

MV\_STFRETE = .T. - Para notas fiscais de serviço onde o primeiro caractere do código do Cód da Sit Trib (CST\_ICMS) deverá ser igual a 0 (zero).

Importante  
Efetuada a criação do parâmetro MV\_STFRETE para definir se o campo Cód.Situação Tributária das notas de conhecimento de frete é considerado do Cadastro de Produtos, campoOrigem (B1\_ORIGEM), ou se iniciará em 0 (zero) mesmo sendo uma importação.
