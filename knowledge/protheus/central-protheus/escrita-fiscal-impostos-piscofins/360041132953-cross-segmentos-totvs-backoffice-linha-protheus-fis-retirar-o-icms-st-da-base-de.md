---
article_id: 360041132953
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 2c6e7d067be9f09b2e32b9c785f900806f656c6960b760dfc6356c336a254e66
fetched_at: '2026-06-28T22:39:36.956437+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Retirar o ICMS ST
  da base de cálculo de PIS e COFINS
type: support-article
updated_at: '2021-09-14T02:46:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041132953-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Retirar-o-ICMS-ST-da-base-de-c%C3%A1lculo-de-PIS-e-COFINS
---

**Dúvida**  
Retirar o ICMS ST da Base de Cálculo de PIS COFINS  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Configure os parâmetros MV\_DBSTPIS e MV\_DBSTCOF:

Conteúdos:

1 - Nunca retira. (Opção padrão do Sistema);

2 - Retira se houver crédito do ICMS ST;

3 - Retira se não houver crédito do ICMS ST;

4 - Retira se houver crédito do ICMS normal;

5 - Retira se não houver crédito do ICMS normal;

6 - Sempre retira;

Resultado esperado:

Alterando os parâmetros é possível identificar se deve ou não considerar o valor ICMS ST na Base de Cálculo de PIS COFINS.

Observações  
Rotinas envolvidas:

MATXFIS, MATA103 (Entrada);

MATXFIS, MATA410, MATA460 (Saída).
