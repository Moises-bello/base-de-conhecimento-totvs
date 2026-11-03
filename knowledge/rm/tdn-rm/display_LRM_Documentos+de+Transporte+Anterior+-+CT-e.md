---
content_hash: 804c357b8d0a49cb724a697c90b6cdc666846b5063100852b664c6dd2c31be9b
fetched_at: '2026-06-29T00:12:15.784851+00:00'
page_id: '981793223'
product: rm
source: tdn-rm
title: Documentos de Transporte Anterior - CT-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Documentos+de+Transporte+Anterior+-+CT-e
version: 2
---

# docAnt - Documentos de Transporte Anterior

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **docAnt** | **[infCTeNorm](https://tdn.totvs.com/pages/viewpage.action?pageId=981002639)** | **0-1** | **Grupo** | **Documentos de Transporte Anterior** |
| emiDocAnt | docAnt | 1-n | **Grupo** | **Emissor do documento anterior** |
| CNPJ | emiDocAnt | 1-1 | Elemento de Escolha | TCTEEMISSOR.CNPJCPF |
| CPF | emiDocAnt | 1-1 | TCTEEMISSOR.CNPJCPF |
| **--- x — Sequência opcional do XML: Sempre será gerado** | | | | |
| IE | emiDocAnt | 1-1 | Elemento da Sequência | TCTEEMISSOR.INSCRESTADUAL |
| UF | emiDocAnt | 1-1 | Elemento da Sequência | TCTEEMISSOR.CODETD |
| **Fim da sequência opcional do XML — x ---** | | | | |
| xNome | emiDocAnt | 1-1 | Elemento | TCTEEMISSOR.NOME |
| **idDocAnt** | **emiDocAnt** | **1-2** | **Grupo** | **Informações de identificação dos documentos de Transporte Anterior** |
| **idDocAntPap** | **idDocAnt** | **1-n** | **Grupo de Escolha** | **Documentos de transporte anterior em papel** |
| tpDoc | idDocAntPap | 1-1 | Elemento | TCTEDOC.TIPODOCORIGINARIO |
| serie | idDocAntPap | 1-1 | Elemento | TCTEDOC.SERIE |
| subser | idDocAntPap | 0-1 | Elemento | TCTEDOC.SUBSERIE |
| nDoc | idDocAntPap | 1-1 | Elemento | TCTEDOC.NUMERODOCFISCAL |
| dEmi | idDocAntPap | 1-1 | Elemento | TCTEDOC.DATAEMISSAO |
| **idDocAntEle** | **idDocAnt** | **1-n** | **Grupo de Escolha** | **Documentos de transporte anterior eletrônicos** |
| chCTe | idDocAntEle | 1-1 | Elemento | TCTEDOC.CHAVEACESSONFE |
