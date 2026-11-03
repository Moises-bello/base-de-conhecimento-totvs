---
content_hash: 640c5dd696d820a022ec0b060be4fdcbaa53fcf5b18f756de5c4b4e484498dc6
fetched_at: '2026-06-29T00:08:35.604876+00:00'
page_id: '281985771'
product: rm
source: tdn-rm
title: 956135 EDUCACIONAL01-1287 DT Erro ao imprimir boleto via webservice
type: documentation
url: https://tdn.totvs.com/display/LRM/956135+EDUCACIONAL01-1287+DT+Erro+ao+imprimir+boleto+via+webservice
version: 106
---

# GERAÇÃO DE LANÇAMENTOS FINANCEIROS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de lançamentos financeiros |
| **Situação/Requisito:** | Ao executar a impressão de boletos via webservice está ocorrendo exceção de referência nula de objeto devido a não existência de um contexto válido. |
| **Solução/Implementação:** | Foi realizada otimização do processo de impressão de boletos via webservice, permitindo ao sistema, retornar os dados do relatório nos casos onde o contexto não é válido.  **Importante:**   * Quando o relatório utilizado é visível a todas coligadas, é importante a alteração da propriedade "Dados de todas as coligadas" para **Verdadeiro,** para que o sistema consiga encontrar as informações do boleto impresso. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
