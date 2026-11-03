---
article_id: 360058758573
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 8088e41f6053703b2480919a425644c0fc1736dd318b045b55447a8cb271a2ed
fetched_at: '2026-06-28T22:39:57.618560+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Patos de
  Minas-MG: Chave de Acesso'
type: support-article
updated_at: '2025-06-25T21:11:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058758573-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Patos-de-Minas-MG-Chave-de-Acesso
---

**Dúvida**Onde informar a Chave de Acesso que permite a comunicação webservice com a prefeitura de Patos De Minas-MG?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**A chave de acesso deve ser extraída no portal da prefeitura e preenchida no campo **Chave de Autenticação**, na ultima tela do wizard.config da rotina FISA022:

**![](https://totvssuporte.zendesk.com/attachments/token/82woz0RHWIWFEzkmgjqxjm218/?name=inline-1621070352.png)**  
Essa chave será gravada na tag **<tsVrsArq></tsVrsArq>,** no XML do RPS.
