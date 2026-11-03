---
content_hash: 3a4570143f7b1f6bbc87245d3a7255b6a0a9b81bee1d1ac272f31856de362c04
fetched_at: '2026-07-02T19:24:28.644894+00:00'
page_id: '804055280'
product: protheus
source: tdn-tec
title: Correção - Campo de entrada de texto em POUI não aceita caracteres acionados
  com Alt Gr
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=804055280
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Situação | Ao tentar entrar um caracter que é acionado com Alt Gr (Ex: Alt Gr+Q = ä), o campo de input de uma tela qualquer em POUI não o apresenta |
| Ocorrência | Por um problema interno do QCefView, caracteres acionados com Alt Gr não eram exibidos em campos de input com POUI |
| <Tipo de alteração (correção, implementação, melhoria, homologação)> | Aplicado correção do projeto QCefView no fonte KeyboardUtils que trata a funcionalidade do Alt Gr |
| Informações adicionais | * + Referente ao chamado: [18353862](https://suporte.totvs.com/portal/p/10098/consulta-tickets?ticket=18353862) * Referente à ocorrência: [DTCLIENT01-4361](https://jiraproducao.totvs.com.br/browse/DTCLIENT01-4361) * Disponível em builds superiores a  7.00.210324P - 20.3.2.1 |
