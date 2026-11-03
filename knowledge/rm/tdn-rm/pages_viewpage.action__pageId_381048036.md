---
content_hash: eb378f741467af2dddfbfa312e4e7a13039ee1fd6066eceee7660f647fdd11eb
fetched_at: '2026-06-29T00:09:03.535163+00:00'
page_id: '381048036'
product: rm
source: tdn-rm
title: 1310607 DSAUGHSCC-266 Lentidão na geração do Livro de Psicotrópicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=381048036
version: 2
---

# ntidão na geração do Livro de Psicotrópicos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Livro de Medicamentos Controlados | sadLivroMedCtrl,   ``` SauLivroServer ``` |  |  | | --- | | **Rotina(s) envolvida(s)** | | Parâmetros gerais | |  | |
| **Parâmetro(s):** | Informe os parâmetros utilizados. |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Esta implementação consiste em diminuir o tempo de processamentos dos itens que compõem o livro de medicamentos controlados quando integrado com o EMS (Datasul)

## Procedimento para Utilização

1. Se  o sistema não estiver integrado com o EMS, não prossiga com os passos seguintes
2. Caso a inclusão dos itens do Livro de medicamentos controlados esteja muito lenta, tente parametrizar o sistema para utilizar múltiplas faixas para consulta ao EMS. Se os códigos dos medicamentos controlados sejam muito espalhados, é aconselhado a utilizar este modelo.
3. Acesse o menu Opções / Parâmetros / Parâmetros Gerais. página "Med. Controlados"
4. Acesse a subpágina "Configurações"
5. Marque a opção "Utiliza modelo multifaixas de itens"
6. O campo "Quantidade permitida de itens que não são controlados dentro de cada faixa", já vem com um valor default de 20. Este valor pode ser alterado para se chegar a um bom tempo de processamento .
