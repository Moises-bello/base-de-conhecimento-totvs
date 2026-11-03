---
content_hash: 0a77a635082f26c7d49dae41580237da8b8120680be6a054afd34b9db77acb3a
fetched_at: '2026-06-29T00:09:01.812525+00:00'
page_id: '378280251'
product: rm
source: tdn-rm
title: DT Layout de Remessa de Cobrança para o banco Crefisa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=378280251
version: 2
---

# Layout de Cobrança para o banco Crefisa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Layout de Remessa de Cobrança | FINLAY0054 - Cob. Crefisa (CNAB240).TotvsGen |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Remessa de Cobrança | Remessa de Cobrança | |  |  | |
| **Cadastros Iniciais:** | Não se aplica |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-7058> |
| **País(es):** | BRA |
| **Banco(s) de Dados:** | SQL Server / Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Disponibilizado layout de geração de arquivo texto, para emissão de bloquetes de cobrança

## Procedimento para Implantação

Acesse o Gerador de Saídas em *Gestão Financeira | Gestão / Gerador de Saída*, e importe o layout em *Processos / Importar Layout*, clique no botão "Adicionar Objetos", e então indique o arquivo FINLAY0054 - Cob. Crefisa (CNAB240).TotvsGen.

O layout deve ser informado no cadastro de Convênios em *Gestão Financeira | Movimentações Bancárias / Convênio*, na aba "Remessa Bancária", no campo "Código Layout" da Remessa de Cobrança.
