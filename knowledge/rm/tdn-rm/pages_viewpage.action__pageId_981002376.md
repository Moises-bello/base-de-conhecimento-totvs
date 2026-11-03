---
content_hash: 7357831520c9103e4fcfd432779933fb8c7de67ab6991144ba9f19fbcc420eaf
fetched_at: '2026-06-29T00:12:15.630437+00:00'
page_id: '981002376'
product: rm
source: tdn-rm
title: Informações do Destinatário do CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=981002376
version: 4
---

# dest - Informações do Destinatário do CT-e

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **dest** | **[infCte](https://tdn.totvs.com/pages/viewpage.action?pageId=981000770)** | **0-1** | **Grupo** | **Informações do Destinatário do CT-e** |
| CNPJ | dest | 1-1 | Elemento de Escolha | FCFO.CGCCFO ou GFILIAL.CGC |
| CPF | dest | 1-1 | FCFO.CGCCFO ou GFILIAL.CGC |
| IE | dest | 0-1 | Elemento | FCFO.INSCRESTADUAL ou GFILIAL.INSCRICAOESTADUAL |
| xNome | dest | 1-1 | Elemento | FCFO.NOME ou GFILIAL.NOME |
| xFant | dest | 0-1 | Elemento | FCFO.NOMEFANTASIA ou GFILIAL.NOMEFANTASIA |
| fone | dest | 0-1 | Elemento | FCFO.TELEFONE ou GFILIAL..TELEFONE |
| ISUF | dest | 0-1 | Elemento | Não será gerado |
| **enderDest** | **dest** | **1-1** | **Grupo** | **Dados do endereço** |
| xLgr | enderDest | 1-1 | Elemento | FCFO.RUA ou GFILIAL.RUA |
| nro | enderDest | 1-1 | Elemento | FCFO.NUMERO ou GFILIAL.NUMERO |
| xCpl | enderDest | 0-1 | Elemento | FCFO.COMPLEMENTO ou GFILIAL.COMPLEMENTO |
| xBairro | enderDest | 1-1 | Elemento | FCFO.BAIRRO ou GFILIAL.BAIRRO |
| cMun | enderDest | 1-1 | Elemento | Conforme classificação do município preenchido no Clie/For ou Filial |
| xMun | enderDest | 1-1 | Elemento | Conforme  município preenchido no Clie/For ou Filial |
| CEP | enderDest | 0-1 | Elemento | FCFO.CEP ou GFILIAL.CEP |
| UF | enderDest | 1-1 | Elemento | FCFO.CODETD ou GFILIAL.ESTADO |
| cPais | enderDest | 0-1 | Elemento | Conforme classificação do país preenchido no Clie/For ou Filial |
| xPais | enderDest | 0-1 | Elemento | GPAIS.DESCRICAO |
| email | dest | 0-1 | Elemento | Não será gerado |
