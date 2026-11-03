---
content_hash: 628f16466ab668c19b94f93c37b0845cea2970e53c0fdf7d85b5efd2e319150c
fetched_at: '2026-06-29T00:05:51.843975+00:00'
page_id: '1056138258'
product: rm
source: tdn-rm
title: Ajuste e Evoluções Abril/2026 (NFS-e)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056138258
version: 15
---

# Conteúdo

1Conteúdononenone

# 1. Sobre

Esta atualização traz alterações no xml do layout único para validação no TSS.

# 2. Versões para atualização

Biblioteca RM:

* 12.1.2506.286
* 12.1.2510.206
* 12.1.2602.127

TSS:

* [Orientações para Instalação e Atualização do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18590720143639-Cross-Segmentos-TOTVS-Backoffice-Linha-RM-Doc-Eletr%C3%B4nicos-Instala%C3%A7%C3%A3o-e-atualiza%C3%A7%C3%A3o-do-TSS-12-1-2410)
* [Pacotes de Atualização - TSS (NFE | NFSE | NFTS | MDE | MDFE)](https://tdn.totvs.com/pages/viewpage.action?pageId=525011807)

# 3. Principais Alterações

## Geração do grupo totTrib

Adicionado o grupo totTrib no layout do TSS. O grupo consiste nos totalizadores dos valores e percentuais dos tributos federais, estaduais e municipais.

Detalhes:

## Nota Técnica Nº 007/2026

O grupo piscofins passa a permitir a geração da tag **tpRetPisCofins** de acordo com a regra anterior à NT 007.

Para isso é necessário um cadastro de um parâmetro que indica que o município emitente não é aderente a essa nota técnica.

Detalhes:

## Atualização do grupo identificacao

Atualizado o grupo identificacao no layout do TSS. O grupo contem dados de identificação do Documento e da transação

Detalhes: [Grupo contendo dados de identificação do Documento e da transação](https://tdn.totvs.com/pages/viewpage.action?pageId=560653244)

## Atualização do grupo prestador

Atualizado o grupo prestador no layout do TSS. O grupo contem dados do prestador de serviços

Detalhes: [Dados do prestador de serviços](https://tdn.totvs.com/pages/viewpage.action?pageId=560653354)

## Atualização do grupo tomador

Atualizado o grupo tomador no layout do TSS. O grupo contem dados do tomador de serviços

Detalhes: [Dados detalhados do tomador do serviço](https://tdn.totvs.com/pages/viewpage.action?pageId=560653794)

## Atualização do grupo comExt

Atualizado o grupo comExt no layout do TSS. O grupo contem informações relativas à exportação/importação de serviço prestado.

Detalhes: [Grupo de informações relativas à exportação/importação de serviço prestado](https://tdn.totvs.com/pages/viewpage.action?pageId=1056144273)

## Atualização do grupo atvEvento

Atualizado o grupo atvEvento no layout do TSS. O grupo contem informações relativas à evento.

Detalhes: [Grupo de informações do DPS relativas à Evento](https://tdn.totvs.com/pages/viewpage.action?pageId=1056144301)

## Atualização do CNAE

Atualizado o preenchimento das tags que recebem o CNAE, passando a priorizar o código CNAE informado no anexo do tributo por município.    
Layout TPF: 

Grupo Identificação: Tag: CNAE - Detalhes:

Grupo Serviço: Tag: CNAE - Detalhes:

Layout TSS:

Grupo Atividade: Tag: Codigo - Detalhes:

Grupo Servicos: Tag: CNAE - Detalhes:

## Atualização do grupo Valores

Atualizado as tags: outdesp, basiss, bascsll, baspis, bascfis, basir, basinss, tribISSQN, tpImunidade, totret, valorliqfinal, tpRetISSQN.

Detalhes:

## Atualização das informações dos tributos PIS/COFINS Apurado

Atualizado as informações relacionadas aos tributos PIS/COFINS Apurado

Detalhes: [Totais das informações dos tributos PIS/COFINS Apurado](https://tdn.totvs.com/pages/viewpage.action?pageId=1056144736)
