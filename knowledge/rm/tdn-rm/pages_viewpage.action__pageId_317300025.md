---
content_hash: 77e6e71205a1d9a3e0b3fa035d49cd1e31c6a1d6207d4ce464c40564eff6d0e4
fetched_at: '2026-06-29T00:08:46.462652+00:00'
page_id: '317300025'
product: rm
source: tdn-rm
title: 1432704 FINANCEIRO01-3225 DT Retorno de cobrança bancária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317300025
version: 94
---

# RETORNO DE COBRANÇA BANCÁRIA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Retorno de cobrança bancária |
| **Situação/Requisito:** | No retorno de cobrança do banco Santander, a chave do lançamento não está sendo preenchida nos boletos que foram registrados online, sem o envio da remessa comum. O campo enviado para “Chave do Lançamento” pelo retorno de cobrança simples, é nas posições 101 – 125. Para boletos registrados através do registro on-line, o banco está retornando esse campo em branco, e a chave do lançamento é enviada nas posições 055 – 069. |
| **Solução/Implementação:** | Ajuste no retorno bancário de cobrança registrada para o banco Santander para utilizar o campo Chave de Lançamento 2 para atender ao retorno dos boletos registrados online |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |

divs
