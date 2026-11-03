---
content_hash: 2bd899e031fd0108763e97f71d799b1a5b3e8ca208426c65070ff19a15141846
fetched_at: '2026-06-29T00:12:02.438485+00:00'
page_id: '901953429'
product: rm
source: tdn-rm
title: Informação da NF modelo 21/22 referenciada (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901953429
version: 8
---

# gNF - Informação da NF modelo 21/22 referenciada

Este grupo esta associado ao **gSub (informações da substituição)** e deve ser gerado quando a Substituição for de Modelos 21 ou 22 por Modelo 62.

Gerado com as Dados do Movimento relacionado.

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **gNF** | **[gSub](https://tdn.totvs.com/pages/viewpage.action?pageId=901953395)** | **1-1** | **Grupo de Escolha** | **Informação da NF modelo 21/22 referenciada** |
| CNPJ | gNF | 1-1 | Elemento | Gerado com CNPJ da Filial Emitente do Documento Modelo 21 ou 22 que está sendo substituído |
| mod | gNF | 1-1 | Elemento | Gerado com o modelo de Documento associado ao Código de Documento, informado no Movimento. |
| serie | gNF | 1-1 | Elemento | Gerado com o Campo Serie informado no Movimento - Identificação TMOV.SERIE |
| nNF | gNF | 1-1 | Elemento | Gerado com o Número do Movimento - Identificação TMOV.NUMEROMOV |
| CompetEmis | gNF | 1-1 | Elemento | Gerado com a Data de Emissão - Identificação TMOV.DATAEMISSÃO |
| hash115 | gNF | 0-1 | Elemento | Gerado com o código de autenticação digital do documento fiscal. A informação é obtida do lançamento fiscal escriturado referente à nota sendo substituída. Identificação DLAF.CODAUTENTDIGITALDOC |

Exemploxml
54096208000185
62
21
123123
202509
]]>
