---
content_hash: aabb51c74847ac0a19b066f70f7de3db777e99a00f0e5481e6c9f66ec989f102
fetched_at: '2026-07-02T19:24:25.138421+00:00'
page_id: '499103645'
product: protheus
source: tdn-tec
title: Correção - TButton em tela touch screen é acionado no segundo toque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=499103645
version: 1
---

Correção - TButton em tela touch screen é acionado no segundo toque

|  |  |
| --- | --- |
| Situação | Quando é utilizado um monitor com tecnologia touch screen, é necessário tocar duas vezes sobre o componente TButton para realizar a ação de clique. |
| Ocorrência | O primeiro toque sobre o TButton coloca o foco no componente, mas somente o segundo toque aciona o botão efetivamente. |
| Correção | Foi aplicada uma correção que adiciona um tratamento especial para o componente TButton quando acionado por eventos de touch screen. |
| Informações adicionais | * Referente ao chamado: 6176406 * Referente à ocorrência: MTEC-2837 * Disponível em builds iguais ou superiores a 7.00.170117A - 17.3.0.9 |
