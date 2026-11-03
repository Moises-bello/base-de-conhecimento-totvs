---
article_id: 360020337112
category: ADVPL - Ponto de Entrada
content_hash: 070ad8b40c707e69741d1b22d2fd802594767929170deca52d2eafd941d4223c
fetched_at: '2026-06-28T22:40:12.688861+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  MTA241MNU
type: support-article
updated_at: '2021-12-29T18:12:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020337112-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MTA241MNU
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Gostaria de saber se temos disponível nesta rotina Ponto de Entrada, para adicionar botões no menu Outras Ações, dá tela inicial da rotina.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– A partir da versão 11.80  
  
**Solução**Disponível ponto de entrada [MTA241MNU - Altera o Menu](http://tdn.totvs.com/display/PROT/MTA241MNU+-+Altera+o+Menu)

```
#INCLUDE "PROTHEUS.CH"  
  
User Function MTA241MNU()  
   aAdd(aRotina, { "Teste" ,"u_BNT()" , 0 , 3, 0, nil} )  
   Alert("PE MTA010MNU")  
Return  
  
user function BNT  
   Alert("excutou BNT")  
return
```
