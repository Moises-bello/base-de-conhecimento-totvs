---
content_hash: 246bcab927c279117be5f19106490ec0b7b3869faeb94133f30f63fc87b16cfe
fetched_at: '2026-06-29T00:08:43.035678+00:00'
page_id: '301184602'
product: rm
source: tdn-rm
title: 1367203 FINANCEIRO01-2796 Lançamento Bolsa 100% Educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301184602
version: 96
---

# Inclusão de 2 lançamentos, 1 com desconto 100% com apenas 1 Boleto, Status Boleto

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção & Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Inclusão de Lançamentos |
| **Situação/Requisito:** | Ao executar a geração de lançamentos, são gerados dois lançamentos para um aluno, sendo um deles baixado (devido a bolsa 100% associada a parcela) e o outro fica em aberto.  Ao acessarmos os boletos desses dois lançamentos, verificamos que o lançamento 1 (que possui a bolsa 100%) ficou baixado porém com o boleto em aberto O lançamento 2 ficou com dois boletos em aberto, sendo um desses boletos referente ao valor correto daquela parcela e o outro boleto com o mesmo idboleto do lançamento 1. |
| **Solução/Implementação:** | Ajustado para que ao realizar a inclusão de lançamentos do Educacional, caso exista lançamentos com 100% de desconto baixados, o sistema gere apenas boleto para os valores em aberto dos lançamentos. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000268, FIN000254, FIN000040 |

divs
