---
content_hash: bc68845d5339ba217cb67844dd38760b722e74ae121351db257026c628d95e20
fetched_at: '2026-06-29T00:10:15.401748+00:00'
page_id: '464966535'
product: rm
source: tdn-rm
title: DEDUMOBILE-1757 DT EducaMobile - Cache do Host com problema quando existe mais
  de um host no EducaMobile
type: documentation
url: https://tdn.totvs.com/display/LRM/DEDUMOBILE-1757+DT+EducaMobile+-+Cache+do+Host+com+problema+quando+existe+mais+de+um+host+no+EducaMobile
version: 2
---

# TOTVS EDUCA MOBILE - Mensagens Pessoais (eduCONNECT)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | eduCONNECT |
| **Função:** | Mensagens |
| **Situação/Requisito:** | Ao acessar o menu: Mensagens, o app não está validando o token do usuário. Com isso não conseguimos acessar a funcionalidade. O erro ocorre no Android e IOS. |
| **Solução/Implementação:** | Realizado ajuste no momento da geração do Token de mensagens pessoais, para que seja replicado o token em todos os hosts configurados no web.config. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
