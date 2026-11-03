---
content_hash: f5dce26573eb70bab2cf25792cf4b8a11314602b6e29f877b1ec733689a0fe55
fetched_at: '2026-06-29T00:06:26.256132+00:00'
page_id: '224456708'
product: rm
source: tdn-rm
title: TUDBGM_DT_Erro_Atualizar_Informacoes_RM_Portal_Informe_De_Rendimentos
type: documentation
url: https://tdn.totvs.com/display/LRM/TUDBGM_DT_Erro_Atualizar_Informacoes_RM_Portal_Informe_De_Rendimentos
version: 122
---

# DIRF/INFORME DE RENDIMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF/Informe de Rendimentos* |
| **Situação/Requisito:** | Ao gerar o Informe de Rendimentos e clicar no botão : Atualiza dados informe de rendimentos quando não existem dados na tabela PPARDIRF para a coligada de geração o sistema apresenta a seguinte mensagem:  ORA-00942: a tabela ou view não existe No SQL Server mesmo quando existem dados ao clicar no botão o sistema cria os dados na tabela. |
| **Solução/Implementação:** | *Ajustado serviço quando atualiza dados do informe de rendimentos em base Oracle.* |
| **Chamados relacionados:** | *TUDBGM, TUGTYI* |

divs
