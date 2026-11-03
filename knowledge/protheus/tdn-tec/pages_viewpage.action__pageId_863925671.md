---
content_hash: 5757633a85b9f0a69191f01319c764f482093a7f5e4c1e3a892001ee9df534b2
fetched_at: '2026-07-02T19:24:28.878465+00:00'
page_id: '863925671'
product: protheus
source: tdn-tec
title: Correção - Drag and Drop em componente POUI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=863925671
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Situação | O Drag and Drop não funciona no componente "Upload" do POUI |
| Ocorrência | Dados de Drag And Drop eram enviados para o javaScript de uma forma diferente de um Browser, o que causou o componente do POUI não funcionar corretamente |
| Correção | Corrigido a forma como os dados de um drag and drop de arquivo é feita, para que tenha o mesmo comportamento do browser |
| Informações adicionais | * Referente ao chamado: [#20646246](https://suporte.totvs.com/portal/p/10098/consulta-tickets?ticket=20646246) * Referente à ocorrência: DTCLIENT01-4918 * Disponível em builds superiores a 20.3.2.9 |
