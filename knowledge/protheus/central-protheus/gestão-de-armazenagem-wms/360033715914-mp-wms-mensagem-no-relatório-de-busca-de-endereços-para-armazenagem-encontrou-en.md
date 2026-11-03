---
article_id: 360033715914
category: Gestão de Armazenagem (WMS)
content_hash: 3e45f5c0554ebc39116bc23820fe17a265eec3ca640f1b7b2cf6de85de350cdd
fetched_at: '2026-06-28T22:45:48.202276+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: 'MP - WMS - Mensagem no relatório de busca  de endereços para armazenagem:
  Encontrou endereço de picking. Múltiplos = Não'
type: support-article
updated_at: '2019-12-27T11:55:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033715914-MP-WMS-Mensagem-no-relat%C3%B3rio-de-busca-de-endere%C3%A7os-para-armazenagem-Encontrou-endere%C3%A7o-de-picking-M%C3%BAltiplos-N%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)***Tempo aproximado para leitura:**00:00:48 min**  
 **Dúvida**Por que ocorre no relatório de busca de endereços para armazenagem a mensagem: Encontrou endereço de picking. Múltiplos = Não?  
   
 **Ambiente**Microsiga Protheus – Gestão de Armazenagem – A partir da versão 11.80  
  
**Solução**No caso de armazenamento priorizando o *picking*, serão levados em conta os parâmetros **MV\_WMSMULP - Considera múltiplos endereços de *picking*** e **MV\_WMSNRPO - Limite de endereços de *picking* ocupados**. Onde, caso esteja parametrizado para utilizar múltiplos *pickings*, será respeitado o limite de endereços definido através da outra parametrização.  
  
Logo, se já existir endereço de *picking* ocupado para o produto e o parâmetro **MV\_WMSMULP** estiver configurado como **N,** o sistema não conseguirá fazer o armazenamento e apresentará no relatório de busca de endereços para armazenamento a mensagem: Encontrou endereço de *picking*. Múltiplos = Não.
