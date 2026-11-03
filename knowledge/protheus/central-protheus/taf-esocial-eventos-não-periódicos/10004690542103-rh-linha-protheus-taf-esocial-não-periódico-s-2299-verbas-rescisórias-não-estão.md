---
article_id: 10004690542103
category: TAF - eSocial - Eventos Não Periódicos
content_hash: ff1ec0344e200cc819e87243b837bc4243af808a2d8b19754bd913a8664d0fe8
fetched_at: '2026-06-28T22:45:17.959998+00:00'
product: protheus
section_id: 1500001548002
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial  - Não Periódico - S-2299 - Verbas rescisórias
  não estão sendo enviadas para o eSocial
type: support-article
updated_at: '2024-05-27T14:45:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10004690542103-RH-Linha-Protheus-TAF-eSocial-N%C3%A3o-Peri%C3%B3dico-S-2299-Verbas-rescis%C3%B3rias-n%C3%A3o-est%C3%A3o-sendo-enviadas-para-o-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23703216797847) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Porque as verbas rescisórias não estão sendo enviadas para o eSocial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial  - Não Periódicos - S-2299 - Desligamento (TAFA266) – Todas as versões

**Problema**O XML de integração (do GPE/RM Labore/Datasul), referente ao evento S-2299, desligamento, contém as verbas rescisórias, porém, o XML gerado pelo TAF, não carrega as informações das verbas, sendo o evento S-2299 transmitido ao governo sem as informações de pagamento.

*Exemplo de XML integrado (com todas as Verbas) x XML do TAF (sem informação das verbas)*

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10004434653335)

Esse problema pode ser identificado no momento da transmissão do S-2299, ou somente identificado ao tentar transmitir o evento S-1210, pois, as informações de recibos de pagamentos, não serão encontrados no evento S-2299 (transmitido). O evento S-1210, retorna inconsistente do governo, com as ocorrências 861 e 726.

*Exemplo de inconsistência retornada no S-1210, se o S-2299 for transmitido sem as verbas rescisórias:*

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10004330393623)

**Solução**

Para correção, é necessário:

**1.** **Atualizar o ambiente**, com o último **Pacote Acumulado**, disponível nos links abaixo:

[RH - Linha Protheus - TAF - ATUALIZAÇÃO - Como atualizar o TAF E-social (Expedição Contínua)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239)

**2.** Se o evento S-2299 **já foi transmitido** ao governo, **sem as verbas** **rescisórias** necessárias, **retifique** o evento, e transmita novamente ao governo, para que o mesmo fique correto e não apresente inconsistências na transmissão do evento S-1210.
