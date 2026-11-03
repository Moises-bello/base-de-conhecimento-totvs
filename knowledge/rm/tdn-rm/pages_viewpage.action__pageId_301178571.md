---
content_hash: 5095bad3ce4e4e33115e7d4c04e1cad9a72e0566fcfa92ea66b9057e41a0260d
fetched_at: '2026-06-29T00:08:42.974584+00:00'
page_id: '301178571'
product: rm
source: tdn-rm
title: FINANCEIRO01-2771 DT Função de fórmula MONTACODIGOBARRASBRADESCO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301178571
version: 94
---

# Função de fórmula MONTACODIGOBARRASBRADESCO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Totvs Gestão Financeira. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Função de fórmula | MONTACODIGOBARRASBRADESCO |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Boletos | *Boletos.* | |  |  | |
| **Cadastros Iniciais:** | N/A. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-2771> |
| **País(es):** | BRA |
| **Banco(s) de Dados:** | Sql Server, Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Função de fórmula para geração de código de barras para o banco Bradesco.

## Procedimento para Utilização

       1.            Abrir o cadastro de fórmulas e incluir ou editar um fórmula.

       2.            Após digitar as informações da fórmula utilizar a função de fórmula MONTACODIGOBARRASBRADESCO, informando os parâmetros para a função de fórmula.

* Valor  (decimal).
* Número do banco (string)
* Número da Agência (string)
* Número da Conta (string)
* Carteira (string)
* Nosso número (string)
* Data vencimento (data)
* Contra apresentação (0 não | 1 sim)

       3.            Utilizar a fórmula criada ou editada para  geração do código de barras.

divs
