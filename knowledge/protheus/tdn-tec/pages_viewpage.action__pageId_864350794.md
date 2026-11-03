---
content_hash: d4ae9c1b9807a4c9d196f7bf56463a0c51299e14f11aaab2d1ed566cf3531a18
fetched_at: '2026-07-02T19:24:28.882049+00:00'
page_id: '864350794'
product: protheus
source: tdn-tec
title: Correção - Impressão de relatorios em MAC. Sistema operacional IOS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=864350794
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Situação | A visualização de um antigo relatório (com extensão ##r) em Mac estava diferente da versão Windows |
| Ocorrência | Ao abrir a tela de visualização do relatório ".##r" enviado pelo cliente, no Mac, a pagina não cobria todo o relatório. Apenas em Windows |
| Correção | O Mac retorna valores de DPI diferentes do Windows, portanto foi adicionado um tratamento específico para o Mac. |
| Informações adicionais | * Referente ao chamado: [#20254909](https://suporte.totvs.com/portal/p/10098/consulta-tickets?ticket=20254909) * Referente à ocorrência: DTCLIENT01-4857 * Disponível em builds superiores a 20.3.2.9 |
