---
article_id: 360035189994
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: d6ead2d317d05383c0c6c896c0492c3fae66769932e25a11aec11ec3405d0fdb
fetched_at: '2026-06-28T22:38:23.982723+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Configuração
  do portal do cliente
type: support-article
updated_at: '2022-03-22T12:45:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035189994-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Configura%C3%A7%C3%A3o-do-portal-do-cliente
---

**Dúvida**

Configurar o portal do cliente?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões.  
  
**Solução**

*A configuração do portal do cliente, obedece as mesmas premissas do portal do vendedor**: [PPVD0003\_Configuração\_completa\_do\_Portal\_do\_Vendedor](https://tdn.totvs.com/pages/viewpage.action?pageId=236596491)***

A diferença será a inserção do cliente no cadastro do usuário de portal, aba cliente, no mais, as configurações serão as mesmas.

![](https://tdn.totvs.com/download/attachments/514744381/usu%C3%A1rio%20de%20portal-aba%20cliente.gif?version=2&modificationDate=1568210028434&api=v2)

Para a configuração do server.ini, basta seguir as informações da faq acima (Configuração completa do portal do vendedor).

**Obs**: A partir da release 12.1.33 do Protheus, a ser liberada em Outubro de 2021, o comportamento padrão de autenticação de WebServices SOAP e REST será alterado. A partir desta versão, caso a chave Security não seja informada no arquivo appserver.ini, os serviços serão iniciados exigindo autenticação de usuário. Caso seja necessário trabalhar sem autenticação, a chave deverá ser configurada com o valor 0 (Exemplo: Security=0).

Para mais detalhes do portal do cliente, acesse a FAQ: **[PPCL0001\_Configuração\_do\_Portal\_do\_Cliente](https://tdn.totvs.com/pages/viewpage.action?pageId=514744381)**
