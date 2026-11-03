---
content_hash: 5342a03e1edac2ed26add47ea78434a696f9e3e8478b76609455feeaa285f06f
fetched_at: '2026-06-29T00:12:15.621373+00:00'
page_id: '981002295'
product: rm
source: tdn-rm
title: Informações do Recebedor da Carga do CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=981002295
version: 4
---

# receb - Informações do Recebedor da Carga

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **receb** | **[infCte](https://tdn.totvs.com/pages/viewpage.action?pageId=981000770)** | **0-1** | **Grupo** | **Informações do Recebedor da Carga** |
| CNPJ | receb | 1-1 | Elemento de Escolha | FCFO.CGCCFO ou GFILIAL.CGC |
| CPF | receb | 1-1 | FCFO.CGCCFO ou GFILIAL.CGC |
| IE | receb | 0-1 | Elemento | FCFO.INSCRESTADUAL ou GFILIAL.INSCRICAOESTADUAL |
| xNome | receb | 1-1 | Elemento | FCFO.NOME ou GFILIAL.NOME |
| xFant | receb | 0-1 | Elemento | FCFO.NOMEFANTASIA ou GFILIAL.NOMEFANTASIA |
| fone | receb | 0-1 | Elemento | FCFO.TELEFONE ou GFILIAL..TELEFONE |
| **enderReceb** | **receb** | **1-1** | **Grupo** | **Dados do endereço** |
| xLgr | enderReceb | 1-1 | Elemento | FCFO.RUA ou GFILIAL.RUA |
| nro | enderReceb | 1-1 | Elemento | FCFO.NUMERO ou GFILIAL.NUMERO |
| xCpl | enderReceb | 0-1 | Elemento | FCFO.COMPLEMENTO ou GFILIAL.COMPLEMENTO |
| xBairro | enderReceb | 1-1 | Elemento | FCFO.BAIRRO ou GFILIAL.BAIRRO |
| cMun | enderReceb | 1-1 | Elemento | Conforme classificação do município preenchido no Clie/For ou Filial |
| xMun | enderReceb | 1-1 | Elemento | Conforme  município preenchido no Clie/For ou Filial |
| CEP | enderReceb | 0-1 | Elemento | FCFO.CEP ou GFILIAL.CEP |
| UF | enderReceb | 1-1 | Elemento | FCFO.CODETD ou GFILIAL.ESTADO |
| cPais | enderReceb | 0-1 | Elemento | Conforme classificação do país preenchido no Clie/For ou Filial |
| xPais | enderReceb | 0-1 | Elemento | GPAIS.DESCRICAO |
| email | receb | 0-1 | Elemento | Não será gerado |
