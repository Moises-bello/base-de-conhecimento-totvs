---
content_hash: 8b129302a0a02f4eb0e3bc6e86a640a1f68e251e203471fd56f69f7e10c3c29f
fetched_at: '2026-06-29T00:08:45.285984+00:00'
page_id: '309414159'
product: rm
source: tdn-rm
title: 1543997 FINANCEIRO01-3406 Remessa Santander CNAB240
type: documentation
url: https://tdn.totvs.com/display/LRM/1543997+FINANCEIRO01-3406+Remessa+Santander+CNAB240
version: 92
---

# LAYOUT REMESSA SANTANDER CNAB240

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Remessa de cobrança. |
| **Situação/Requisito:** | Ocorria erro na execução do processo de remessa de cobrança para o layout do Banco Santander no modelo CNAB240. A sentença SQL para carga dos dados do boleto era gerada com inconsistências na sintaxe em bases Oracle. |
| **Solução/Implementação:** | Foi ajustado o layout oficial da aplicação para remessa de cobrança CNAB240 do Banco Santander retirando da montagem da tabela FBOLETO (contexto 01) os alias para as tabelas de Lançamentos do Boleto, Lançamentos, Convênio e Conta. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 1543997. |
| **Requisito:** | FINANCEIRO01-3406. |

divs
