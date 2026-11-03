---
article_id: 6530811825943
category: Materiais - Compras (SIGACOM)
content_hash: 733a4ba2df3d54ced79bd12396d356f37f3e8d83194f93a302a6833be1146950
fetched_at: '2026-06-28T22:41:11.737072+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Qual a Funcionalidade
  do Parâmetro MV_HISTAPC - Histórico de Aprovação / Alteração de Pedido de Compras
  ?
type: support-article
updated_at: '2025-09-15T16:20:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6530811825943-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Qual-a-Funcionalidade-do-Par%C3%A2metro-MV-HISTAPC-Hist%C3%B3rico-de-Aprova%C3%A7%C3%A3o-Altera%C3%A7%C3%A3o-de-Pedido-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24342789480471) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Qual a funcionalidade do parâmetro MV\_HISTAPC ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**

Na rotina Pedido de Compras (MATA120), esta é uma funcionalidade de consulta do histórico de aprovação do pedido de compras para os pedidos que possuem controle de alçada.

***Obs.:***

*O intuito desta opção é gravar apenas as **alterações**realizadas no pedido de compra.*

*Para verificar o histórico e fluxo das aprovações existentes e já realizadas, clicar no botão "Aprovac" onde será apresentado o log de aprovações.*

Habilitando o parâmetro MV\_HISTAPC = .T. , ao visualizar o Pedido de Compras (MATA121) em Outras Ações, será habilitada a opção 'Hist Aprov'

![imagem5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6529497102359)

O parâmetro tem a finalidade de gravar o histórico de alterações do Pedido de Compras e do Item do Pedido quando houver fluxo de Alçada, após ou mesmo antes de suas respectivas aprovações, não tratando alterações de Solicitação de Compras.

![Hist_rico.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/6530783269399)

**Observação**:

Esta funcionalidade não gera registro na tabela SGV de Histórico logo na inclusão do Pedido com alçada, e nem ao ser realizada a liberação de alçada do Pedido, mas somente na Alteração do Pedido posteriormente de ter sido incluído.

Para verificar as Aprovação do Pedido / Item do Pedido é necessário realizar a consulta no botão "Outras Ações > Aprovac." da imagem abaixo:

![imagem6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6529603198231)

É nessa funcionalidade que é realizada a consulta do Tipo de Documento, Aprovador Responsável, Situação Atual e Data de Liberação.

***Saiba Mais:***

* [TRXNNX\_DT\_HISTORICO\_DE\_APROVACAO\_DO\_PEDIDO\_DE\_COMPRAS](https://tdn.totvs.com/x/wIE_Dw)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
