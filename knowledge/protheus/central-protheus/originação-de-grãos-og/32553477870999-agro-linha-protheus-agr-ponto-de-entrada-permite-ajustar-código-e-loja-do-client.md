---
article_id: 32553477870999
category: Originação de Grãos (OG)
content_hash: 0b32aabbab73e434dc86a3d94eff4fa21746a680ab6b86db9e38ccffb885c907
fetched_at: '2026-06-28T22:45:43.102962+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada permite ajustar código e loja
  do cliente/fornecedor para listar os documentos fiscais
type: support-article
updated_at: '2025-07-14T19:51:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32553477870999-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-permite-ajustar-c%C3%B3digo-e-loja-do-cliente-fornecedor-para-listar-os-documentos-fiscais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32553468029079) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como funciona esse processo do **Ponto de Entrada permite ajustar código e loja do cliente/fornecedor** **para listar os documentos fiscais**?  
  
**Ambiente**  
TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
O ponto de entrada **OGA430G1** está disponível na função que monta os dados para listar as **NFs** de complemento dos romaneios que tiveram dependência na fixação do contrato na rotina do gestor da entidade. O ponto de entrada permite ajustar o código e loja do **cliente/fornecedor** para buscar as **NFs** de complemento dos romaneios que receberam a entidade trocada

|  |  |
| --- | --- |
| **Localização:** | FQUERY() |
| **Programa Fonte:** | OGA430G |
| **Função:** | OGA430G1() |
| **Parâmetro:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | PARAMIXB[1] | Variedade | Caractere variável contendo código cliente/fornecedor | NÃO | | PARAMIXB[2] | Variedade | Caractere variável contendo a  Loja cliente/fornecedor | NÃO | | PARAMIXB[3] | Variedade | Caractere variável contendo o código do contrato | NÃO | | PARAMIXB[4] | Variedade | Caractere variável contendo código do Romaneio | NÃO | |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | aRtPE430G[1] | Variedade | Caractere variável contendo o  código cliente/fornecedor | NÃO | | aRtPE430G[2] | Variedade | Caractere variável contendo a  loja cliente/fornecedor | NÃO | |

**Visão Geral:**

`User Function OGA430G1() <``font``></``font``>`

`<``font``></``font``>`

`Local aRet  := {}<``font``></``font``>`

`Local cTmpClFo := PARAMIXB[1]   //código cliente/fornecedor<``font``></``font``>`

`Local cTmpLoja := PARAMIXB[2]   //loja cliente/fornecedor<``font``></``font``>`

`Local cTmpCtr  := PARAMIXB[3]   //código contrato<``font``></``font``>`

`Local cTmpRom  := PARAMIXB[4]   //código romaneio<``font``></``font``>`

`<``font``></``font``>`

`//validação necessárias<``font``></``font``>`

`<``font``></``font``>`

`aadd(aRet,cTmpClFo))    <``font``></``font``>`

`aadd(aRet,cTmpLoja)) <``font``></``font``>`

`<``font``></``font``>`

`Return aRet`
