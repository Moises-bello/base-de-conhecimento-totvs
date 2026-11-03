---
article_id: 32552127877911
category: Originação de Grãos (OG)
content_hash: 459cb322051f14fd3b0fd47d712c4b92eefd34249614e0a2a3c70958b3d30453
fetched_at: '2026-06-28T22:45:42.749843+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para ajustar o código e loja
  Cliente/Fornecedor para buscar como NFs de complemento
type: support-article
updated_at: '2025-06-03T13:56:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32552127877911-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-ajustar-o-c%C3%B3digo-e-loja-Cliente-Fornecedor-para-buscar-como-NFs-de-complemento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32552127857943) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como fazer para ajustar o código e loja Cliente/Fornecedor para buscar como **NFs** de complemento. **Ponto de Entrada**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**O ponto de entrada **OGA430C1** está disponível na função que realiza o ajuste de dependência dos romaneios que requer **NF** de complemento na fixação do contrato na rotina do gestor de entidade. O ponto de entrada permite ajustar o código e loja do **cliente/fornecedor** para buscar as **NFs** dos romaneios com pendência que receberam a entidade trocada.

|  |  |
| --- | --- |
| **Localização:** | OGA430CREG() |
| **Programa Fonte:** | OGA430C |
| **Função:** | OGA430C1() |
| **Parâmetro:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | PARAMIXB[1] | Variedade | Caractere variável contendo código cliente/fornecedor | NÃO | | PARAMIXB[2] | Variedade | Caractere variável contendo a  Loja cliente/fornecedor | NÃO | | PARAMIXB[3] | Variedade | Caractere variável contendo o código do contrato | NÃO | | PARAMIXB[4] | Variedade | Caractere variável contendo código do Romaneio | NÃO | |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | aRtPE430C[1] | Variedade | Caractere variável contendo o  código cliente/fornecedor | NÃO | | aRtPE430C[2] | Variedade | Caractere variável contendo a  loja cliente/fornecedor | NÃO | |

**Visão Geral:**

`<``font` `style``=``"vertical-align: inherit;"``><``font` `style``=``"vertical-align: inherit;"``>Função de usuário OGA430C1()</``font``></``font``><``font``></``font``><``font` `style``=``"vertical-align: inherit;"``><``font` `style``=``"vertical-align: inherit;"``>`

`aRetOGA local := {}</``font``></``font``><``font``></``font``><``font` `style``=``"vertical-align: inherit;"``><``font` `style``=``"vertical-align: inherit;"``>`

`cTmpClFo local := PARAMIXB[1] //cCliFor</``font``></``font``><``font``></``font``><``font` `style``=``"vertical-align: inherit;"``><``font` `style``=``"vertical-align: inherit;"``>`

`cTmpLoja local := PARAMIXB[2] //cLoja</``font``></``font``><``font``></``font``><``font` `style``=``"vertical-align: inherit;"``><``font` `style``=``"vertical-align: inherit;"``>`

`cTmpCtr local := PARAMIXB[3] //cCtrato</``font``></``font``><``font``></``font``><``font` `style``=``"vertical-align: inherit;"``><``font` `style``=``"vertical-align: inherit;"``>`

`cTmpRom local := PARAMIXB[4] //cRomaneio</``font``></``font``><``font``></``font``>`

`<``font``></``font``><``font` `style``=``"vertical-align: inherit;"``><``font` `style``=``"vertical-align: inherit;"``>`

`//validações necessárias</``font``></``font``><``font``></``font``>`

`<``font``></``font``><``font` `style``=``"vertical-align: inherit;"``><``font` `style``=``"vertical-align: inherit;"``>`

`aadd(aRetOGA,cTmpClFo ) //Retorno para o campo de Cliente/Fornecedor da Nota Fiscal</``font``></``font``><``font``></``font``><``font` `style``=``"vertical-align: inherit;"``><``font` `style``=``"vertical-align: inherit;"``>`

`aadd(aRetOGA,cTmpLoja ) //Retorno para o campo de Loja Cliente/Fornecedor da Nota Fiscal</``font``></``font``><``font``></``font``>`

`<``font``></``font``><``font` `style``=``"vertical-align: inherit;"``><``font` `style``=``"vertical-align: inherit;"``>`
