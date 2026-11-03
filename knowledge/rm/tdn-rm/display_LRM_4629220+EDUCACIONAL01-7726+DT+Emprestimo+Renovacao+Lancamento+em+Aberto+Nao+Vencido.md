---
content_hash: bddab1fe21f46d9b5d929b97c742b096381a01723385db48b994d156825a40b8
fetched_at: '2026-06-29T00:09:55.021680+00:00'
page_id: '445675487'
product: rm
source: tdn-rm
title: 4629220 EDUCACIONAL01-7726 DT Emprestimo Renovacao Lancamento em Aberto Nao
  Vencido
type: documentation
url: https://tdn.totvs.com/display/LRM/4629220+EDUCACIONAL01-7726+DT+Emprestimo+Renovacao+Lancamento+em+Aberto+Nao+Vencido
version: 4
---

# EMPRÉSTIMOS E RENOVAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Bibliotecária |
| **Função:** | Empréstimo e Renovação |
| **Situação/Requisito:** | Durante a operação de empréstimo, se o usuário tiver algum lançamento financeiro gerado pela biblioteca com a data de vencimento no mesmo dia que a movimentação está sendo feita, o sistema mostra um alerta sobre estes lançamentos e pedi uma confirmação se deseja ou não prosseguir com o empréstimo. Na renovação este aviso não era exibido. |
| **Solução/Implementação:** | Foi feito um ajuste para que o sistema considere o lançamento em aberto que não esteja vencido, não somente o que vence no dia da movimentação, foi feito o ajuste para mostrar também o aviso na renovação. Foi também criado um parâmetro para que ao invés de mostrar o aviso, o sistema bloqueará a movimentação, este parâmetro é o "**Bloquear empréstimo/renovação para usuários com lançamentos na Biblioteca em aberto"** (para mais detalhes sobre este parâmetro )". |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
