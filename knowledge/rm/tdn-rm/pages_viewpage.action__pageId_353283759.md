---
content_hash: f37a62049476b7380e1011d82caf0e5d4525eb19450f313b732ad9a9a70d71bb
fetched_at: '2026-06-29T00:08:57.218939+00:00'
page_id: '353283759'
product: rm
source: tdn-rm
title: DT Função de fórmula MONTACODIGOBARRASITAU
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=353283759
version: 2
---

# Função de fórmula MONTACODIGOBARRASITAU

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Totvs Gestão Financeira. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Função de fórmula | MONTACODIGOBARRASITAU |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Boletos | *Boletos.* | |
| **Cadastros Iniciais:** | N/A. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-6344> |
| **País(es):** | BRA |
| **Banco(s) de Dados:** | Sql Server, Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Função de fórmula para geração de código de barras para o banco Itau.

## Procedimento para Utilização

       1.            Abrir o cadastro de fórmulas e incluir ou editar um fórmula.

       2.            Após digitar as informações da fórmula utilizar a função de fórmula MONTACODIGOBARRASITAU, informando os parâmetros para a função de fórmula.

* Valor  (decimal).
* Número do banco (string) (104)
* Número da Conta (string)
* Número da Agência (string)
* Código do Cedente (string)
* Carteira (string)
* Nosso número (string)
* Número do documento (string)
* Data vencimento (data)

       3.            Utilizar a fórmula criada ou editada para  geração do código de barras.
