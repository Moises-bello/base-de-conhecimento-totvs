---
content_hash: e4bc3ad62ff7fb9ff4e8c9b70cd48a2127e9577e2eb1e3bddc30f258bc3b5dcd
fetched_at: '2026-06-29T00:08:12.052031+00:00'
page_id: '243634319'
product: rm
source: tdn-rm
title: TVCPZC_DT_Data_Transferencia_Funcionario
type: documentation
url: https://tdn.totvs.com/display/LRM/TVCPZC_DT_Data_Transferencia_Funcionario
version: 114
---

# FUNCIONÁRIOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Cadastro de Funcionários |
| **Situação/Requisito:** | Ao efetuar uma admissão preenchendo a data de transferência, mas posteriormente informando o Tipo de admissão como REEMPREGO, o sistema automaticamente desabilita o campo da data de transferência, porém a data ainda fica registrada lá, quando o sistema deveria limpar o campo. |
| **Solução/Implementação:** | Alteração na lógica ao alterar o valor do campo 'Tipo de Admissão' |
| **Chamados relacionados:** | TVCPZC; TVEF64 |

divs
