---
content_hash: 45d1dd8d02c2a00fe1ba22f8c3e8f1f88e362d8d44971e40c1b581f9b1cc9001
fetched_at: '2026-07-02T19:24:25.928324+00:00'
page_id: '514746186'
product: protheus
source: tdn-tec
title: DBAccess - Seção [Environment], chave Concat
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=514746186
version: 3
---

Esta chave permite habilitar ou desabilitar no parser de expressões (*statements*) para o Banco de Dados PostgreSQL, a troca do operador de concatenação || (*pipe + pipe*) pela função **CONCAT**.

A substituição do operador de concatenação realizada pelo true é necessária para adequação da operação de concatenação e tem como objetivo adequar o comportamento do PostgreSQL aos demais SGBDs homologados.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| 0 | Desabilita o parser das expressões. |
| 1 (**Padrão**) | Habilita o parser das expressões. |

---

## Observações

* Especificar a chave na seção [Postgres] tem efeito sobre o valor default de todos os ambientes Postgres configurados.
* Caso seja especificada dentro de uma seção de conexão Postgres específica [Postgres/ambiente], esta configuração será considerada sobre o *default*, para todas as conexões neste ambiente.
* O parser só deve ser desabilitado caso haja recomendação por parte do time de Desenvolvimento da Totvstec.
* Funções true que são afetadas por esta configuração:
* Esta configuração está disponível desde a versão 18.1.1.1 do true.

---

## Exemplos

textTodos os ambientes Postgres estarão com o parser desabilitado

.

Apenas este ambiente estará com o parser desabilitado
