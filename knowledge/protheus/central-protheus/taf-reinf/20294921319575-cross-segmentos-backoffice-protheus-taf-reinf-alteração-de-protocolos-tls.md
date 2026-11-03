---
article_id: 20294921319575
category: TAF - REINF
content_hash: 9bb2a06e80d1bbc67f8d3f619933a48fc438c9f5a2b45abc43261f315c060e38
fetched_at: '2026-06-28T22:41:33.596382+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Alteração de Protocolos
  TLS
type: support-article
updated_at: '2024-01-11T19:47:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20294921319575-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Altera%C3%A7%C3%A3o-de-Protocolos-TLS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20294921299223) Tempo aproximado para leitura: **00:02:00min** **Dúvida**Alteração de **protocolos TLS** para transmissão da **Reinf**.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Automação Fiscal  - Todas as versões  
  
**Solução**

Informamos que a revisão do conjunto de versões de protocolos **TLS** na **EFD-Reinf** foi programada para os **dias 20 e 21 de janeiro de 2024**. Ressaltamos que a partir dessa data a **EFD-REINF** deixará de permitir conexões utilizando os **protocolos TLS 1.0 e TLS 1.1.**  
O **Manual de Orientação** ao Desenvolvedor da **EFD-Reinf** foi atualizado para a **versão 2.4** com informações sobre os protocolos **TLS** e as cifras criptográficas.

O TSS Já possui a configuração do TLS 1.2, segue configuração padrão:

**[SSLConfigure]**  
**SSL2 = 0**  
**SSL3 = 1**  
**TLS1\_0 = 1**  
**TLS1\_1 = 1**  
**TLS1\_2 = 1**  
**Verbose = 1**  
 

Para mais informações:   
<http://sped.rfb.gov.br/pagina/show/7313>
