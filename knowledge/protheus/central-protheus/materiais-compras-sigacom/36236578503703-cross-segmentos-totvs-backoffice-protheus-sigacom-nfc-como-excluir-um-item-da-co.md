---
article_id: 36236578503703
category: Materiais - Compras (SIGACOM)
content_hash: 29b60f3afba6fefaa647d4c0fd79c9788ead96087bb496a04d2fce5fe681c352
fetched_at: '2026-06-28T22:41:21.733914+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Como excluir
  um item da cotação?
type: support-article
updated_at: '2025-11-10T19:56:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36236578503703-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Como-excluir-um-item-da-cota%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36236607077015) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
No Novo Fluxo de Compras, existe a possibilidade de excluir um código de produto de todas as propostas de uma cotação? 

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2310

**Solução**  
Sim, na tela de **Editar Cotação**, temos um grupo inicial chamado **Itens da Cotação.**

Ao clicar nesse grupo, a lista é expandida e exibe todos os itens que estão associados na cotação atual, ou seja, exibe os produtos que estão sendo cotados. Caso entenda que um item não seja mais necessário e deseja excluir esse item da cotação, temos a opção **Remover**, que fica na frente de cada item constante na cotação.

Ao clicar em remover, o sistema exibe uma modal, informando se deseja realmente excluir o item da cotação, detalhando o item selecionado e informando que ao realizar a remoção, não é possível reverter o processo.

**Atenção:** Caso o item a ser deletado tenha sido agrupado, apesar de ser mostrado separadamente cada item no grupo **Itens da Cotação**, ao excluir qualquer um que esteja no agrupamento, todos serão deletados, visto que o sistema grava o agrupamento como item único na SC8.

**Observação**

Caso ocorra um dos erros abaixo:

PG020NODELITEM Não foi possível excluir o item XXXX pois ele foi respondido por um ou mais fornecedores

Http failure response for http://linknfc 400 Bad Request

Será necessário verificar se o item em questão já foi preenchido por algum fornecedor participante dessa cotação.

![](https://tdn.totvs.com.br/download/attachments/680260500/editar_itens_cotacao.gif?version=1&modificationDate=1716921471697&api=v2)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36236607077527)

***Saiba Mais:***

[Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-))
