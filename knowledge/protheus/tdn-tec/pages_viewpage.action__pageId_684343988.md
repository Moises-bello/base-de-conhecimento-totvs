---
content_hash: 6539ae941d76cbbd33a3a26c558d462f36d866c3fe1ad7ce4881109347abd945
fetched_at: '2026-07-02T19:24:27.844629+00:00'
page_id: '684343988'
product: protheus
source: tdn-tec
title: Correção - TcBrwose deve mostrar no mínimo uma linha
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=684343988
version: 1
---

|  |  |
| --- | --- |
| Situação | Após atualização do Smartclient para a versão Harpia o TcBrwose parou de mostrar uma linha de um TcBrowse pequeno |
| Ocorrência | Problema ocorre devido a um cálculo de linhas visíveis que se a linha não aparecer inteira, a mesma era escondida |
| Correção | Correção efetuada para sempre mostrar no mínimo 1 linha (mesmo que ela não seja totalmente visível |
| Informações adicionais | * Referente ao chamado: #LOGIX-56 (Ryver) * Referente à ocorrência: DTCLIENT01-3355 * Disponível em builds iguais ou superiores a 7.00.210324P - 20.3.0.4 e 7.00.21.0324P - 20.3.1.0 |
