---
article_id: 360020132231
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 4a9337d0a5bf1f74e01fac81bcccf198e830d0d2a81285c2d14cc47cc218749b
fetched_at: '2026-06-28T22:38:31.215439+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-Help: A contabilização não pode ser executada'
type: support-article
updated_at: '2021-04-28T15:55:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020132231-MP-FAT-Help-A-contabiliza%C3%A7%C3%A3o-n%C3%A3o-pode-ser-executada
---

**Dúvida**

Ao gerar a contabilização off line, o sistema exibe a mensagem: Help a contabilização não pode ser executada.  
   
 **Ambiente**

Microsiga Protheus - a partir da versão 11.  
  
**Solução**

A mensagem de HELP : A contabilização não pode ser executada, se refere a tela abaixo:

![](http://tdn.totvs.com/download/attachments/438288185/image2018-11-22_16-6-59.png?version=1&modificationDate=1542911745860&api=v2)

Também poderá ter esse formato:

![](http://tdn.totvs.com/download/attachments/438288185/image2018-11-22_16-7-58.png?version=1&modificationDate=1542911745833&api=v2)

Essas mensagens ocorrem por que o ambiente está configurado para tratar a contabilização por **Mult Thread**, desta forma, existem premissas a serem respeitadas neste tipo de contabilização, caso contrário, o sistema exibirá estas mensagens.

Para que não ocorram, deixe os parâmetros **MV\_ALTLCTO** igual a N e **MV\_PRELAN** igual a D - Doc inconsistente.

**Saiba Mais: [FAT0283 Help: A contabilização não pode ser executada](http://tdn.totvs.com/pages/viewpage.action?pageId=438288185)**
