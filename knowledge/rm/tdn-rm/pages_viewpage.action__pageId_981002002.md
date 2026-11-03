---
content_hash: dd3269f071e2d5abed305f8e73ec49578953f271cc2f472bf25a4c651d46083f
fetched_at: '2026-06-29T00:12:15.586552+00:00'
page_id: '981002002'
product: rm
source: tdn-rm
title: Identificação do Emitente do CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=981002002
version: 5
---

# emit - Identificação do Emitente do CT-e

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **emit** | **[infCte](https://tdn.totvs.com/pages/viewpage.action?pageId=981000770)** | **1-1** | **Grupo** | **Identificação do Emitente do CT-e** |
| CNPJ | emit | 1-1 | Elemento de Escolha | GFILIAL.CGC |
| CPF | emit | 1-1 | GFILIAL.CGC |
| IE | emit | 0-1 | Elemento | GFILIAL.INSCRICAOESTADUAL |
| IEST | emit | 0-1 | Elemento | Não será gerado |
| xNome | emit | 1-1 | Elemento | GFILIAL.NOME |
| xFant | emit | 0-1 | Elemento | GFILIAL.NOMEFANTASIA |
| **enderEmit** | **emit** | 1-1 | **Grupo** | **Endereço do emitente** |
| xLgr | enderEmit | 1-1 | Elemento | GFILIAL.RUA |
| nro | enderEmit | 1-1 | Elemento | GFILIAL.NUMERO |
| xCpl | enderEmit | 0-1 | Elemento | GFILIAL.COMPLEMENTO |
| xBairro | enderEmit | 1-1 | Elemento | GFILIAL.BAIRRO |
| cMun | enderEmit | 1-1 | Elemento | Classificação do município conforme definido no cadastro da Filial relacionado ao Movimento do CT-e |
| xMun | enderEmit | 1-1 | Elemento | Definido no cadastro da Filial relacionado ao Movimento do CT-e |
| CEP | enderEmit | 0-1 | Elemento | GFILIAL.CEP |
| UF | enderEmit | 1-1 | Elemento | GFILIAL.ESTADO |
| fone | enderEmit | 0-1 | Elemento | GFILIAL.TELEFONE |
| CRT | emit | 1-1 | Elemento | **SE** (DFILIAL.CLASSIFTRIBUTARIA == MEI)        CRT = 4;        **SE** ((DFILIAL.OPTANTESIMPLES) && (DFILIAL.SUBLIMITEEXCEDIDO))        CRT = 2;        **SE** (DFILIAL.OPTANTESIMPLES)         CRT = 1;        **SENAO** CRT = 3; |
