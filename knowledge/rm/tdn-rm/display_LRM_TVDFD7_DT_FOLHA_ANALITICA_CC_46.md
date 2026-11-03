---
content_hash: f508c54c4afdb2098851802193af6b5dbc188619542243281b0db99bb7217173
fetched_at: '2026-06-29T00:08:13.312492+00:00'
page_id: '243662770'
product: rm
source: tdn-rm
title: TVDFD7_DT_FOLHA_ANALITICA_CC_46
type: documentation
url: https://tdn.totvs.com/display/LRM/TVDFD7_DT_FOLHA_ANALITICA_CC_46
version: 114
---

# Folha Analítica

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamentos* |
| **Função:** | *Calculo de FGTS e FGTS SEFIP* |
| **Situação/Requisito:** | A Folha Analítica Delphi não contemplava a incidência de FGTS para eventos de código de cálculo 46 Honorários para funcionários autônomos. O valor dos eventos era somado  ou subtraído observando apenas a categoria de autônomo e o código de cálculo 46. Computando os valores destes eventos nos campos FGTS e FGTS sefip*.* |
| **Solução/Implementação:** | A Folha Analítica Delphi passa a contemplar a incidência de FGTS para eventos de código de cálculo 46 Honorários para funcionários autônomos. O valor dos eventos era somado  ou subtraído observando apenas a categoria de autônomo e o código de cálculo 46. Caso as incidências de FGTS estão desmarcados os valores dos eventos não serão computados nos campos FGTS e FGTS SEFIP*.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TVDFD7 |
| **Requisito (ISSUE):** |  |

divs
