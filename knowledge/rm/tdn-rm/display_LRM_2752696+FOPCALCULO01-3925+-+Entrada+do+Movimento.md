---
content_hash: c1e5becd07c009ce09c8feb1799b2608bf53bdb9430d18a19ccbe86ebfbe4244
fetched_at: '2026-06-29T00:09:01.037287+00:00'
page_id: '370623105'
product: rm
source: tdn-rm
title: 2752696 FOPCALCULO01-3925 - Entrada do Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/2752696+FOPCALCULO01-3925+-+Entrada+do+Movimento
version: 1
---

# Entrada do Movimento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Entrada do Movimento |
| **Situação/Requisito:** | Ao acessar o menu entrada de movimento e acessar a opção digitar por nome, o sistema não respeita a seleção de digitar por nome. Ao abrir o Processo 'Entrada do Movimento', o cursor fica no nome, mas ao clicar em novo, o cursor vai para o campo chapa, mas o correto é o cursor permanecer no campo nome. |
| **Solução/Implementação:** | No Totvs Folha de Pagamento foi identificado uma inconsistência no focus da tela de Entrada do Movimento, mesmo informando o o tipo de digitação por nome, o focus do componente sempre fica no campo chapa. Foi feito um ajuste para que o sistema identifique corretamente qual será o componente do focus e defini-lo corretamente. |
| **Tickets relacionados:** | 2752696 |
