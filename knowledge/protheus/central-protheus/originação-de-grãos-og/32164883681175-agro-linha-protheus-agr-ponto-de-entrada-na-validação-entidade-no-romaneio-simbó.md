---
article_id: 32164883681175
category: Originação de Grãos (OG)
content_hash: e97d15c599d03ccf0d9c7936d18fa35a72f8f110e12a7b3245a118643f9bfcf4
fetched_at: '2026-06-28T22:45:42.698360+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada na Validação entidade no romaneio
  simbólico
type: support-article
updated_at: '2025-08-20T20:01:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32164883681175-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-na-Valida%C3%A7%C3%A3o-entidade-no-romaneio-simb%C3%B3lico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32164883656087) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como encontrar o **Ponto de Entrada na Validação entidade no romaneio simbólico**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Características do Requisito:**O ponto de entrada **OGA251R1** esta localizado na rotina de romaneio sem pesagem, na função que gera automático os  romaneios simbólicos no Sistema. Este ponto de entrada substitui a validação da entidade e loja do romaneio com a entidade e loja do contrato, usada por padrão no sistema, ficando a validação a critério do ponto de entrada.

|  |  |
| --- | --- |
| **Localização:** | OGA251GSimb |
| **Programa Fonte:** | OGA251 |
| **Função:** | OGA251R1 |
| **Parâmetros:** | |  |  |  |  | | --- | --- | --- | --- | | **Parametro** | **Tipo** | **Descrição** | **Obrigatório** | | PARAMIXB[1] | Array | Variável caractere contendo o código da entidade do contrato | NÃO | | PARAMIXB[2] | Array | Variável caractere contendo a loja da entidade do contrato | NÃO | | PARAMIXB[3] | Array | Variável caractere contendo o código da entidade do romaneio | NÃO | | PARAMIXB[4] | Array | Variável caractere contendo o loja da entidade do romaneio | NÃO | |
| **Retorno**: | Variável logica True(.T.) ou False(.F.) |

  
**EXEMPLO DE UTILIZAÇÃO:**

|  |
| --- |
| `User Function OGA251R1()`  `Local aAreaAtu  := GetArea()`  `Local lRetorno  := .F.`  `//Local cEntCtr := PARAMIXB[1]   //Entidade do Contrato`  `//Local cLojCtr := PARAMIXB[2]   //Loja do Contrato`  `//Local cEntRom := PARAMIXB[3]   //Entidade do Romaneio`  `//Local cLojRom := PARAMIXB[4]   //Loja do Romaneio`    `//fazer as validações necessárias`    `lRetorno := .T.`    `Return lRetorno` |
