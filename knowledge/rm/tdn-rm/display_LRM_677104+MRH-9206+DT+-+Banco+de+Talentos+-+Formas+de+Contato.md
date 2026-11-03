---
content_hash: ed4d0a55ff6fc3181dc1b4e6d7eb9bcb697489be05a6d9f004c8bb6367cb5238
fetched_at: '2026-06-29T00:08:30.375658+00:00'
page_id: '272428051'
product: rm
source: tdn-rm
title: 677104 MRH-9206 DT - Banco de Talentos - Formas de Contato
type: documentation
url: https://tdn.totvs.com/display/LRM/677104+MRH-9206+DT+-+Banco+de+Talentos+-+Formas+de+Contato
version: 105
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | Bairo |
| **Situação/Requisito:** | Ao preencher os dados do campo bairro no painel de opções FORMAS DE CONTATO ocorre erro. |
| **Solução/Implementação:** | O problema estava acontecendo quando tentava salvar mais de uma vez o registro de bairro no mesmo dia. Pois quando salvava a tela era preenchido um historico na tabela PFHSTEND. Mas na tabela CODPESSOA E DTMUDANCA são KEYS e o sistema estava tentando criar um novo registro com datas iguais, pois ele não gerava data com hora e somente a data. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | MRH-9206 |
| **Requisito:** |  |

divs
