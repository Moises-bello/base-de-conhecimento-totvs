---
article_id: 360047549334
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 0bb67625394dea6ad8945d234fa53290bd3ff50536f6bb507c442cb15579e4ef
fetched_at: '2026-06-28T22:39:30.456700+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como aumentar o
  tamanho do campo MVA ? '
type: support-article
updated_at: '2021-07-29T13:43:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047549334--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-aumentar-o-tamanho-do-campo-MVA
---

**Dúvida** **Como aumentar o tamanho do campo MVA ?**  
  
   
 **Ambiente**Protheus - Fiscal - A partir da versão 11.80  
  
**Solução**

Aumentar as Casas Decimais da Margem de Lucro (MVA-ICMS ST)

Para que o sistema atenda sua solicitação, deverá aumentar a margem de lucro até atingir o valor desejado. Como o campo suporta somente 99,99 deverá aumentar no configurador:

SIGACFG: Base de Dados->Dicionário de Dados->Base de Dados e localizar o tamanho dos campos referente a Margem de lucro abaixo:

D2\_MARGEM, D1\_MARGEM, FT\_MARGEM, F7\_MARGEM, CD2\_MVA, B1\_PICMRET, B1\_PICMENT

Nas respectivas Tabelas:

SD2, SD1, SFT, SF7, CD2 e SB1

* Exemplo:

**Campo**: F7\_MARGEM

**Tamanho Original**: 05, (Altere para a quantidade desejada)

**Decimal**: 04 (Ou alterar para quantidade desejada)

**Formato original**: @E 99.99, (Exemplo: Altere para @E 999.99)

Após alterações, confirme e salve as alterações, reinicie o Microsiga Protheus e visualize na exceção, o campo suportará as casas decimais informadas.

O procedimento deve ser realizado em modo exclusivo.
