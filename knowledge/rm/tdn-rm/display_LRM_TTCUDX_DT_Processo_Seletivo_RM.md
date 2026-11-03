---
content_hash: ec548d5d81a78e9aadc69ef7adec843bc7af63a188e45375e318e6003e7e9c44
fetched_at: '2026-06-29T00:06:06.191491+00:00'
page_id: '201729164'
product: rm
source: tdn-rm
title: TTCUDX_DT_Processo_Seletivo_RM
type: documentation
url: https://tdn.totvs.com/display/LRM/TTCUDX_DT_Processo_Seletivo_RM
version: 2
---

# PROCESSO SELETIVO RM

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Processo Seletivo RM* |
| **Situação/Requisito:** | *Erro ao informar plano de pagamento na matrícula processo seletivo RM. Na matrícula do processo seletivo RM na aba Financeiro é habilitado Cadastrar contrato e em seguida clicado na lookup de plano de pagamento ocorre o erro: Ocorreu um erro ao efetuar a leitura da visão de lookup: ORA-00918: coluna definida de maneira ambígua. O mesmo incidente ocorre em base de dados sql server.* |
| **Solução/Implementação:** | *Ajuste no filtro da consulta sql da lookup que traz a visão dos planos de pagamento.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.7 e 12.1.8* |
