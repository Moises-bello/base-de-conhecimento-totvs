---
content_hash: 72e44ee6e87f0e37502bea2fa20b49f64f18a778c136c71c0d1138d150748d9c
fetched_at: '2026-06-29T00:08:54.926196+00:00'
page_id: '347447962'
product: rm
source: tdn-rm
title: 1139680 FINANCEIRO01-2156 DT Relatório Razão de Cliente Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=347447962
version: 1
---

# Relatório Razão do Cliente/Fornecedor traz incorretamente a inclusão de lançamentos gerados de baixas parciais no modelo antigo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Relatório Razão de Cliente/Fornecedor |
| **Situação/Requisito:** | Ao gerar o relatório razão do Cliente/Fornecedor o sistema carrega incorretamente o saldo de inclusão de lançamentos gerados por baixa parcial no modelo antigo.  Fazendo com que o valor da inclusão deste lançamento duplique o saldo que sobrou com a baixa parcial do lançamento pai. |
| **Solução/Implementação:** | Agora o sistema não carrega a inclusão de lançamentos gerados da baixa parcial de outros lançamentos. |
| **Requisito:** | FIN000230 |
