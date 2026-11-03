---
content_hash: a0c7f292d40f487ae6bda06bb8dda335f9cee88614fc7dfff7904b21c30e74b3
fetched_at: '2026-06-29T00:06:12.960761+00:00'
page_id: '207356066'
product: rm
source: tdn-rm
title: TTEIUG_DT_Tipo_CAGED_Diario
type: documentation
url: https://tdn.totvs.com/display/LRM/TTEIUG_DT_Tipo_CAGED_Diario
version: 7
---

# CAGED - TIPO CAGED DIÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *CAGED - Tipo CAGED diário* |
| **Situação/Requisito:** | Ao gerar o CAGED para o tipo Diário, o arquivo é gerado, porém os funcionários não são apresentados  no final da execução e nem no arquivo gerado. |
| **Solução/Implementação:** | Ajuste na busca do funcionário, verificar somente a data para o campo 'dataadmissao' que é datetime. |
| **Chamados   relacionados:** | *TTEIUG* |
| **Versões/Release:** | *12.1.9* |

divs
