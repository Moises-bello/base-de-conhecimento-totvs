---
content_hash: c453d301e287aa062304c4244a1aa8eb81b7afb618c80e868725fb3cfca7cb63
fetched_at: '2026-06-29T00:08:28.258321+00:00'
page_id: '271674282'
product: rm
source: tdn-rm
title: 115873 MCP-1624 DT Processo de Importação de Movimentos para Automação Comercial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271674282
version: 117
---

# PROCESSO DE IMPORTAÇÃO DE MOVIMENTOS PARA AUTOMAÇÃO COMERCIAL

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Totvs Gestão de Estoque, Compras e Faturamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *MOV 039* | *IMPORTAÇÃO DE MOVIMENTO* | |
| **Tickets relacionados** | *115873* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MCP-1624 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL e Oracle.* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Criação do parâmetro "Não Emitir Cupom Fiscal" no conceito de Importação de Movimento, com o objetivo de sobrescrever o parâmetro do Tipo de Movimento (FIS - DADOS - "Emitir Cupom Fiscal").

Este procedimento foi criado para possibilitar a Importação Comercial corretamente, pois, como o arquivo de automação comercial já importa o Vínculo com o movimento, as Reduções e os Cupons, então, o movimento importado não deve gerar o Cupom Fiscal automaticamente.

## Procedimento para Utilização

1. Entrar em ***"Integração | Conceito (ETL)"***;
2. Selecionar o conceito de "Importação de Movimento" e em ***"Processos"*** clicar em ***"Processar******Novo Conceito"***.
3. Na primeira aba, será apresentado o parâmetro "Não Emitir Cupom Fiscal", que deve ser marcado caso não queira que o movimento gere os Cupons Fiscais.
4. Escolher o arquivo de movimento a ser importado e realizar a importação.
5. Verificar que os movimentos foram criados, porém os Cupons Ficais não foram gerados.

divs
