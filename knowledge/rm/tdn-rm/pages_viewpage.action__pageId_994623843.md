---
content_hash: 62058c122ab8cac46b16769e6c83c8702932d234d32f1a2931a33847c170330d
fetched_at: '2026-06-29T00:12:16.605086+00:00'
page_id: '994623843'
product: rm
source: tdn-rm
title: Informações do Tomador/Usuário do  Serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=994623843
version: 1
---

# toma - Informações do Tomador/Usuário do  Serviço

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| toma | **[infCte](https://tdn.totvs.com/pages/viewpage.action?pageId=981000770)** | **0-1** | **Grupo** | **Informações do Tomador/Usuário do Serviço** |
| CNPJ | toma | 1-1 | Elemento de Escolha | FCFO.CGCCFO ou GFILIAL.CGC |
| CPF | toma | 1-1 | FCFO.CGCCFO ou GFILIAL.CGC |
| IE | toma | 0-1 | Elemento | FCFO.INSCRESTADUAL ou GFILIAL.INSCRICAOESTADUAL |
| xNome | toma | 1-1 | Elemento | FCFO.NOME ou GFILIAL.NOME |
| xFant | toma | 0-1 | Elemento | FCFO.NOMEFANTASIA ou GFILIAL.NOMEFANTASIA |
| fone | toma | 0-1 | Elemento | FCFO.TELEFONE ou GFILIAL..TELEFONE |
| ISUF | toma | 0-1 | Elemento | Não será gerado |
| **enderToma** | **toma** | **1-1** | **Grupo** | **Dados do endereço** |
| xLgr | enderToma | 1-1 | Elemento | FCFO.RUA ou GFILIAL.RUA |
| nro | enderToma | 1-1 | Elemento | FCFO.NUMERO ou GFILIAL.NUMERO |
| xCpl | enderToma | 0-1 | Elemento | FCFO.COMPLEMENTO ou GFILIAL.COMPLEMENTO |
| xBairro | enderToma | 1-1 | Elemento | FCFO.BAIRRO ou GFILIAL.BAIRRO |
| cMun | enderToma | 1-1 | Elemento | Conforme classificação do município preenchido no Clie/For ou Filial |
| xMun | enderToma | 1-1 | Elemento | Conforme  município preenchido no Clie/For ou Filial |
| CEP | enderToma | 0-1 | Elemento | FCFO.CEP ou GFILIAL.CEP |
| UF | enderToma | 1-1 | Elemento | FCFO.CODETD ou GFILIAL.ESTADO |
| cPais | enderToma | 0-1 | Elemento | Conforme classificação do país preenchido no Clie/For ou Filial |
| xPais | enderToma | 0-1 | Elemento | GPAIS.DESCRICAO |
| email | toma | 0-1 | Elemento | Não será gerado |
