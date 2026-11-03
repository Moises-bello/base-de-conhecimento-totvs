---
article_id: 24416742138903
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 2fcdff99f93c69b80dd9c94c8f5071413ae6b87f1f446e9b1ea0c7a6f6487c6f
fetched_at: '2026-06-28T22:39:57.603345+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - O municipio
  xxxxxxx não está na tabela TSS0013
type: support-article
updated_at: '2025-05-23T13:09:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24416742138903-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-O-municipio-xxxxxxx-n%C3%A3o-est%C3%A1-na-tabela-TSS0013
---

**Dúvida**Como corrigir o erro abaixo apresentado na tentativa de transmissão da nota?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24416742100247)  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões  
  
**Solução**Para solução desse erro é importante revisar 4 pontos:  
  
1- O **RPO do TSS** está atualizado?  
2 - O Parâmetro **MV\_NEWNFSE** dessa entidade na **SPED000** está como **S**?  
3 - O municipio existe na tabela **TSS0013**?  
4 - A **versão** informada no **Wizard.cfg** da rotina FISA022 está correta?  
  
Veja no link abaixo a versão correta para o município.  
**Exemplos**: Santos e Joinville.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27914525850007)  
  
[- Relação de Municipios Homologados (clique aqui).](https://tdn.totvs.com/pages/releaseview.action?pageId=4814340)  
  
**Por padrão, ao refazer o Wizard.cfg (item 4) com a versão correta, o problema é sanado.**
