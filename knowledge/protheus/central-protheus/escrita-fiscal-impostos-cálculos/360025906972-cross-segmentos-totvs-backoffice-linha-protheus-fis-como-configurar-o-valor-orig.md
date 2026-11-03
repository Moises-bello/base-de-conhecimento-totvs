---
article_id: 360025906972
category: Escrita Fiscal - Impostos - Cálculos
content_hash: d4bbe80a48f159964cc4f54a9e3c6a2920dc21fd1a4c72ffc2db1ff2d8998023
fetched_at: '2026-06-28T22:39:30.672039+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como configurar o
  valor original do bem na classificação do ativo quando a nota é lançada pelo compras? '
type: support-article
updated_at: '2021-07-29T13:59:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025906972-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-valor-original-do-bem-na-classifica%C3%A7%C3%A3o-do-ativo-quando-a-nota-%C3%A9-lan%C3%A7ada-pelo-compras
---

**Dúvida**

Como configurar o valor original do bem na classificação do ativo quando a nota é lançada pelo compras?

**Ambiente**

Protheus - Compras - a partir da 11.80  
   
**Solução**

 A expressão de cálculo considerada para compor o valor do Bem no módulo Ativo Fixo quando há integração do módulo de compras através de Documento de entrada deverá ser configurado no parâmetro MV\_VLRATF.

A rotina FISXATF.PRW contém uma chamada de leitura ao conteúdo deste parâmetro, e aplica uma expressão padrão (Brasil) caso não exista um valor ou expressão configurada no parâmetro,

 Conteúdo da rotina FISXATF.PRW:

(SD1->D1\_TOTAL-SD1->D1\_VALDESC)+If(SF4->F4\_CREDIPI=="S",0,SD1->D1\_VALIPI)-IIf(SF4->F4\_CREDICM=="S",SD1->D1\_VALICM,0)

 Conteúdo do Dicionário SX6:

MV\_VLRATF = (SD1->D1\_TOTAL-SD1->D1\_VALDESC)+If(SF4->F4\_CREDIPI=="S",0,SD1->D1\_VALIPI)-IIf(SF4->F4\_CREDICM=="S",SD1->D1\_VALICM,0)

Nesse parâmetro contém expressão que deverá ser alterada conforme a necessidade do cliente.
