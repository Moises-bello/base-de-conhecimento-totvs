---
content_hash: d760a9cc931c4b4e793fd00405c25336cba1d8603514291b409f1e5a81c4959a
fetched_at: '2026-06-29T00:08:23.270188+00:00'
page_id: '269554053'
product: rm
source: tdn-rm
title: 169217_DT_Folha_Analitica_Pagina_Em_Branco
type: documentation
url: https://tdn.totvs.com/display/LRM/169217_DT_Folha_Analitica_Pagina_Em_Branco
version: 112
---

# Folha Analítica

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projeto.* |
| **Módulo:** | *TOTVS Folha de Pagamento.* |
| **Função:** | *Emissão Folha Analítica.* |
| **Situação/Requisito:** | Ao gerar a folha analítica com a primeira quebra de seção as primeiras páginas ficam em branco, e as demais aparecem somente com totalizadores |
| **Solução/Implementação:** | *Foi identificado que para o ultimo patch na 12.1.13.129 e como os últimos layouts dos relatórios da folha analítica FOPREL0010 - Folha Analítica TXT.TotvsReport e FOPREL0009 - Folha Analítica.TotvsReport o sistema não emite folhas em branco e nem deixa de emitir os dados de cada funcionário.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *169217.* |
| **Requisito (ISSUE):** | MRH-2486 |

divs
