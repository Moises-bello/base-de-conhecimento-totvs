---
article_id: 33207753029911
category: NFe - Nota Fiscal Eletrônica
content_hash: 44a7b60fba1b39a1691b9d3e8e188675ad174364ebd0a9b34403a64deb9283f4
fetched_at: '2026-06-28T22:40:06.909248+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Rejeição 452
  - Solicitada resposta assíncrona para Lote com somente 1 (uma) NF-e.
type: support-article
updated_at: '2025-10-14T17:15:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33207753029911-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Rejei%C3%A7%C3%A3o-452-Solicitada-resposta-ass%C3%ADncrona-para-Lote-com-somente-1-uma-NF-e
---

**Ocorrência**  
Ao realizar a transmissão de uma NF-e em ambiente de homologação ocorre a rejeição 452, como proceder?  
  
**Ambiente**  
Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Causa**  
Essa rejeição começou a ser apresentada **após uma nova regra da Sefaz entrar em vigor dia 02/06/2025 em ambiente de homologação e 13/10/2025 em ambiente de produção**, exigindo que transmissões de notas individuais sejam geradas através do método síncrono.  
  
**Solução**  
**1.** Realizar a aplicação do pacote abaixo no **RPO do TSS,** conforme release do ambiente:

**TSS 12.1.2210 - 3.0 (somente para clientes com garantia estendida):**[Clique aqui para download.](https://r.totvs.io/p/1215829)  
**TSS 12.1.2310 - 3.0: (somente para clientes com garantia estendida):**[Clique aqui para download.](https://r.totvs.io/p/1215830)  
**TSS 12.1.2410 - 3.0:**[Clique aqui para download.](https://r.totvs.io/p/1215827)  
  
A partir de 30/06/2025 apenas clientes com garantia estendida conseguem aplicar patchs ou utilizar RPO atualizado na versão 12.1.2310, maiores informações no link abaixo:  
- [Garantia Estendida TOTVS Backoffice Linha 12.1.2310](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32097480016791-Garantia-Estendida-TOTVS-Backoffice-Linha-Protheus-12-1-2310)

**IMPORTANTE - AMBIENTES CLOUD**  
- Para ambientes de TSS **Cloud Compartilhado** TOTVS, os mesmos já estão devidamente atualizados e contemplando essa atualização.  
- Para ambientes de TSS **Cloud Dedicado/Exclusivo** TOTVS, deverá ser solicitado essa atualização para a equipe do Cloud.  
  
Lembrando que a nível de transmissão, não há nenhum procedimento adicional a ser realizado, o próprio TSS internamente valida se a transmissão é de uma ou múltiplas notas e realiza a montagem de forma esperada pela Sefaz (assíncrona ou síncrona).  
  
Documentação  
- <https://tdn.totvs.com/pages/releaseview.action?pageId=960027496>
