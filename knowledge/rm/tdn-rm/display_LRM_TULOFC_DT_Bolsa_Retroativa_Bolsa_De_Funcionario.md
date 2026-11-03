---
content_hash: c94a896bd956310a85ff3a7d52ec0a57581c3b761ee5c63f617c2b9a20172924
fetched_at: '2026-06-29T00:06:28.859853+00:00'
page_id: '233763867'
product: rm
source: tdn-rm
title: TULOFC_DT_Bolsa_Retroativa_Bolsa_De_Funcionario
type: documentation
url: https://tdn.totvs.com/display/LRM/TULOFC_DT_Bolsa_Retroativa_Bolsa_De_Funcionario
version: 119
---

# VERIFICAÇÃO DE BOLSA DE FUNCIONÁRIO NO PROCESSO DE BOLSA RETROATIVA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Bolsa Retroativa* |
| **Situação/Requisito:** | *Quando era executado o processo de Bolsa Retroativa para bolsas de funcionários, o sistema emitia a mensagem de erro: Invalid Object name: 'VFILIACAO'* |
| **Solução/Implementação:** | *Ajuste para buscar os códigos de pessoa para Pai e Mãe da tabela SPESSOA ao invés de buscar o código da tabela de filiação (VFILIACAO) na validação de bolsas de funcionário.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
