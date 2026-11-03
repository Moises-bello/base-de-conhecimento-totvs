---
content_hash: 5022aeb276c9ccc6432e355a1ee6cb1bd466fee974f2ad7bd938ab7d056716cf
fetched_at: '2026-06-29T00:08:46.371619+00:00'
page_id: '317292546'
product: rm
source: tdn-rm
title: 1389784 FINANCEIRO01-2877 DT Campo evento contábil para caixa de cartão de
  crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317292546
version: 93
---

# BAIXA DE LANÇAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Baixa de Lançamento |
| **Situação/Requisito:** | Ao realizar o recebimento via cartão de credito/debito(Checkout Cielo), o sistema está utilizando o evento contábil incorreto na contabilização de baixa. O sistema está buscando o Evento Contábil na opção "Evento Contábil para Baixa Contábil” ou “Evento Contábil para Baixa" da tabela Default para Evento, sendo que o correto seria buscar da opção “Evento Contábil para Baixa de Cartão de Crédito”, |
| **Solução/Implementação:** | Ajuste no serviço de baixa de lançamento de cartão de crédito para buscar o evento contábil corretamente. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000040 |

divs
