---
article_id: 360021602612
category: Financeiro - Contas a Pagar
content_hash: 7be7cd58d94e5924e69234b4c606474c3ed7bc4996c21e66023d03355373247e
fetched_at: '2026-06-28T22:38:06.946241+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Exclusão de Nota fiscal
  de entrada com conciliação DDA no financeiro
type: support-article
updated_at: '2022-04-11T16:54:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021602612-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Exclus%C3%A3o-de-Nota-fiscal-de-entrada-com-concilia%C3%A7%C3%A3o-DDA-no-financeiro
---

**Ocorrência**Nos módulos **Compras ou Financeiro**, ao tentar realizar **a exclusão de uma nota de entrada ou contas a pagar,** é apresentada a mensagem **"FIN050DDA - O titulo não pode ser excluído pois foi conciliado por DDA"**  
  
**Ambiente**  
Microsiga Protheus – Compras/Financeiro – A partir da versão 12  
  
**Causa**   
Esse incidente ocorre, pois o título a pagar teve uma conciliação DDA, portanto para que possa excluir a nota ou o título, será necessário efetuar o cancelamento da conciliação.  
  
**Solução**  
Para efetuar o cancelamento, realize os seguintes passos:

**1.** Acesse o módulo Financeiro e em Em “Atualizações/Comunic. Bancária/Conciliação DDA” (FINA260), posicione o cursor sobre um registro com legenda verde (conciliado). Clique na opção “Cancelar”.  
**2.** Serão apresentados os dados do registro DDA (tabela FIG) e do registro de Contas a Pagar (tabela SE2).  
**3.** Confira os dados e confirme.
