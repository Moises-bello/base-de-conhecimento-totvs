---
article_id: 360056166474
category: ADVPL - Classe e Função
content_hash: d1592513d5ba036bbb598ddbbb2ca79fda6f60192818c203f09c6c00d1e16ea8
fetched_at: '2026-06-28T22:40:14.162857+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Extenso() - Conversão
  em outras línguas
type: support-article
updated_at: '2021-05-06T20:30:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056166474-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Extenso-Convers%C3%A3o-em-outras-l%C3%ADnguas
---

**Dúvida**Qual a funcionalidade do método Extenso() em relação a outras línguas.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões  
  
**Solução**A função Extenso() tem como objetivo retornar um texto por extenso de um valor numérico.

Sintaxe:

Extenso(nValor,lQuantid,nMoeda,cPrefixo,cIdioma,lCent,lFrac)

Para buscar no detalhe todos os parâmetros passados para a função, abra o link: <https://tdn.totvs.com/pages/viewpage.action?pageId=312163721>

Exemplo:

Tenho o valor 1000, e apliquei a função extenso da maneira abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095313514/mceclip1.png)

A variável cExtenco conterá o valor igual a "Mil Reais"

No exemplo acima foi utilizado a moeda real e busquei o extenso em português, porém essa função também dá a opção de utilizar outras duas línguas, sendo espanhol e inglês. Para definir qual a língua a ser apresentada por extenso, deverá passar através da variável cIdioma a opção deseja, sendo 1=Português ,2=Espanhol ,3=Inglês.

Ao utilizar essa funcionalidade de idioma, o sistema buscará a descrição da moeda através dos parâmetro MV\_MOEDAx e MV\_MOEDAPx, onde x é o número da moeda desejada e passada para a função Extenso através da variável nMoeda.

Para buscar a descrição da moeda a função Extenso utiliza o GetMV, que trás o conteúdo contido no dicionário referente ao idioma contido no ambiente. Exemplo: Se o meu ambiente é português, irá buscar a descrição da moeda no campo X6\_CONTEUD dos parâmetros MV\_MOEDAx e MV\_MOEDAPx.

**Saiba mais**

GetMV: <https://tdn.totvs.com/pages/viewpage.action?pageId=24346929>

Extenso: <https://tdn.totvs.com/pages/releaseview.action?pageId=6070758>

Sobre o uso da função no plural: [Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Função Extenso texto no plural](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050813633)
