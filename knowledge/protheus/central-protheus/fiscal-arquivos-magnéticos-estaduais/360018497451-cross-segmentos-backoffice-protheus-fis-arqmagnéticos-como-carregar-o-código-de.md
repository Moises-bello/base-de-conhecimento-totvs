---
article_id: 360018497451
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: a804ec4492421f1f83ad05503ed7e7a14f22588e20065362639b6237a0539aaa
fetched_at: '2026-06-28T22:42:10.290583+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como carregar
  o código de FCI automaticamente no Pedido de Vendas
type: support-article
updated_at: '2023-06-28T20:45:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018497451-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-carregar-o-c%C3%B3digo-de-FCI-automaticamente-no-Pedido-de-Vendas
---

**Dúvida**Como carregar o código da **FCI** automaticamente no momento da inclusão do **Pedido de Vendas**.  
  
**Ambiente**Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**Para que o código da **FCI** seja carregada no pedido de vendas, é necessario realizar o seguinte procedimento:

1. Configure o parâmetro **MV\_FISAUCF** para .T. ;

2. Configure o parâmetro **MV\_FCIATUC** para .T. ;

3. Verifique se o campo **CFD\_PERCAL** está no mesmo período que a emissão do **Pedido de Vendas**.
