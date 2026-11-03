---
article_id: 40503073523479
category: NFSE - Nota Fiscal de Serviço Nacional
content_hash: f994216a983011cf201f599eff8678f332c9dcb5eeead87c309dd0c71843e830
fetched_at: '2026-06-28T22:39:54.410474+00:00'
product: protheus
section_id: 33955617231639
source: central-protheus
title: 'Cross Segmentos - TSS Transmissão de Documentos Eletrônicos - NFSE Nacional:
  Falha de Schema Element ''{http://www.sped.fazenda.gov.br/nfse}xDescServ'': This
  element is not expected. Expected is ( {http://www.sped.fazenda.gov.br/nfse}cTribNac
  ).'
type: support-article
updated_at: '2026-05-15T17:38:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40503073523479-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-NFSE-Nacional-Falha-de-Schema-Element-http-www-sped-fazenda-gov-br-nfse-xDescServ-This-element-is-not-expected-Expected-is-http-www-sped-fazenda-gov-br-nfse-cTribNac
---

**Ocorrência**  
Ao realizar a transmissão de uma nota ocorre a falha de schema abaixo:  
  
**Element '{http://www.sped.fazenda.gov.br/nfse}xDescServ': This element is not expected. Expected is ( {http://www.sped.fazenda.gov.br/nfse}cTribNac ).**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Causa**  
Essa rejeição ocorre pela falta do Código de Tributação Municipal na **tag <cTribNac>, que é obrigatória.**  
  
**Solução**  
Atualmente existem as tags de Tributação Nacional e Tributação Municipal.  
  
No Protheus esses conteúdos devem ser informados no campo**B1\_TRIBMUN, BZ\_TRIMUN ou FT\_TRIBMUN,**o campo usado irá depender da configuração do ambiente.  
[**Possibilidades TRIBMUN aqui!**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061751034-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Possibilidades-de-montagem-de-C%C3%B3digo-de-Servi%C3%A7o-C%C3%B3digo-de-Tributa%C3%A7%C3%A3o-e-CNAE-NFSEXMLENV)  
  
Ao informar o código 110201001 no campo \_TRIBMUN, os 6 primeiros dígitos serão gerados na TAG **cTribNac** e os 3 seguintes na TAG **cTribMun**, exemplo:

<cTribNac>110201</cTribNac>  
<cTribMun>001</cTribMun>  
  
OBS: A tag **cTribMun é opcional do MUNICIPIO,**ou seja, caso o município nao obrigue o envio basta nao preencher os 9 digitos, ficando somente os 6 dígitos do cTribNac.

* **Como descubro o código de que devo enviar?**
  + **Acesse o**[**portal da Nacional**](https://www.producaorestrita.nfse.gov.br/EmissorNacional/Login?ReturnUrl=%2fEmissorNacional%2fDashboard)**e simule uma emissão de nota, na segunda tela de serviços você verá os códigos nacionais e municipais .****![](https://tdn.totvs.com/download/attachments/801316412/image-2025-9-24_17-56-50.png?version=1&modificationDate=1758747411637&api=v2)**
