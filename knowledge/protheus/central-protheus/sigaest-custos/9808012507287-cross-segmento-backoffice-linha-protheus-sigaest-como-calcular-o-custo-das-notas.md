---
article_id: 9808012507287
category: SIGAEST - CUSTOS
content_hash: d8fef25572690c2d8ff99074c8395ab5f5ebd099db8a4a726a0566d03811b9fc
fetched_at: '2026-06-28T22:39:00.652701+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como calcular o custo
  das notas fiscais de entrada que controlam poder de terceiro e não atualizam estoque?
type: support-article
updated_at: '2025-03-12T12:27:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9808012507287-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-calcular-o-custo-das-notas-fiscais-de-entrada-que-controlam-poder-de-terceiro-e-n%C3%A3o-atualizam-estoque
---

**Dúvida**Como calcular o custo das notas fiscais de entrada que controlam poder de terceiro e não atualizam estoque?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**O custo das notas fiscais de entrada que controlam poder de terceiro e não atualizam estoque é calculado quando o parâmetro **MV\_SDTESN3** está configurado como 1 ou 2.

Com essas configurações, o custo calculado será apenas informativo (não irá atualizar o saldo físico e financeiro do produto) e armazenado nos campos D1\_CUSTO e B6\_CUSTO1.

O custo calculado será considerado pelos relatórios Inventário Mod.7 (MATR460) e Relação de materiais de/em terceiros (MATR480).

**Importante**

Configurar o parâmetro MV\_SDTESN3 como 1 ou 2 irá considerar no relatório Inventário Mod.7 (MATR460) notas de terceiro que não atualizam estoque.

Para maiores informações referente ao seu conceito e configurações disponíveis, acesse o link abaixo:  
[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Validação do parâmetro MV\_SDTESN3PEST002 - MV\_SDTESN3 - Considera TES que não atualiza estoque.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060289014-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Valida%C3%A7%C3%A3o-do-par%C3%A2metro-MV-SDTESN3)

**INFORMAÇÕES ADICIONAIS**

Caso o parâmetro seja alterado para considerar o custo das notas de terceiros que não atualizam estoque, e seja necessário recalcular o custo das notas fiscais e os saldos de terceiros, poderá ser executada as rotinas **Refaz Custo de Entrada (MATA190)** e **Refaz Poder de Terceiros (MATA216).**

Para atualização do custo da nota através da rotina Refaz Custo de Entrada, é necessário que o período em que a nota foi digitada esteja em aberto.

**Saiba mais:**

*[MP - SIGAEST - Como fazer uma análise de Custos no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*

[*Refaz Custo de Entrada (MATA190) - Conceito e Exemplos*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051999634-MP-SIGAEST-Custo-de-entrada-MATA190-?source=search)
