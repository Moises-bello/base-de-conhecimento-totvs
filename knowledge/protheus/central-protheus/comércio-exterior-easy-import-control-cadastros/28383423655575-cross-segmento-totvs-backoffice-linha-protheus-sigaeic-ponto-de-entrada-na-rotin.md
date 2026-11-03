---
article_id: 28383423655575
category: Comércio Exterior - Easy Import Control - Cadastros
content_hash: 1d1ced33987479da63efa875598b8205cceebf719e0305bd4d4be6d9590bd788
fetched_at: '2026-06-28T22:39:52.277670+00:00'
product: protheus
section_id: 1500001549382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Ponto de Entrada
  na rotina de Condições de Pagamento (EICA060)
type: support-article
updated_at: '2024-12-11T12:07:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28383423655575-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Ponto-de-Entrada-na-rotina-de-Condi%C3%A7%C3%B5es-de-Pagamento-EICA060
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28383423640343) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ponto de entrada para manipular o Menu "**Outras Ações**" do Cadastro de Condições de Pagamento do SIGAEIC (EICA060).  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - *Easy Import Control* - a partir da versão 12  
  
**Solução**  
Segue abaixo o exemplo do Ponto de Entrada:

```
#INCLUDE 'PROTHEUS.CH'  
  
User Function IA060MNU()  
Local aRotAdic := {}  
  
Aadd(aRotAdic, { 'Sua Rotina', "Sua_funcao" , 0 , 6})  
  
return aRotAdic
```

**Saiba Mais:**  
[PE IA060MNU Menu Cadastro de cond. de pagamento.](https://tdn.totvs.com/pages/releaseview.action?pageId=843146789)  
[Condições de Pagamento (EICA060 - SIGAEIC)](https://tdn.totvs.com/pages/viewpage.action?pageId=312159046)
