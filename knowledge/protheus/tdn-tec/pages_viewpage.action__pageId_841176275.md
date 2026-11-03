---
content_hash: eae613dea755ef51be68e751f07227e5eaf3c85e63f8de876a9571a4b43d2065
fetched_at: '2026-07-02T19:24:28.730475+00:00'
page_id: '841176275'
product: protheus
source: tdn-tec
title: Correção - Impressão de PDF via TWebEngine não imprime cores de fundo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=841176275
version: 2
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Situação | Ao usar os métodos Print() e/ou PrintPDF de uma página html, as cores de fundo existentes não eram impressas no PDF. |
| Ocorrência | As cores de fundo não apareciam em impressões de páginas HTML |
| Correção | Uma propriedade específica de impressão de fundo precisou ser explicitamente ligada para que  as cores de fundo de uma página html fossem impressas quando utilizado PrintPDF.  Não foi possível a correção para o Print por limitações técnicas. |
| Informações adicionais | * Referente ao chamado: [19513827](https://suporte.totvs.com/portal/p/10098/consulta-tickets?ticket=19513827) * Referente à ocorrência: [DTCLIENT01-4631](https://jiraproducao.totvs.com.br/browse/DTCLIENT01-4631) * Disponível em builds superiores a 20.3.2.6 |
