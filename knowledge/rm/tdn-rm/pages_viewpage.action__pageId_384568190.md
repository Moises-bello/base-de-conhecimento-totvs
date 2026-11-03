---
content_hash: e3d560a85c80c8d18592585c3a0bbc3164e68609ebd02d20473b75863fa164de
fetched_at: '2026-06-29T00:09:07.146609+00:00'
page_id: '384568190'
product: rm
source: tdn-rm
title: 1287907 MATESTCNTFTOF01-614 DT LOG da Regeração de Saldos e Custos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=384568190
version: 82
---

# LOG da Regeração de Saldos e Custos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Gestão de Estoque, Compras e Faturamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *REGERAÇÃO DE SALDOS E CUSTOS* | *EstRegerarSaldosECustosProcAction* | |
| **Cadastros Iniciais:** | LOG da Regeração de Saldos e Custos. |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | **N/A** |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATESTCNTFTOF01-614 |
| **País(es):** | **Brasil** |
| **Banco(s) de Dados:** | **SQLServer e Oracle** |
| **Tabelas Utilizadas:** | *TRELSLD, **TITMMOV, *TPRODUTODEF, TPRDLOC**** |
| **Sistema(s) Operacional(is):** | **Windows** |

## Descrição

Criação de flag "Gravar Arquivo de Log" que permite o processo de Regeração de Saldos e Custos a gravar o Log fisicamente a cada produto regerado. Utilizando este parâmetro, a cada produto regerado, o arquivo de Log será atualizado com as informações da regeração daquele produto, informando se ocorreu algum erro ou se obteve sucesso. Caso não marque esta opção, será exibido o Log na tela no final do processo, porém não ficará gravado em nenhum lugar.

Se a flag "Usar Log Detalhado" for marcada, o Log será gerado com informações adicionais, especificando movimentações do produto. Observe que neste caso a performance poderá diminuir.

Para que o arquivo seja gravado corretamente, deve-se especificar corretamente o FileServerPath no RM.HOST, conforme documentação abaixo:

**Obs.: Caso o FileServerPath não seja configurado corretamente no RM.HOST, o arquivo de Log será gravado por Default na pasta "Arquivos" dentro do diretório onde o RM.HOST se encontra.**

divs
