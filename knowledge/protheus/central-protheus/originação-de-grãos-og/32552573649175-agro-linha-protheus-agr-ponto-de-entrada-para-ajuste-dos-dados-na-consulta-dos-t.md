---
article_id: 32552573649175
category: Originação de Grãos (OG)
content_hash: 6c9252bf7bfe66d8c4d2e9ba2d71fe59fe0d642f7bbad81fb1a6a8602488ebb1
fetched_at: '2026-06-28T22:45:42.765769+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para ajuste dos dados na consulta
  dos títulos financeiros do romaneio
type: support-article
updated_at: '2025-06-03T14:28:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32552573649175-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-ajuste-dos-dados-na-consulta-dos-t%C3%ADtulos-financeiros-do-romaneio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32552529287831) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como realizar o ajuste dos dados na consulta dos títulos financeiros do romaneio?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**O ponto de entrada **OGA430D1** esta disponível na função que realiza o ajuste de pendencia dos romaneios com valor de fixação a menor do contrato na rotina do gestor de entidade. O ponto de entrada permite ajustar os dados para a busca e ajuste dos títulos financeiro dos romaneios que tiveram a entidade trocada.

|  |  |
| --- | --- |
| **Localização:** | FAJUFINA() |
| **Programa Fonte:** | OGA430D |
| **Função:** | OGA430D1() |
| **Parametro:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | PARAMIXB[1] | Array | Variável caractere contendo o numero do documento fiscal | NÃO | | PARAMIXB[2] | Array | Variável caractere contendo a serie do documento fiscal | NÃO | | PARAMIXB[3] | Array | Variável caractere contendo  o código do cliente/fornecedor | NÃO | | PARAMIXB[4] | Array | Variável caractere contendo a loja do cliente/fornecedor | NÃO | | PARAMIXB[5] | Array | Variável caractere contendo  o código do contrato | NÃO | | PARAMIXB[6] | Array | Variável caractere contendo  o código do romaneio | NÃO | |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | aRtPE430D[1] | Array | Variável caractere contendo o numero do documento fiscal | NÃO | | aRtPE430D[2] | Array | Variável caractere contendo a serie do documento fiscal | NÃO | | aRtPE430D[3] | Array | Variável caractere contendo o código cliente/fornecedor | NÃO | | aRtPE430D[4] | Array | Variável caractere contendo a loja cliente/fornecedor | NÃO | |

**Visão Geral:**

`User Function OGA430D1()`

`Local aRet := {}`

`Local cTmpDoc := PARAMIXB[1] //numero doc fiscal`

`Local cTmpSer := PARAMIXB[2] //serie doc fiscal`

`Local cTmpClFo := PARAMIXB[3] //codigo cliente/fornecedor`

`Local cTmpLoja := PARAMIXB[4] //loja cliente/fornecedor`

`Local cTmpCtr := PARAMIXB[5] //codigo contrato`

`Local cTmpRom := PARAMIXB[6] //loja contrato`

`//validações necessárias`

`aadd(aRet,cTmpDoc)`

`aadd(aRet,cTmpSer)`

`aadd(aRet,cTmpClFo)`

`aadd(aRet,cTmpLoja)`

`Return aRet`
