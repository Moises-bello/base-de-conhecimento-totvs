---
content_hash: 19405facc2663ca073d4f9e472a9fa3d10942a0e43257db0adc129183b1c7e51
fetched_at: '2026-06-29T00:06:26.511577+00:00'
page_id: '225950321'
product: rm
source: tdn-rm
title: TUBSJD_DT_ENVELOPE_DE_PAGAMENTO_NOME_DOS_CAMPOS
type: documentation
url: https://tdn.totvs.com/display/LRM/TUBSJD_DT_ENVELOPE_DE_PAGAMENTO_NOME_DOS_CAMPOS
version: 123
---

# ENVELOPE DE PAGAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Envelope de Pagamento* |
| **Situação/Requisito:** | Ao selecionar a opção de "Visualizar nome dos campos" no envelope de pagamento, na aba de incidência era exibido "0.0" como o nome de vários campos, pois na query foi selecionado o valor "0.0" ao invés dos campos da tabela. |
| **Solução/Implementação:** | *Foi alterado para trazer os campos propriamente ditos no select, e zerado os seus valores nas rows após o select. Dessa forma o nome dos campos serão exibidos corretamente* |
| **Chamados relacionados:** | TUBSJD, TUHZ82 |

divs
