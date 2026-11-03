---
content_hash: 218c027777601fd7b473f9ef394d05fd2ee8c70a72929ad9478a03e27ef3a380
fetched_at: '2026-06-29T00:08:47.090374+00:00'
page_id: '318605942'
product: rm
source: tdn-rm
title: 1770373 EDUCACIONAL01-3340 DT Classificao por Nota Criterio Desempate
type: documentation
url: https://tdn.totvs.com/display/LRM/1770373+EDUCACIONAL01-3340+DT+Classificao+por+Nota+Criterio+Desempate
version: 91
---

# CLASSIFICAÇÃO DE CANDIDATOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Classificação de candidatos* |
| **Situação/Requisito:** | *F**oi identificado uma inconsistência na classificação de candidatos quando utilizado o processo de desempate por prioridade de prova. Foi analisado e identificado que o problema ocorre por uma inconsistência da tecnologia .net, as notas de um candidato após um somatório no formato "double (.net)", deveria ser igual a 11.9, porém fica "11.8999999..." o que no momento da comparação da nota entre outro candidato que possui a mesma nota 11.9 ocorre a inconsistência no desempate.* |
| **Solução/Implementação:** | *Foi feito um ajuste no código para que a soma não tenha distorções na sua parte decimal assim o desempate ocorrerá sempre normalmente.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs

oi identificado uma inconsistência na classificação de candidatos quando utilizado o processo de desempate por prioridade de prova. Foi analisado e identificado que o problema ocorre por uma inconsistência da tecnologia .net, as notas de um candidato após um somatório no formato "double (.net)", deveria ser igual a 11.9, porém fica 11.8999999... o que no momento da comparação da nota entre outro candidato que possui a mesma nota 11.9 ocorre a inconsistência no desempate.Foi feito um ajuste no código para que a soma não tenha distorções na sua parte decimal assim o desempate ocorrerá sempre normalmente.
