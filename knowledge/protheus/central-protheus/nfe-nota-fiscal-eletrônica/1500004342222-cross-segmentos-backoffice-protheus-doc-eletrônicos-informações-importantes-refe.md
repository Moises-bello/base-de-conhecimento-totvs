---
article_id: 1500004342222
category: NFe - Nota Fiscal Eletrônica
content_hash: 56349cdcdb7553cb5b3d10460fa9c66c0bd91d663fb554d515220a5371d00833
fetched_at: '2026-06-28T22:40:01.864715+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Informações importantes
  referente ao processamento de documentos utilizando o TOTVS Colaboração 2.0'
type: support-article
updated_at: '2021-10-11T16:57:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004342222--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Informa%C3%A7%C3%B5es-importantes-referente-ao-processamento-de-documentos-utilizando-o-TOTVS-Colabora%C3%A7%C3%A3o-2-0
---

**Dúvida** Informações importantes referente ao processamento de documentos utilizando o TOTVS Colaboração 2.0.  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Abaixo descrevemos informações importantes referentes ao processamento de documentos por meio do TOTVS Colaboração 2.0:

* Ao transmitir o documento e não obter retorno, verificar o **CNPJ** do arquivo **MercadorConf** com o **CNPJ** enviado no arquivo **XML**.
* Nomenclatura do arquivo.
* Verificar se o **Schedule** está configurado corretamente e se está movendo o arquivo da pasta **IN** para a pasta **LIDOS.**
* Identificado que o arquivo foi enviado através da pasta **SENT** e não obteve o retorno, um ticket precisará ser aberto e transferido para **NeoGrid** avaliar.

Geralmente os 3 primeiros dígitos do arquivo XML identificam o tipo de documento ou processo realizado, conforme exemplos:

**Nomenclatura dos arquivos XML - NFe**

* **170** - Transmissão de NFe;
* **171** - Transmissão de cancelamento de NFe;
* **172** - Transmissão de inutilização de NFe;
* **301** - Transmissão de carta de correção de NFe.

**Nomenclatura dos arquivos XML - NFSe**

* **203** - Transmissão de NFSe;
* **204** - Transmissão de cancelamento de NFSe.

**Nomenclatura dos arquivos XML - CTe**

* **199** - Transmissão de CTe, CTe Complementar;
* **200** - Transmissão de cancelamento de CTe;
* **201** - Transmissão de inutilização de CTe;
* **385** - Transmissão evento carta de correção de CTe.

**Nomenclatura dos arquivos XML - MDFe**

* **360** - Transmissão de MDFe;
* **361** - Transmissão de encerramento de MDFe;
* **362** - Transmissão de cancelamento de MDFe.

**Glossário:****XML** - Extensible Markup Language         
**NFe** - Nota fiscal eletrônica  
**NFSe** - Nota fiscal de serviço eletrônica  
**CTe** - Conhecimento de transporte eletrônico  
**MDFe -** Manifesto Eletrônico de Documentos Fiscais
