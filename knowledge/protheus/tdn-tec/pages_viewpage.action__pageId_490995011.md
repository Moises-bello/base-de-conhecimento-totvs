---
content_hash: 323d1af3ba02869b891b69b724d90becbceaf7ab9c158aba87255624cb0dfa4f
fetched_at: '2026-07-02T19:24:24.933096+00:00'
page_id: '490995011'
product: protheus
source: tdn-tec
title: Melhoria - TGet ignora caractere TAB na operação de colar texto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490995011
version: 1
---

Melhoria - TGet ignora caractere TAB na operação de colar texto

|  |  |
| --- | --- |
| Situação | O componente TGet do tipo texto aceita o caractere TAB quando um texto é inserido através da operação copiar/colar. |
| Ocorrência | O caractere TAB em algum registro pode causar problemas na geração de relatórios. |
| Melhoria | O componente TGet recebeu uma proteção para substituir o caractere TAB por um caractere de espaço em branco durante as operações de colar texto. |
| Informações adicionais | * Referente ao chamado: 5464574 * Referente à ocorrência: MTEC-2521 * Disponível em builds iguais ou superiores a 13.2.3.41 |
