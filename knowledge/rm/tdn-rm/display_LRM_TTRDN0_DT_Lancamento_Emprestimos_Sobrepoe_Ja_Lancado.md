---
content_hash: cc09eb7d8bd7c12244dc647e332f2bef0b392e985950873637e4b15d7df583b1
fetched_at: '2026-06-29T00:06:22.337202+00:00'
page_id: '223914893'
product: rm
source: tdn-rm
title: TTRDN0_DT_Lancamento_Emprestimos_Sobrepoe_Ja_Lancado
type: documentation
url: https://tdn.totvs.com/display/LRM/TTRDN0_DT_Lancamento_Emprestimos_Sobrepoe_Ja_Lancado
version: 2
---

# LANÇAMENTO DE EMPRÉSTIMOS SOBREPÕE EVENTO JÁ LANÇADO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Grupo de Eventos* |
| **Situação/Requisito:** | *No lançamento de empréstimos pelo Grupo de Eventos não está somando com empréstimos já lançados no mês. Sempre sobrepõe o valor do evento.*  *Com isto, os dados inseridos na movimentação do cadastro de empréstimos ficam incompatíveis com o valor descontado no envelope do funcionário.* |
| **Solução/Implementação:** | *Ajuste no lançamento de empréstimos pelo Grupo de Eventos para sempre somar, caso o mesmo evento já exista no envelope do funcionário.* |
| **Chamados   relacionados:** | *TTRDN0, TTYXDU* |
| **Versões/Release:** | *11.82.43, 12.1.10* |
