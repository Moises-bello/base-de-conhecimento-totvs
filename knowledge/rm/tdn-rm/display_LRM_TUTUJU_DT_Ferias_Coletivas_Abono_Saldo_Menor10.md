---
content_hash: c3cbf4fb6e23a8b57df83530c33b41e1fd13153b50ba967c92ed99e027a1cadc
fetched_at: '2026-06-29T00:08:09.374074+00:00'
page_id: '239035715'
product: rm
source: tdn-rm
title: TUTUJU_DT_Ferias_Coletivas_Abono_Saldo_Menor10
type: documentation
url: https://tdn.totvs.com/display/LRM/TUTUJU_DT_Ferias_Coletivas_Abono_Saldo_Menor10
version: 1
---

# FÉRIAS COLETIVAS NÃO CONSIDERA ABONO AO VERIFICAR SALDO MENOR QUE 10

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Férias Coletivas* |
| **Situação/Requisito:** | *Ao cadastrar Férias Coletivas marcando o parâmetro "Pagar Abono", não está sendo considerado os dias de abono para validar se o saldo de férias ficou menor que 10 dias.*  *Dessa forma, quando está marcado o parâmetro "Completa período de férias quando saldo ficar menor que 10 dias" no Sindicato, e os dias de férias deixa o saldo inferior a 10, está sendo alterado o período de férias informado pelo usuário.* |
| **Solução/Implementação:** | *Ajuste no cadastro de Férias Coletivas para que, caso esteja marcada a opção "Pagar Abono", considere os dias de abono para validar se o saldo de férias ficou menor que 10 dias.* |
| **Chamados   relacionados:** | *TUTUJU, TVBH70* |
| **Versões/Release:** | *12.1.12, 11.82.45* |
