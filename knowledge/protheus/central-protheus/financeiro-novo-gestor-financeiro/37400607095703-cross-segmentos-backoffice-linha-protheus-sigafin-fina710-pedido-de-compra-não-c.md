---
article_id: 37400607095703
category: Financeiro - Novo Gestor Financeiro
content_hash: b88fb431ad3b71d1b901e1c1cad88fab3062de6cc7f9bbc64a9ad2032b5bdd2e
fetched_at: '2026-06-28T22:37:41.586724+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN – FINA710 - Pedido de
  compra não considerar data de emissão
type: support-article
updated_at: '2026-01-02T18:59:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37400607095703-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Pedido-de-compra-n%C3%A3o-considerar-data-de-emiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37400607078807) Tempo aproximado para leitura: 00**:05:00 min**  
  
**Dúvida**  
Ao incluir um pedido de compra com data de emissão futura o sistema considera a data base para exibi-lo no consolidado do Novo Gestor Financeiro (FINA710)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
   a) Se a data de entrega do pedido é maior ou igual a data de execução do job, o campo F76\_DATA é gravado com o resultado da data de entrega + dias da condição de pagamento (vide exemplo cenário 1);

    b) Se a data de entrega do pedido é menor que a data de execução do job, o campo F76\_DATA é gravado com o resultado da data de execução do job + dias da condição de pagamento (vide exemplo cenário 2).  
  
Ou seja, caso deseje incluir um pedido de compra com data futura, para exibição com essa data no novo gestor financeiro (FINA710) deve ser alterado o campo "data entrega" dos itens no pedido de compra, como na imagem abaixo:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37400592632471)

Dessa forma, a exibição no novo gestor na aba consolidado irá considerar está data + os dias cadastrados na condição de pagamento utilizada, como na imagem abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37400607083287)

**Saiba Mais:**  
[Gravação da tabela F76 - FINA711](https://tdn.totvs.com/pages/releaseview.action?pageId=709395826)
