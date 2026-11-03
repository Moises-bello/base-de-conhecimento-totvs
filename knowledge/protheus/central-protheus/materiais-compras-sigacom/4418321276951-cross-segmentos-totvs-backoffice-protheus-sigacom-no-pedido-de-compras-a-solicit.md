---
article_id: 4418321276951
category: Materiais - Compras (SIGACOM)
content_hash: 40b34200cfd93e9d139180ea33f0001067e029865135c041803a1c53cf764399
fetched_at: '2026-06-28T22:41:21.923902+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - No Pedido de Compras
  a Solicitação de Compras de Produto Importado ( Legenda Rosa ) não é listada para
  ser selecionada
type: support-article
updated_at: '2025-11-03T19:39:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418321276951-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-No-Pedido-de-Compras-a-Solicita%C3%A7%C3%A3o-de-Compras-de-Produto-Importado-Legenda-Rosa-n%C3%A3o-%C3%A9-listada-para-ser-selecionada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36074926467863) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**No Pedido de Compras a Solicitação de Compras Produto Importado ( Legenda Rosa ) não é listada para ser selecionada  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões  
  
**Solução**A Solicitação de Compras de Produto Importado, significa que foi incluída com um Produto Importado ficando com legenda "Rosa" conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418339888407)

Abaixo também o campo "B1\_IMPORT" do cadastro do produto que define ele ser "Importado":

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418333041815)

As SCs com produtos cadastrado desta forma (que ficam com a Legenda Rosa), conforme a instrução do campo do Produto, são utilizadas apenas para Integração com o módulo SIGAEIC.

Para uso de SC na rotina de Pedido de Compras devem ser utilizadas SCs com Produto com o campo B1\_IMPORT = Não, que quando incluídas ficam com o Status "Verde - Solicitação Pendente".

***Exemplo:***

SC Cadastrada (Produto com B1\_IMPORT = Não):

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418333048983)

Abaixo na rotina de Pedido de Compras, verifica-se a SC de status Verde disponível para ser selecionada:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418333081879)

***Obs1:***

Observar que a SC de Produto Importação (de legenda Rosa) corretamente não é listada para ser selecionada.

***Obs2:***

Caso seja necessário, é possível editar uma Solicitação de Compras de Importação. Segue exemplo do GIF abaixo.

![Gravar_2025_10_31_17_39_36_737-ezgif.com-video-to-gif-converter (1).gif](https://centraldeatendimento.totvs.com/hc/article_attachments/36074905709463)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
