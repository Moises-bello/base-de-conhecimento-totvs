---
content_hash: 9f961bf0a56a53f127549f4773d807600d29f5adc4b5eda0327eb67d3fada73e
fetched_at: '2026-06-29T00:08:23.242463+00:00'
page_id: '269553149'
product: rm
source: tdn-rm
title: 169285_DT_Folha_Analitica_Funcionarios_sem_movimento_Tipo_U
type: documentation
url: https://tdn.totvs.com/display/LRM/169285_DT_Folha_Analitica_Funcionarios_sem_movimento_Tipo_U
version: 113
---

# Folha Analítica

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | *TOTVS Folha de Pagamento.* |
| **Função:** | *Emissão da Folha Analítica para funcionários com movimentação na competência e período.* |
| **Situação/Requisito:** | *Ao gerar folha analítica para todos os funcionários com o parâmetro ‘Imprimir funcionários sem movimentação’, os funcionários do tipo U- Outros são impressos mesmo que não haja movimentação na competência atual.* |
| **Solução/Implementação:** | *Foi identificado que para o ultimo patch na 12.1.13.129 e como os últimos layouts dos relatórios da folha analítica FOPREL0010 - Folha Analítica TXT.TotvsReport e FOPREL0009 - Folha Analítica.TotvsReport mesmo que o funcionário esteja com tipo de funcionário U - Outros e não tendo movimentação e o parâmetro "Imprimir funcionários sem movimentação" esteja desmarcado tal funcionário não é impresso na Folha Analítica tanto no layout em PDV como em TXT.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *169285.* |
| **Requisito (ISSUE):** | *MRH-2476* |

divs
