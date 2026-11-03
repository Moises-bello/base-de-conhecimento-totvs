---
content_hash: 78e6c5f157e691813965cb0a3ffe09fad835779c439559d6e6ca16d7288cfcbf
fetched_at: '2026-06-29T00:12:15.696643+00:00'
page_id: '981783628'
product: rm
source: tdn-rm
title: Indicador do papel do Tomador CT-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Indicador+do+papel+do+Tomador+CT-e
version: 7
---

# Indicador do "papel do Tomador do Serviço no CT-e

Tomadortoma 3

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **toma3** | **[ide](https://tdn.totvs.com/pages/viewpage.action?pageId=981001839)** | **1-1** | **Grupo de Escolha** | **Indicador do "papel do Tomador do Serviço no CT-e** |
| toma | toma3 | 1-1 | Elemento | TMOVTRANSP.TOMADORTIPO  Definido no Movimento |

toma 4

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **toma4** | **[ide](https://tdn.totvs.com/pages/viewpage.action?pageId=981001839)** | **1-1** | **Grupo de Escolha** | **Indicador do "papel do Tomador do Serviço no CT-e** |
| toma | toma4 | 1-1 | Elemento | TMOVTRANSP.TOMADORTIPO  Definido no Movimento |
| CNPJ | toma4 | 1-1 | Elemento de Escolha | Definido no Cliente/Fornecedor relacionado ao Movimento do CT-e |
| CPF | toma4 | 1-1 |
| IE | toma4 | 0-1 | Elemento | Definido no Cliente/Fornecedor relacionado ao Movimento do CT-e |
| **--- x — Sequência opcional do XML: Sempre será gerado** | | | | |
| xNome | toma4 | 1-1 | Elemento da Sequência | FCFO.NOME  Definido no Cliente/Fornecedor relacionado ao Movimento do CT-e |
| xFant | toma4 | 0-1 | Elemento da Sequência | FCFO.NOMEFANTASIA  Definido no Cliente/Fornecedor relacionado ao Movimento do CT-e |
| fone | toma4 | 0-1 | Elemento da Sequência | FCFO.TELEFONE  Definido no Cliente/Fornecedor relacionado ao Movimento do CT-e |
| **enderToma** | **toma4** | **1-1** | **Grupo da Sequência** | **Dados do endereço** |
| xLgr | enderToma | 1-1 | Elemento | FCFO.RUA  Definido no Cliente/Fornecedor relacionado ao Movimento do CT-e |
| nro | enderToma | 1-1 | Elemento | FCFO.NUMERO  Definido no Cliente/Fornecedor relacionado ao Movimento do CT-e |
| xCpl | enderToma | 0-1 | Elemento | FCFO.COMPLEMENTO  Definido no Cliente/Fornecedor relacionado ao Movimento do CT-e |
| xBairro | enderToma | 1-1 | Elemento | FCFO.BAIRRO  Definido no Cliente/Fornecedor relacionado ao Movimento do CT-e |
| cMun | enderToma | 1-1 | Elemento | Classificação do município conforme definido no Cliente/Fornecedor relacionado ao Movimento do CT-e |
| xMun | enderToma | 1-1 | Elemento | FCFO.CIDADE  Definido no Cliente/Fornecedor relacionado ao Movimento do CT-e |
| CEP | enderToma | 0-1 | Elemento | FCFO.CEP  Definido no Cliente/Fornecedor relacionado ao Movimento do CT-e |
| UF | enderToma | 1-1 | Elemento | FCFO.CODETD  Definido no Cliente/Fornecedor relacionado ao Movimento do CT-e |
| cPais | enderToma | 0-1 | Elemento | Classificação do país conforme definido no Cliente/Fornecedor relacionado ao Movimento do CT-e |
| xPais | enderToma | 0-1 | Elemento | GPAIS.DESCRICAO  Definido no Cliente/Fornecedor relacionado ao Movimento do CT-e |
| email | enderToma | 0-1 | Elemento da Sequência | Não será gerado |
| **Fim da sequência opcional do XML — x ---** | | | | |
