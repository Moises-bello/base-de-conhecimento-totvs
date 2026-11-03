---
content_hash: 1a877bca1cecec0a9184999b08ab770dae5c3876e0257bb088c302dd6154c9a9
fetched_at: '2026-06-29T00:08:59.492673+00:00'
page_id: '362458956'
product: rm
source: tdn-rm
title: 2773631 FINANCEIRO01-7073 DT Erro Ao Gerar Boleto Com Registro Online
type: documentation
url: https://tdn.totvs.com/display/LRM/2773631+FINANCEIRO01-7073+DT+Erro+Ao+Gerar+Boleto+Com+Registro+Online
version: 2
---

# Lançamento - Boleto

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Lançamento - Boleto |
| **Situação/Requisito:** | Ao tentar gerar um boleto com registro online pelo PDC o sistema apresenta o erro: "O índice estava fora do intervalo. Ele deve ser não-negativo e menor que o tamanho da coleção." |
| **Solução/Implementação:** | Otimização no processo de inclusão de boleto com registro online. Agora o sistema inclui o boleto e valida corretamente se não houver um convênio no lançamento e se não estiver nenhum outro convênio default parametrizado. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000268 |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
