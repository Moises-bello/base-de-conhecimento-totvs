---
content_hash: dd7357909b44e4739ab7dda12255f432d73f30e0092ab89e0dd170c8b279b4a5
fetched_at: '2026-06-29T00:08:33.517381+00:00'
page_id: '274326350'
product: rm
source: tdn-rm
title: FOPROTINAS01-285 DT GRAFICO COMPARATIVO INSS ONERACAO x DESONERACAO
type: documentation
url: https://tdn.totvs.com/display/LRM/FOPROTINAS01-285+DT+GRAFICO+COMPARATIVO+INSS+ONERACAO+x+DESONERACAO
version: 108
---

# Objeto Gerencial

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Folha de Pagamento. |
| **Função:** | Emissão do Gráfico comparativo INSS Oneração x Desoneração. |
| **Situação/Requisito:** | O Sistema deve prover um comparativo que demonstre os valores da Oneração x Desoneração na folha de pagamento. |
| **Solução/Implementação:** | O sistema passa a disponibilizar o objeto gerencial "FOPGRA0001 - Gráfico Comparativo Desoneração  Orenação.TotvsReport". Este gráfico em barras mostra o valor onerado e o valor desonerado de uma competência de uma Filial ou empresa.      O valor onerado é obtido do envelope de pagamento somando-se a base de INSS Folha e base de INSS 13º  aplicando o percentual de incidência de INSS. Já o valor Desonerado é aplicado o percentual redutor ao valor Onerado:      O Relatório solicita os seguintes dados:    * Seção:  + Orienta-se informa a seção de quebra que represente a Filial ou empresa. Para que seja sumarizado os valores Onerado e Desonerado. + O sistema irá buscar a lotação dos funcionários no histórico de seção de acordo com a competência informada.  * Ano da Competência * Mês da Competência * % Redutor * Coligada * % INSS    . |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | FOPROTINAS01-285. |
| **Requisito:** |  |

divs
