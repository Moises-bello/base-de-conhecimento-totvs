---
article_id: 360018684912
category: Escrita Fiscal - Impostos - ICMS
content_hash: eb0bb3fb048f408e3935131c7fb2fce6450ce1243387d1e817063a13fcc273d8
fetched_at: '2026-06-28T22:39:24.230368+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - IVA Ajustado
type: support-article
updated_at: '2021-07-28T02:33:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018684912-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-IVA-Ajustado
---

**Dúvida** **Como Calcular o IVA Ajustado?**

**Ambiente**Protheus - Sigafis – A partir da versão 12.1.17  
  
  
**Solução**

Configurar no cadastro do Produto:

B1\_IVAAJU = Sim

A Margem de Lucro Original deve ser informada no cadastro do Produto Campo: Solid Saída.

\*\*\* Sistema  fará o cálculo do IVA Ajustado configurando a Margem de Lucro Original no cadastro do produto: Campos: Solid Saída ou Solid Entrada. Configurando a margem de Lucro na Exceção fiscal, o IVA Ajustado não será calculado. \*\*\*

TES:

Calcula ICMS = Sim

L. Fiscal ICMS = Diferente de Não

Mkp ICM Comp = Não

Marg. Solid = Configuração

Parâmetro:

MV\_FISXMVA = .T.
