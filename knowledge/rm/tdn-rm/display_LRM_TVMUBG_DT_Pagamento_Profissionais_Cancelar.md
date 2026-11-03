---
content_hash: 8fdc5bdd944685160089b632ab56f4857d51c60ecfb2284a119d188c7b820292
fetched_at: '2026-06-29T00:08:16.284790+00:00'
page_id: '244935240'
product: rm
source: tdn-rm
title: TVMUBG_DT_Pagamento_Profissionais_Cancelar
type: documentation
url: https://tdn.totvs.com/display/LRM/TVMUBG_DT_Pagamento_Profissionais_Cancelar
version: 110
---

# PAGAMENTO DE PROFISSIONAIS - CANCELAR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *Arquivos do candidato* |
| **Situação/Requisito:** | *Quando é executado um processo pagamento de profissionais alocados, com a função de cancelar o lançamento, quando é um cliente fornecedor o sistema retorna um erro e não conclui a operação.* |
| **Solução/Implementação:** | *Foi identificado que ocorre uma inconsistência de nome de coluna da base de dados inválida, quando o sistema identifica que o valor é zero (0) e é cliente fornecedor o sistema carrega os dados do lançamento, como está inválido, retorna a mensagem. Foi feito o ajuste na consulta sql que carrega os dados e o processo passou  a ser executado corretamente.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
