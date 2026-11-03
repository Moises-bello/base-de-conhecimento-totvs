---
article_id: 360027577352
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: dfa0d80f879dfe3bc243ae45051710834fb5bf4e712c40ff9b7ac6eecbee0d98
fetched_at: '2026-06-28T22:39:57.610683+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Opção não
  disponível no Protheus Função : U_NFSEXMLECalled by NFSEXML'
type: support-article
updated_at: '2021-10-19T18:21:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027577352-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Op%C3%A7%C3%A3o-n%C3%A3o-dispon%C3%ADvel-no-Protheus-Fun%C3%A7%C3%A3o-U-NFSEXMLECalled-by-NFSEXML
---

**Ocorrência**Ao realizar a transmissão de uma NFSE pela rotina **FISA022** é apresentado o erro: **Opção não disponível no Protheus Função : U\_NFSEXMLECalled by NFSEXML.**

![erro.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360027611991/erro.png)

**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**Essa mensagem ocorre pelo fato do fonte **NFSEXMLENV** não estar compilado no RPO do Protheus.  
  
**Solução**Deverá compilar o RDMAKE NFSEXMLENV disponível no link abaixo, contemplando todas as versões:  
  
[RDMAKE NFSEXMLENV (12.1.25 - 12.1.27)](https://suporte.totvs.com/portal/p/10098/download#detail/1031443)  
  
*Obs.: Também verificar se o parâmetro **MV\_NFSEMOD** está igual à **.T.***
