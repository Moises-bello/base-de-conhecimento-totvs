---
content_hash: cb76a62dd5696992f4b7982210ce1fb0d5e81f52e9014d4aa57e7e3527c5b656
fetched_at: '2026-06-29T00:10:13.778778+00:00'
page_id: '458756896'
product: rm
source: tdn-rm
title: DT - Número de Registros por Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458756896
version: 8
---

# NÚMERO DE REGISTROS POR LOTE

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | BackOffice |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Regeração de Saldos e Custos | EstRegerarSaldosECustosProcAction | |
| **Parâmetro(s):** | 04.04.01 - Definições de Estoque |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | Totvs0c783de1-186e-383b-975c-a1acd7d76cb5MATESTCNTFTOF01-4821 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL, Oracle |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | 12.1.24 |

## Descrição

Foi criado o parâmetro Número de Registros por Lote. Ele é utilizado no processo de Regeração de Saldos e Custos para definir a quantidade de registros a ser inserida no banco a cada atualização. Por default o parâmetro é definido com o valor de 20.000, mas é possível informar valores entre 1 e 30.000. Este valor pode gerar erro de TimeOut ao inserir os registros se o mesmo tiver muito elevado para o SGBD, por isso é necessário atentar para este parâmetro que esta em Definições de Estoque e se necessário diminuir o valor.
