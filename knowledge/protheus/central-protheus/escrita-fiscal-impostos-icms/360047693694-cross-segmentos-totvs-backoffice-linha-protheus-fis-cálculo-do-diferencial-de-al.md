---
article_id: 360047693694
category: Escrita Fiscal - Impostos - ICMS
content_hash: a922da174cd89651838701124d0d2d0612bc8b0c1102ec11254139b925bfff83
fetched_at: '2026-06-28T22:39:24.351523+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Cálculo do diferencial
  de alíquota (ICMS-ST) em operações de saída para cliente Contribuinte
type: support-article
updated_at: '2021-07-20T14:26:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047693694-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-do-diferencial-de-al%C3%ADquota-ICMS-ST-em-opera%C3%A7%C3%B5es-de-sa%C3%ADda-para-cliente-Contribuinte
---

**Dúvida**Como Calcular na saída o diferencial de alíquota para Cliente Contribuinte?  
   
 **Ambiente**

Protheus- Todas as versões.  
   
**Solução**Informar o percentual de ICMS-ST (MVA) estabelecido por norma legal, no cadastro de produto( solid.saida) ou exceção fiscal (margem de lucro), caso não exista essa margem de lucro, deve informar um percentual fictício (por exemplo 0,01) somente para possibilitar o cálculo pelo diferencial:

**TES**

**Calcula ICMS**(F4\_ICM) = SIM

**L. FISC. ICMS** (F4\_LFICM) = TRIBUTADO

**Calc Dif ICM**. (F4\_COMPL) = NÃO

**MATL CONSUMO** (F4\_CONSUMO) = SIM

**AGREGA SOLID.** (F4\_INCSOL) = SIM

**MKP.ICM.COMP** (F4\_MKPCMP) = NÃO

**Marg Solid** = Nunca

**CLIENTE**

- Deve ter o tipo do preenchido no parâmetro: **MV\_TPSOLCF**

- Deve ser de um Estado diferente do emitente ( MV\_ESTADO)

- Deve ter a inscrição estadual preenchida no cadastro

- Contribuinte = Sim

Para tratar base dupla, deverá configurar o parâmetro **MV\_UFBDST**informando os estados que devem realizar esse cálculo de base dupla para o ICMS-ST , o tipo do cliente deve constar no cadastro como **Consumidor Final.**
