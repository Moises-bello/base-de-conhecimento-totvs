---
content_hash: 7829c3fc14f68bb8f77396ceb7f6b3a0195b987acf9d8dea74f8cf9b69dbfd15
fetched_at: '2026-06-29T00:08:54.829073+00:00'
page_id: '346498558'
product: rm
source: tdn-rm
title: FINANCEIRO01-5763 DT Função de fórmula MONTACODIGOBARRASCAIXA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=346498558
version: 2
---

# Função de fórmula MONTACODIGOBARRASCAIXA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Totvs Gestão Financeira. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Função de fórmula | MONTACODIGOBARRASCAIXA |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Boletos | *Boletos.* | |
| **Cadastros Iniciais:** | N/A. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-5763> |
| **País(es):** | BRA |
| **Banco(s) de Dados:** | Sql Server, Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Função de fórmula para geração de código de barras para o banco Caixa Econômica Federal.

## Procedimento para Utilização

       1.            Abrir o cadastro de fórmulas e incluir ou editar um fórmula.

       2.            Após digitar as informações da fórmula utilizar a função de fórmula MONTACODIGOBARRASCAIXA, informando os parâmetros para a função de fórmula.

* Valor  (decimal).
* Número do banco (string) (104)
* Número do Convênio (string)
* Número da Agência (string)
* Código do Cedente (string)
* Dígito do Cedente (string)
* Carteira (string)
* Nosso número (string)
* Data vencimento (data)

       3.            Utilizar a fórmula criada ou editada para  geração do código de barras.
