---
content_hash: 9ba10f9dd9c45d8918b02479df1b1c331302898b1bc941b92ec5318989bc4973
fetched_at: '2026-06-29T00:12:02.310544+00:00'
page_id: '900727029'
product: rm
source: tdn-rm
title: Endereço do emitente (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=900727029
version: 6
---

# enderEmit - Endereço do emitente

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **enderEmit** | **[emit](https://tdn.totvs.com/pages/viewpage.action?pageId=900452652)** | **1-1** | **Grupo** | **Endereço do emitente** |
| xLgr | enderEmit | 1-1 | Elemento | Tipo de Rua + o campo Endereço informado na aba Endereço do cadastro da Filial. |
| nro | enderEmit | 1-1 | Elemento | Campo Número informado na aba Endereço do cadastro da Filial. |
| xCpl | enderEmit | 0-1 | Elemento | Campo Complemento informado na aba Endereço do cadastro da Filial.  Se não possuir este campo não será gerado |
| xBairro | enderEmit | 1-1 | Elemento | Tipo de Bairro + o campo Bairro do cadastro da Filial. |
| cMun | enderEmit | 1-1 | Elemento | Classificação IBGE vinculada ao cadastro do município da Filial Emitente |
| xMun | enderEmit | 1-1 | Elemento | Nome do município da Filial Emitente informado no cadastro. |
| CEP | enderEmit | 1-1 | Elemento | Informado na aba endereço do cadastro da Filial. |
| UF | enderEmit | 1-1 | Elemento | Estado selecionado na aba endereço do cadastro da Filial. |
| fone | enderEmit | 0-1 | Elemento | DDD + Telefone do Cadastro da Filial | pasta Endereço.  Se não possuir este campo não será gerado |
| email | enderEmit | 0-1 | Elemento | e-mail do Cadastro da Filial | pasta Endereço.  Se não possuir este campo não será gerado |

Exemploxml
Avenida Raja Gabaglia
2664
4º andar
Estoril
3106200
BeloHorizonte
30494170
MG
3132215566
teste@totvs.com.br
]]>
