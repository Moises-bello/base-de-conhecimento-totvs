---
article_id: 360028132651
category: Faturamento - Cadastros
content_hash: 47464d2b5f3bc9d45fba5b780456dce779771d6f91af972a57e5ac6cbcf4c539
fetched_at: '2026-06-28T22:38:35.572048+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - Como gerar comissão
  do Cadastro do Cliente?
type: support-article
updated_at: '2022-02-18T19:43:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028132651-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-gerar-comiss%C3%A3o-do-Cadastro-do-Cliente
---

**Dúvida**

Ao informar uma comissão no cadastro do cliente, sistema não está considerando a comissão conforme cadastro de cliente e sim conforme cadastro do vendedor informado no pedido de vendas. Como gerar comissão?  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT – A partir da versão 11.80.  
  
**Solução**

Para que seja considerado a comissão informada no cadastro de cliente **SA1** é necessário informar no cadastro de cliente um vendedor e sua comissão. Se o vendedor não for amarrado ao cliente juntamente com a porcentagem da sua comissão, o sistema não vai realizar o calculo de comissão baseado neste cadastro.

Campos que devem ser considerados para a comissão ser gerado conforme cadastro de cliente:  
**A1\_VEND** e **A1\_COMIS** os mesmos devem "caminhar juntos".

**Saiba Mais**

Lembrando que o sistema prioriza a sua forma de busca para gerar comissão ao vendedor.  
**[FAT0036\_Hierarquia\_priorização\_de\_busca\_de\_comissão\_para\_gerar\_comissão\_ao\_vendedor\_sobre\_Pedido\_de\_Vendas](http://tdn.totvs.com/pages/viewpage.action?pageId=232818579)**
