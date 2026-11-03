---
content_hash: 1e0a478260d59a33686e1309d6b8bee1a992b38fcd65f30c11e2dae92ac2acad
fetched_at: '2026-06-29T00:08:14.256938+00:00'
page_id: '244445286'
product: rm
source: tdn-rm
title: TUK864_DT_INSS_TERCEIRO
type: documentation
url: https://tdn.totvs.com/display/LRM/TUK864_DT_INSS_TERCEIRO
version: 113
---

# Folha Analítica

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Calculo do INSS de Terceiros* |
| **Situação/Requisito:** | *A Folha Analítica DELPHI não estava considerando a base de INSS autônomo para o cálculo do INSS de terceiro.* |
| **Solução/Implementação:** | O INSS de terceiro na folha analítica passará ter o seguinte cálculo:  Base INSS empresa somado a base INSS autônomo CC 46, NÃO SENDO CATEGORIA 15, com ou sem incidência de INSS é aplicado o percentual de terceiro da seção;  Acrescido dos  eventos de código calculo 46- Honorários  somando proventos ou base subtraindo descontos e aplicado 0,025 para funcionários de categoria 15;  *.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TUK864* |
| **Requisito (ISSUE):** |  |

divs
