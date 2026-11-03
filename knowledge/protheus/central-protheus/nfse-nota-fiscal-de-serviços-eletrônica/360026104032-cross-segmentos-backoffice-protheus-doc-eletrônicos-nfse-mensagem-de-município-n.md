---
article_id: 360026104032
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 27a64149de0d4d7f305b0ba8538148b22921cefffe41c260c0e5471334ab0b22
fetched_at: '2026-06-28T22:39:57.540734+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Mensagem
  de Município não homologado
type: support-article
updated_at: '2025-08-12T12:20:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026104032-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Mensagem-de-Munic%C3%ADpio-n%C3%A3o-homologado
---

**Dúvida**O que fazer quando aparecer a mensagem "Município não homologado" na rotina FISA022?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**Quando ocorrer a mensagem de "Município não homologado" é necessário realizar os seguintes procedimentos/validações:  
  
**1.** Verificar se o município de fato está homologado e disponível em nossa lista de Municípios Homologados: [Municipios Homologados](http://tdn.totvs.com/pages/releaseview.action?pageId=4814340)  
  
**2.** Ter o ambiente do TSS devidamente atualizado: [RPO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS) e [NEWNFSE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16784834285847-Cross-Segmentos-Backoffice-Protheus-TSS-NFSe-Configura%C3%A7%C3%A3o-do-NewNfse).  
  
**3.** Reiniciar todos os serviços: Protheus, TSS e DBACCESS **(em especial o do Protheus)**.   
Lembrando que caso haja balanceamento, todos os appserver's devem ser reiniciados.  
  
Dessa forma nenhum dado ficará preso em memória e a mensagem de "Município não homologado" não ocorrerá.
