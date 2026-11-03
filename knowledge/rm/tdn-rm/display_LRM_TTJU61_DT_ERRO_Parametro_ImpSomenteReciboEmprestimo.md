---
content_hash: f36132e495f5d842a635c6608ec201de0b2d278c016ca18fb1432853280be7b6
fetched_at: '2026-06-29T00:06:14.658598+00:00'
page_id: '210048381'
product: rm
source: tdn-rm
title: TTJU61_DT_ERRO_Parametro_ImpSomenteReciboEmprestimo
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJU61_DT_ERRO_Parametro_ImpSomenteReciboEmprestimo
version: 2
---

# EMPRÉSTIMO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Bibliotecária* |
| **Função:** | *Empréstimo* |
| **Situação/Requisito:** | *O sistema não está respeitando o parâmetro configurado. Favor verificar como proceder para regularizar a rotina, pois temos um grande volume de empréstimos e o fato de visualizar os recibos atrasa muito a rotina.* |
| **Solução/Implementação:** | *O método responsável por validar o parâmetro ImpSomenteReciboEmprestimo estava realizando a validação em um determinado ponto, que, para alguns registros, estava validando erroneamente o cenário de Renovação de empréstimo.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *N/A* |
| **Versão Corrigida:** | *12.1.8* |
| **Versão Expedida:** | *Versão em que o programa será oficialmente expedido.* |

divs

```
ImpSomenteReciboEmprestimo
```
