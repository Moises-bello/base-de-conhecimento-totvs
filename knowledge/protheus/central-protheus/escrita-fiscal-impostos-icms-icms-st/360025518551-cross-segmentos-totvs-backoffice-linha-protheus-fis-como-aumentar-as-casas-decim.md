---
article_id: 360025518551
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: b1a2d6e34804737a8d3166a15c6b9c0854fedcbda6d7f20ed805fad7cbc1f621
fetched_at: '2026-06-28T22:39:20.356839+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como Aumentar as
  Casas Decimais da Margem de Lucro (MVA-ICMS ST)?
type: support-article
updated_at: '2021-07-13T17:28:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025518551-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-Aumentar-as-Casas-Decimais-da-Margem-de-Lucro-MVA-ICMS-ST
---

**Dúvida**

Como Aumentar as Casas Decimais da Margem de Lucro (MVA-ICMS ST)?

**Ambiente**Protheus - Fiscal - A partir da versão 11.80  
  
  
   
**Solução**

# Aumentar as Casas Decimais da Margem de Lucro (MVA-ICMS ST)

|  |  |
| --- | --- |
| **Produto:** | Microsiga Protheus |
| **Versões:** | Protheus 11 e 12 |
| **Ocorrência:** | Aumentar as Casas Decimais da Margem de Lucro (MVA-ICMS ST) |
| **Ambiente:** | SIGAFIS |
| **Passo a passo:** | Para que o sistema atenda sua solicitação, deverá aumentar a margem de lucro até atingir o valor desejado. Como o campo suporta somente 99,99 deverá aumentar no configurador:  SIGACFG: Base de Dados->Dicionário de Dados->Base de Dados e localizar o tamanho dos campos referente a Margem de lucro abaixo:    D2\_MARGEM, D1\_MARGEM, FT\_MARGEM, F7\_MARGEM, CD2\_MVA, B1\_PICMRET, B1\_PICMENT, CFC\_MARGEM  Nas respectivas Tabelas:  SD2, SD1, SFT, SF7, CD2 , SB1 e CFC     * Exemplo:   **Campo**: F7\_MARGEM  **Tamanho Original**: 05, (Altere para a quantidade desejada)  **Decimal**: 04 (Ou alterar para quantidade desejada)  **Formato original**: @E 99.99, (Exemplo: Altere para @E 999.99)    Após alterações, confirme e salve as alterações, reinicie o Microsiga Protheus e visualize na exceção, o campo suportará as casas decimais informadas. |
