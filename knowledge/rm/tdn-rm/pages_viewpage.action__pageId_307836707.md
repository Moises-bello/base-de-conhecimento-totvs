---
content_hash: 3fee29bdabfb60fdf845c945bbceab4ac393022fac513855ee7d9d7a91921e8d
fetched_at: '2026-06-29T00:08:43.991658+00:00'
page_id: '307836707'
product: rm
source: tdn-rm
title: 1513672 FINANCEIRO01-3276 Lançamento - Boleto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=307836707
version: 95
---

# Lançamento - Boleto

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Lançamento - Boleto |
| **Situação/Requisito:** | Ao executar a geração de um boleto via Web Service, o sistema não está registrando o boleto automaticamente, sendo que ao realizar a geração do boleto via sistema, o mesmo é registrado corretamente. |
| **Solução/Implementação:** | Apresentar o Log via WebService. O sistema executava a geração do boleto mas ao registrar o banco retornava uma informação onde era camuflada para as chamadas via WebService. A partir de agora o ProcessServerName a ser executado no XML deverá ser o " FinBoletoInclusaoTBCData ". |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000268 |

divs
