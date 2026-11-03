---
article_id: 360022582991
category: ADVPL - Ponto de Entrada
content_hash: 81e99962751b2f34250eab2f3bf0dacd2d201d41cd1aeaa5b3b68a0b5a34677b
fetched_at: '2026-06-28T22:40:12.740274+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  OS010BTN '
type: support-article
updated_at: '2021-12-29T17:49:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022582991-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-OS010BTN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Existe algum exemplo do Ponto de Entrada OS010BTN ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**

Segue exemplo do ponto de entrada [OS010BTN - Adiciona Botões](https://tdn.totvs.com/pages/releaseview.action?pageId=631330230)

```
User Function OS010BTN()  
  
 Local aButtons := {}  
   
 //Adicionando o botão no Ações Relacionadas  
 aAdd(aButtons,{ "* Atualiza Produtos", {|| u_suafuncao()}, "* Atualiza Produtos" })  
  
Return aButtons
```
