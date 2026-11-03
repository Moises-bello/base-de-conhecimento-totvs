---
article_id: 360050192953
category: Gestão de Transportes (TMS)
content_hash: 502962b6b2ca0295b5ff6bfc58cdb3c0982617756553d295aa0a43ddc1abca93
fetched_at: '2026-06-28T22:45:29.338399+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Informações importantes para situações referente
  a Transmissão de Documentos utilizando o TOTVS Colaboração 2.0
type: support-article
updated_at: '2022-06-20T14:12:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050192953-Log%C3%ADstica-Linha-Protheus-TMS-Informa%C3%A7%C3%B5es-importantes-para-situa%C3%A7%C3%B5es-referente-a-Transmiss%C3%A3o-de-Documentos-utilizando-o-TOTVS-Colabora%C3%A7%C3%A3o-2-0
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:24 min**  
**Dúvida**Informações importantes para situações referente a Transmissão de Documentos utilizando o **TOTVS Colaboração 2.0**  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Abaixo descrevemos informações importantes para situações referente a Transmissão de Documentos:

* Ao transmitir o documento e não obter retorno, verificar o **CNPJ** do arquivo **MercadorConf** com o **CNPJ** enviado no arquivo **XML**.
* Nomenclatura do arquivo
* Verificar se o **Schedule** está configurado corretamente e está movendo o arquivo da pasta **IN** para a pasta **LIDOS.**
* Identificado que o arquivo foi enviado através da pasta **SENT** e não obteve o retorno, um ticket precisará ser aberto e transferido para **NeoGrid**.

**Nomenclatura dos arquivos XML - CT-e**Normalmente os 3 primeiros dígitos do arquivo **XML** identificam o **tipo de documento ou processo** realizado, exemplos:

* **199** - Transmissão de documentos tipo **CT-e, CT-e** Complementar
* **200** - Transmissão de cancelamento documento tipo **CT-e**
* **201** - Transmissão de inutilização documento tipo **CT-e**
* **385** - Transmissão evento carta de correção para documento tipo **CT-e**

**Nomenclatura dos arquivos XML - MDF-e**

* **360** - Transmissão de envio documentos tipo **MDF-e**
* **361** - Transmissão de encerramento documentos tipo **MDF-e**
* **362** - Transmissão de cancelamento documento tipo **MDF-e**

**Glossário  
CT-e** - Conhecimento de transporte eletrônico **MDF-e** - Manifesto Eletrônico de Documentos Fiscais**XML** - Extensible Markup Language
