---
article_id: 360028516572
category: Materiais - Compras (SIGACOM)
content_hash: d4c00201e7076b32aaa527b1a39211a4614a28e7fb9e18008fd92288b28c035e
fetched_at: '2026-06-28T22:41:16.123744+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como visualizar PIS
  e COFINS de Retenção no Pedido de Compras ?
type: support-article
updated_at: '2022-05-16T21:26:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028516572-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-visualizar-PIS-e-COFINS-de-Reten%C3%A7%C3%A3o-no-Pedido-de-Compras
---

**Dúvida**Como visualizar PIS e COFINS de Retenção no Pedido de Compras ?  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80]  
  
**Solução**

Os campos de **PIS** e **COFINS** de Retenção são necessários ser adicionados manualmente para ser possível visualizar.

Adicionar Campos e "Valids" dos Campos:

* ## **PIS**

1. Criar o Campo **C7\_BASEPIS**

1. **Tipo:** 2 - Numérico
2. **Tamanho:** 14
3. **Decimal:** 2
4. **Contexto:** 1 - Real
5. **Propriedade:**1 - Alterar
6. **X3\_VALID**: MaFisRef("IT\_BASEPIS","MT120",M->C7\_BASEPIS)

2. Criar o Campo **C7\_ALIQPIS**

1. **Tipo**: 2 - Numérico
2. **Tamanho**: 5
3. **Decimal**: 2
4. **Contexto**: 1 - Real
5. **Propriedade**: 1 - Alterar
6. **X3\_VALID**: MaFisRef("IT\_ALIQPIS","MT120",M→C7\_ALIQPIS)

3. Criar Campo **C7\_VALPIS**

1. **Tipo:** 2 - Numérico
2. **Tamanho:** 14
3. **Decimal:** 2
4. **Contexto:** 1 - Real
5. **Propriedade:**1 - Alterar
6. **X3\_VALID**: MaFisRef("IT\_VALPIS","MT120",M→C7\_VALPIS)

* ## **COFINS**

1. Criar o Campo**C7\_BASECOF**

1. **Tipo:** 2 - Numérico
2. **Tamanho:** 14
3. **Decimal:** 2
4. **Contexto:** 1 - Real
5. **Propriedade:**1 - Alterar
6. **X3\_VALID**: MaFisRef("IT\_BASECOF","MT120",M->C7\_BASEPIS)

2. Criar o Campo**C7\_ALIQCOF**

1. **Tipo**: 2 - Numérico
2. **Tamanho**: 5
3. **Decimal**: 2
4. **Contexto**: 1 - Real
5. **Propriedade**: 1 - Alterar
6. **X3\_VALID**: MaFisRef("IT\_ALIQCOF","MT120",M→C7\_ALIQCOF)

3. Criar Campo **C7\_VALCOF**

1. **Tipo:** 2 - Numérico
2. **Tamanho:** 14
3. **Decimal:** 2
4. **Contexto:** 1 - Real
5. **Propriedade:**1 - Alterar
6. **X3\_VALID**: MaFisRef("IT\_VALCOF","MT120",M->C7\_VALCOF)

***Saiba Mais :***

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
