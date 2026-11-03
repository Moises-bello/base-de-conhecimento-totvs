---
article_id: 360028450352
category: ADVPL - Ponto de Entrada
content_hash: 032336a9997c2eac577a31d3631c822c58c669270f23c9989425441859459378
fetched_at: '2026-06-28T22:40:11.628482+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Alterar mensagem
  M-Messenger
type: support-article
updated_at: '2022-06-21T18:03:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028450352-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Alterar-mensagem-M-Messenger
---

**Dúvida**  
Na inclusão do pedido de compras, é enviado um e-mail com mensagem padrão do sistema, é possível customizar esta mensagem?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões  
  
**Solução**Para alterar ou substituir a mensagem que será enviada por e-mail conforme o evento do   
M-Messenger utilizado, utilize o ponto de entrada **MMENS.**Para utilização do Ponto de Entrada **MMENS**, deve-se criar a função de usuário de nome **MMENS+(Código do Evento)**, para que a alteração da mensagem seja processada no evento cadastrado.

Ex.: MMENS001 para personalizar a mensagem do evento de ponto de pedido.

```
User Function MMENS001()  
  
Local aDados       := ParamIXB[1]  
Local cMensagem := ParamIXB[2]  
  
// Customizações da mensagem conforme regra de negócio praticada.  
cMensagem := "Alteração da Mensagem"  
  
Return(cMensagem)
```

**Saiba Mais  
[MMENS - Processamento de Mensagem Enviada por E-Mail](http://tdn.totvs.com/display/public/PROT/MMENS+-+Processamento+de+Mensagem+Enviada+por+E-Mail)**
