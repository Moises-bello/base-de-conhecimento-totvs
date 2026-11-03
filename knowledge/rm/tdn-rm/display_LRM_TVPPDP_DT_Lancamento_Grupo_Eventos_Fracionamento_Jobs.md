---
content_hash: 3a11b6b8ed6a3072c0b76bb073f7da8f5d8514989d219b1a7d87a3d5ffe94a56
fetched_at: '2026-06-29T00:08:16.418658+00:00'
page_id: '245172563'
product: rm
source: tdn-rm
title: TVPPDP_DT_Lancamento_Grupo_Eventos_Fracionamento_Jobs
type: documentation
url: https://tdn.totvs.com/display/LRM/TVPPDP_DT_Lancamento_Grupo_Eventos_Fracionamento_Jobs
version: 109
---

# LANÇAMENTO DE GRUPO DE EVENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Lançamento de Grupo de eventos* |
| **Situação/Requisito:** | *Quando a base está parametrizada para fracionar jobs e é realizado o lançamento global de eventos, pelo menu de grupo de eventos, o sistema pergunta ao usuário se deseja facionar os jobs para execução do processo, ao confirmar o fracionamento, o sistema apresenta a mensagem:*  *Object reference not set to an instance of an object.* |
| **Solução/Implementação:** | Foi ajustado o lançamento de grupo de eventos, para que quando o mesmo for executado com fracionamento de jobs, o erro não ocorra novamente. |
| **Chamados relacionados:** | *TVPPDP, TWCXLF* |

divs
