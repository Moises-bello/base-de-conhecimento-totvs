---
content_hash: 91212f713b8820427955a00541a1211c48e568e91b8dc05db64fdb733a675b95
fetched_at: '2026-06-29T00:12:15.595339+00:00'
page_id: '981002055'
product: rm
source: tdn-rm
title: Informações do Remetente do CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=981002055
version: 4
---

# rem - Informações do Remetente das mercadorias transportadas pelo CT-e

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **rem** | **[infCte](https://tdn.totvs.com/pages/viewpage.action?pageId=981000770)** | **0-1** | **Grupo** | **Informações do Remetente das mercadorias transportadas pelo CT-e**  DFILIAL.SUBLIMITEEXCEDIDO |
| CNPJ | rem | 1-1 | Elemento de Escolha | FCFO.CGCCFO ou GFILIAL.CGC |
| CPF | rem | 1-1 | FCFO.CGCCFO ou GFILIAL.CGC |
| IE | rem | 0-1 | Elemento | FCFO.INSCRESTADUAL ou GFILIAL.INSCRICAOESTADUAL |
| xNome | rem | 1-1 | Elemento | FCFO.NOME ou GFILIAL.NOME |
| xFant | rem | 0-1 | Elemento | FCFO.NOMEFANTASIA ou GFILIAL.NOMEFANTASIA |
| fone | rem | 0-1 | Elemento | FCFO.TELEFONE ou GFILIAL..TELEFONE |
| **enderReme** | **rem** | **1-1** | **Grupo** | **Dados do endereço** |
| xLgr | enderReme | 1-1 | Elemento | FCFO.RUA ou GFILIAL.RUA |
| nro | enderReme | 1-1 | Elemento | FCFO.NUMERO ou GFILIAL.NUMERO |
| xCpl | enderReme | 0-1 | Elemento | FCFO.COMPLEMENTO ou GFILIAL.COMPLEMENTO |
| xBairro | enderReme | 1-1 | Elemento | FCFO.BAIRRO ou GFILIAL.BAIRRO |
| cMun | enderReme | 1-1 | Elemento | Conforme classificação do município preenchido no Clie/For ou Filial |
| xMun | enderReme | 1-1 | Elemento | Conforme  município preenchido no Clie/For ou Filial |
| CEP | enderReme | 0-1 | Elemento | FCFO.CEP ou GFILIAL.CEP |
| UF | enderReme | 1-1 | Elemento | FCFO.CODETD ou GFILIAL.ESTADO |
| cPais | enderReme | 0-1 | Elemento | Conforme classificação do país preenchido no Clie/For ou Filial |
| xPais | enderReme | 0-1 | Elemento | GPAIS.DESCRICAO |
| email | rem | 0-1 | Elemento | Não será gerado |
