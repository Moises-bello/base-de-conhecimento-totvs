---
content_hash: 4991d3c530d5ef039b57e573b40cd2074649b24dcd26c53a9ed5980dcb471416
fetched_at: '2026-06-29T00:12:15.603532+00:00'
page_id: '981002186'
product: rm
source: tdn-rm
title: Informações do Expedidor da Carga do CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=981002186
version: 5
---

# exped - Informações do Expedidor da Carga do CT-e

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **exped** | **[infCte](https://tdn.totvs.com/pages/viewpage.action?pageId=981000770)** | **0-1** | **Grupo** | **Informações do Expedidor da Carga** |
| CNPJ | exped | 1-1 | Elemento de Escolha | FCFO.CGCCFO ou GFILIAL.CGC |
| CPF | exped | 1-1 | FCFO.CGCCFO ou GFILIAL.CGC |
| IE | exped | 0-1 | Elemento | FCFO.INSCRESTADUAL ou GFILIAL.INSCRICAOESTADUAL |
| xNome | exped | 1-1 | Elemento | FCFO.NOME ou GFILIAL.NOME |
| fone | exped | 0-1 | Elemento | FCFO.TELEFONE ou GFILIAL..TELEFONE |
| **enderExped** | **exped** | **1-1** | **Grupo** | **Dados do endereço** |
| xLgr | enderExped | 1-1 | Elemento | FCFO.RUA ou GFILIAL.RUA |
| nro | enderExped | 1-1 | Elemento | FCFO.NUMERO ou GFILIAL.NUMERO |
| xCpl | enderExped | 0-1 | Elemento | FCFO.COMPLEMENTO ou GFILIAL.COMPLEMENTO |
| xBairro | enderExped | 1-1 | Elemento | FCFO.BAIRRO ou GFILIAL.BAIRRO |
| cMun | enderExped | 1-1 | Elemento | Conforme classificação do município preenchido no Clie/For ou Filial |
| xMun | enderExped | 1-1 | Elemento | Conforme  município preenchido no Clie/For ou Filial |
| CEP | enderExped | 0-1 | Elemento | FCFO.CEP ou GFILIAL.CEP |
| UF | enderExped | 1-1 | Elemento | FCFO.CODETD ou GFILIAL.ESTADO |
| cPais | enderExped | 0-1 | Elemento | Conforme classificação do país preenchido no Clie/For ou Filial |
| xPais | enderExped | 0-1 | Elemento | GPAIS.DESCRICAO |
| email | exped | 0-1 | Elemento | Não será gerado |
