---
content_hash: 23329730c25e167a55694ed0dc2c6f3b41edb7ea4c854499b04715285046db9a
fetched_at: '2026-06-29T00:08:12.973974+00:00'
page_id: '243656140'
product: rm
source: tdn-rm
title: TVE545_DT_Pagamento_Inscricao_Cartao_Portal
type: documentation
url: https://tdn.totvs.com/display/LRM/TVE545_DT_Pagamento_Inscricao_Cartao_Portal
version: 113
---

# PAGAMENTO DE INSCRIÇÃO PELO PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Parâmetros* |
| **Situação/Requisito:** | *Ao tentar efetuar o pagamento da inscrição utilizando o cartão de crédito/débito pelo portal, o sistema retorna um erro e não inicia a operação.* |
| **Solução/Implementação:** | *Foi identificado que no momento que é carregado os dados para o pagamento, o sistema está buscando de uma fonte incorreta, foi feito o ajuste e o pagamento passou a ser iniciado corretamente.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs

na tela de parâmetro foi identificado nos parâmetros de pessoa, não está sendo possível marcar ou desmarcar nenhum parâmetro.
