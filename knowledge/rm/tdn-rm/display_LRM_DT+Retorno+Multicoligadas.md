---
content_hash: 376ecc4f92268c9c45c5d799fda60448bf9e39a82f7acdbb3852bb3f45c98ff8
fetched_at: '2026-06-29T00:08:53.047072+00:00'
page_id: '342308276'
product: rm
source: tdn-rm
title: DT Retorno Multicoligadas
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Retorno+Multicoligadas
version: 11
---

# Retorno Multicoligadas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Retorno de Débito Automático*  *Retorno de Cobrança*  *Retorno de Pagamento* | *Retorno de Débito Automático*  *Retorno de Cobrança*  *Retorno de Pagamento* | |
| **Cadastros Iniciais:** | *Bancos e Agências, Convênio, Conta Caixa.* |
| **Parâmetro(s):** | *Contas a Pagar | Integração Bancária | Pagamento Eletrônica | Valor Default para diferença em retorno bancário.*  **Contas a Receber | Integração Bancária | Cobrança Eletrônica | Valor Default para diferença em retorno bancário** |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-5398> |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | **Oracle e MS-SqlServer** |
| **Tabelas Utilizadas:** | *FBANCOLAYOUT, FBANCO, FLAN, FLANBAIXA, FCXA, FRETORNOBANCARIO, FRETORNOBANCARIOITEM* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Evolução nos processos em lote, para permitir efetuar o retorno de pagamento, cobrança e débito automático para múltiplos arquivos que tenham informações de várias coligadas ao mesmo tempo.

## Procedimento para Utilização

Seguir o procedimento padrão para utilização do retorno em lote, definido nos documentos técnicos abaixo:

Observações:

1. As parametrizações referentes a diferença a maior e a menor serão as que foram definidas em "Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a Receber | Integração Bancária | Pagamento Eletrônica | Valor default para diferença em retorno bancário.
2. A conta caixa que será utilizada para efetuar a baixa será a definida no lançamento.
3. A contabilização será efetuada baseado no evento contábil definido nos defaults do tipo de documento/campos opcionais do lançamento.
