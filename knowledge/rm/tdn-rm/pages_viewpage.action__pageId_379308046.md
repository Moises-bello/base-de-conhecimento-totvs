---
content_hash: dc050c59e9681e3149a56f9e8b9b927b69674eb9e50f107225c3ae006bfd1d06
fetched_at: '2026-06-29T00:09:02.427296+00:00'
page_id: '379308046'
product: rm
source: tdn-rm
title: TOTVS Item de Pedido de Antibiótico - Manutenção 12.1.19
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379308046
version: 4
---

# 197881 DSAUGCIH-13 DT Botão Calcular do Item de Pedido de Antibiótico

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Controle de Infecção Hospitalar |
| **Função:** | Cadastro de Antibiótico |
| **Situação/Requisito:** | No módulo CIH referente ao Item de Pedido de Antibiótico: Em Paciente > Internações > Antibiótico > Principio Ativo (Realizar dois cliques no registro) > Dispensações > Botão Calcular.  Ao clicar no botão Calcular da tela de Item de Pedido de Antibiótico o mesmo deve excluir os registros de dispensação de antibiótico ao apresentar o cálculo como "Dose Zerada", esse comportamento não está ocorrendo. |
| **Solução/Implementação:** | Implementada exclusão de registros de dispensações de antibióticos no botão calcular da tela de Item de Pedido de Antibiótico, esses registros são apenas excluídos se o cálculo verificar a condição de "Dose Zerada" nos registros de dispensação. |
