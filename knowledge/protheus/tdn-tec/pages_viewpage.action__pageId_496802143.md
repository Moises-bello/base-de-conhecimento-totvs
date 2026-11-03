---
content_hash: 9ae0f88ff062c0d647d24dd04c2db89124477535ffd4c9a6a723eb4ec1646cda
fetched_at: '2026-07-02T19:24:25.070446+00:00'
page_id: '496802143'
product: protheus
source: tdn-tec
title: Implementação - Método pra limpar o cache de navegação do TWebEngine
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496802143
version: 1
---

Foi criado o método TWebEngine:ClearCache().

|  |  |
| --- | --- |
| Situação | Não existe possibilidade de limpar o cache de navegação do TWebEngine no SmartClient desktop. |
| Ocorrência | É necessário criar um método pra que o cache de navegação seja limpo evitando problemas com carregar partes antigas das páginas. |
| Implementação | Criado o método TWebEngine:ClearCache() que apaga o cache de navegação. |
| Informações adicionais | * Referente à ocorrência: ITEC-423 * Disponível em builds superiores a 17.3.0.8 |
