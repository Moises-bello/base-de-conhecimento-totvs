---
article_id: 360045702113
category: NFe - Nota Fiscal Eletrônica
content_hash: 501b965b9f8ea702fd0ff7ac5e1ce5a1234e98e41431fe29d734f357a2b833d1
fetched_at: '2026-06-28T22:40:03.872695+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 319 Rejeição :
  Contranota de Produtor referenciada somente NF de entrada'
type: support-article
updated_at: '2025-06-11T12:33:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045702113-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-319-Rejei%C3%A7%C3%A3o-Contranota-de-Produtor-referenciada-somente-NF-de-entrada
---

**Dúvida**Como solucionar a Rejeição 319 Contranota de Produtor referenciada somente NF de entrada ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1- Caso isso esteja ocorrendo deve-se verificar os seguintes pontos:

Quando for NFPe **(Nota com uma chave eletrônica)**

* A nota de produtor rural eletrônica (NFP-e) deve ser criada com o formulário próprio = Não, Espécie = SPED e o campo F1\_CHVNFE tem que estar preenchido com a chave da nota. (Esta nota não é transmitida)  
  (Quando a nota do produtor rural for NFP-e, não utilizar o modelo NFP e sim SPED no campo espécie por se tratar de uma nota modelo 55 - nota fiscal eletrônica).
* A contra-nota deve estar com o formulário próprio = Sim e espécie = SPED (Esta é transmitida e deve ser referenciada à nota NFP-e do produtor rural que foi incluída anterior e que não foi transmitida, através dos campos D1\_ITEMORI, D1\_SERIORI, D1\_NFORI e F1\_CHVNFE.)
* Quando é feito uma nota complementar ou de devolução deve ter formulário próprio = Sim, Espécie = SPED e essa nota deve ser referenciada a nota que foi transmitida e não a primeira com formulário próprio = Não.

2 - Quando for NFP **(Nota sem uma chave eletrônica)**

* Nota de Entrada com formulário próprio = Não Espécie = NFP (Esta não é transmitida).
* A contra-nota deve estar com o formulário próprio = Sim Espécie = SPED (Esta é transmitida e deve ser referenciada à nota anterior que não foi transmitida, através dos campos D1\_ITEMORI, D1\_SERIORI, D1\_NFORI)
* Quando a nota for complementar deve ter formulário próprio = Sim, Espécie = SPED e essa nota deve ser referenciada a nota que foi transmitida e não a primeira com formulário próprio = Não  
    
    
  **IMPORTANTE**  
  Quando a nota for de complemento (F1\_TIPO = "C") e o estado for Rio Grande do Sul (MV\_ESTADO = "RS"), e a operação ocorrer dentro do Estado, no XML irá conter as duas referências (Exigência da Sefaz Rio grande do Sul)  
    
  **Chave da nota que recebera o complemento :**  
  <NFRef>  
  <refNFe></refNFe>   
  </NFRef>  
    
  **Dados da nota de produtor rural:**  
    
  <NFRef>  
  <refNFP>  
  <cUF></cUF>  
  <AAMM></AAMM>  
  <CNPJ></CNPJ>  
  <IE></IE>  
  <mod></mod>  
  <serie></serie>  
  <nNf></nNf>  
  </refNFP>  
  </NFRef>
