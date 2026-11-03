---
content_hash: 531067a7541af5f6bdddf9657c05e31a22d1c10772baa3bfe660d737a46a0822
fetched_at: '2026-06-29T00:08:31.112291+00:00'
page_id: '272717099'
product: rm
source: tdn-rm
title: 196042 MRH-5664 DT Restituicao 1 Centavo INSS Ferias
type: documentation
url: https://tdn.totvs.com/display/LRM/196042+MRH-5664+DT+Restituicao+1+Centavo+INSS+Ferias
version: 108
---

# ARREDONDAMENTO GERANDO RESTITUIÇÃO DE 1 CENTAVO NO INSS DE FÉRIAS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projeto |
| **Módulo:** | Folha de Pagamento |
| **Função:** | INSS Férias |
| **Situação/Requisito:** | Quando é calculado o recibo de férias com o parâmetro "Arredondar valores" da Tabela de INSS marcado, e antes de efetuar o lançamento das férias para o envelope esse parâmetro é desmarcado, está sendo incluído na movimentação um valor de 1 centavo de restituição de INSS. |
| **Solução/Implementação:** | Ajuste no cálculo de INSS para ignorar restituição de 1 centavo no caso de lançamento de férias para o envelope. |
| **Tickets relacionados:** | MRH-5664 |

divs
