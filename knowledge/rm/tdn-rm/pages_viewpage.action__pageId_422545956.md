---
content_hash: 991bd83f4d6964dcdcfa5a2069334e1467aa2165e9b16b07a9a918a92706600a
fetched_at: '2026-06-29T00:09:22.059824+00:00'
page_id: '422545956'
product: rm
source: tdn-rm
title: Geração dos Campos Livres NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545956
version: 22
---

#f5f5f5#363636noneGERAÇÃO DOS CAMPOS LIVRES NF-e

## **Conteúdo**



## **01. Visão GeralVisaoGeral**

No xml da Nota Fiscal Eletrônica existem alguns campos de uso livre para que o contribuinte possa destacar informações de seu interesse ou de interesse do Fisco. Estes campos são dinâmicos e o contribuinte pode definir qual será o nome e conteúdo do campo.

Neste documento está sendo apresentando qual o procedimento para geração destes campos e como é o comportamento na montagem do xml da NF-e

## **02. Cadastro do Campos LivresCadastro**

O primeiro passo é realizar o cadastro dos Campos Livres.

Mais informações em [Campos Livres NF-E](https://tdn.totvs.com/pages/viewpage.action?pageId=687150856)

## **03. MovimentoMovimento**

Os campos Cadastrados devem ser incluídos no Movimento da NF-e

Mais informações em [Campos de Uso Livre (Nota Fiscal Eletrônica)](https://tdn.totvs.com/pages/viewpage.action?pageId=687748443)

## **04. Emissão da NF-eNFe**

Ao executar o processo de Envio da NF-e, os campos livres serão gerados conforme abaixo:

Por Item

Serão gerados no xml da nota os campo que estejam no item do Movimento e que tenha algum valor preenchido.

* A informação será gerada no grupo obsCont ou obsFisco, conforme definido no cadastro do campo.
* O valor do campo xCampo também irá considerar o Cadastro do campo

Exemplo:

xmlEclipsetrue

Nota de Recolhimento de ICMS Fev/2021

02/2021
]]>

Se no Item estiver mais de um campo preenchido para o mesmo grupo, será apresentada uma mensagem de erro indicando que apenas um campo pode ser preenchido por item

Por Nota

Serão gerados no xml da nota os campo que estejam no Movimento e que tenha algum valor preenchido.

* A informação será gerada no grupo obsCont ou obsFisco, conforme definido no cadastro do campo.
* O valor do campo xCampo também irá considerar o Cadastro do campo

Exemplo:

xmlEclipsetrue

Nota de Recolhimento de ICMS Fev/2021

01/2020

02/2021
]]>

Deve ser observado, no manual da NF-e, a quantidade de campos permitidos na mesma nota

## **05. SPED****SPED**

Na geração do SPED,  também é possível  gerar os registros 0450 e 0460 através das [Informações Fiscais Adicionais](https://tdn.totvs.com/pages/viewpage.action?pageId=696092112) cadastradas nos Campos de Uso Livre que estão vinculadas no Lançamento.

Mais informações em [SPED FISCAL - Bloco 0](https://tdn.totvs.com/pages/viewpage.action?pageId=422546008#BLOCO0-0450)

## **06. Outras InformaçõesOutrasInformacoes**

Este comportamento está disponível a partir dos patches:

* 12.1.33.264
* 12.1.34.163
* 12.1.2205.106
