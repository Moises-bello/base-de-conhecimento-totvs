---
content_hash: ebbb6cd3346668cd877849e020e81f745251aa57620b5801250fc6bad0410a27
fetched_at: '2026-06-29T00:08:43.623100+00:00'
page_id: '305923041'
product: rm
source: tdn-rm
title: 1185478 FINANCEIRO01-2372 Desabilitar controle de histórico de alteração de
  lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=305923041
version: 97
---

# DESABILITAÇÃO DO CONTROLE DE HISTÓRICO DE ALTERAÇÃO DE LANÇAMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Controle de histórico de alteração de lançamentos. |
| **Situação/Requisito:** | Ao tentar desabilitar o controle de histórico de alteração de lançamentos é apresentada a seguinte mensagem: “O Controle de Histórico de Alterações é Obrigatório para cliente do TIN”. Porém, o cliente não utiliza o TIN – TOTVS Incorporação. |
| **Solução/Implementação:** | Será verificada a seguinte regra, em relação ao Totvs Incorporação, para definir se o controle de histórico de alteração de lançamentos pode ser desabilitado:   * Se o cliente possui alguma venda cadastrada, ou seja, o cliente está utilizando o TIN; * A a base é revitalizada. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 1185478. |
| **Requisito:** | FINANCEIRO01-2372. |

divs
