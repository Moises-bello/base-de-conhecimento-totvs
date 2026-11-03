---
article_id: 32797452284823
category: Originação de Grãos (OG)
content_hash: 6fe3052da76e89dcf63fcd1819b9bc43b64278d8124eea3b5aaf82b41b67c57f
fetched_at: '2026-06-28T22:45:42.883366+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para Buscar dados contábeis
  para Título de PR
type: support-article
updated_at: '2025-06-13T21:13:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32797452284823-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-Buscar-dados-cont%C3%A1beis-para-T%C3%ADtulo-de-PR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32797452264343) Tempo aproximado para leitura: **00:01:50 min** **Dúvida**Como funciona o **Ponto de Entrada para Buscar dados contábeis para Título de PR**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | OGX018A | Geração de Títulos no Financeiro | |
| **País(es):** | Todos |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Localização:** | Ao confirmar Acordo de Troca. |
| **Programa Fonte:** | OGX018A |
| **Função:** | Buscar dados contábeis para criação do título de PR. |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | OGX018ACTB | Nenhum | Envia como parâmetro o negócio e a operação contábil. | NÃO | |

**Exemplo:**

#incluir ' [protheus.ch](http://protheus.ch/) '

#include ' [parmtype.ch](http://parmtype.ch/) ' 

 

Função de usuário OGX018ACTB()

Local aDados := aClone(PARAMIXB[1])  
Local aRet := {} //Personalizações do usuário  
Local aDadosCfo := {}  
Local aAreaNJR := NJR->(GetArea())  
Local aAreaN9A := N9A->(GetArea())  
Local aAreaSA1 := SA1->(GetArea())  
Local aAreaSF4 := SF4->(GetArea())  
Local cOperacao := ""  
Local cCultura := ""  
  
DbSelectArea('NJR')  
DbSetOrder(1)  
  
If NJR->(DbSeek(xFilial('NJR')+aDados[1]))  
  
DbSelectArea('SB5')  
DbSetOrder(1)  
  
If SB5->(DbSeek(xFilial('SB5')+NJR->NJR\_CODPRO))  
cCultura := SB5->B5\_CULTRA  
Endif  
  
DbSelectArea('N9A')  
DbSetOrder(1)

Se N9A->(DbSeek(xFilial('N9A')+aDados[1]))  
  
DbSelectArea('SF4')  
DbSetOrder(1)  
  
Se SF4->(DbSeek(xFilial('SF4')+N9A->N9A\_TES))  
Se !Empty(SF4->F4\_CF)

dbSelectArea("SA1")  
dbSetOrder(1)  
If SA1->(DbSeek(FWxFilial()+aDados[2]+aDados[3]))  
  
Aadd(aDadosCfo,{"OPERNF","S"})  
Aadd(aDadosCfo,{"TPCLIFOR",SA1->A1\_TIPO})  
Aadd(aDadosCfo,{"UFDEST",SA1->A1\_EST})  
Aadd(aDadosCfo,{"INSCR" ,SA1->A1\_INSCR})  
If SA1->(FieldPos("A1\_CONTRIB")) > 0  
Aadd(aDadosCfo,{"CONTR", SA1->A1\_CONTRIB})  
Endif  
  
cCfop := MaFisCFO(,SF4->F4\_CF,aDadosCfo)  
cOperação := IIF(DIREITA(ALLTRIM(cCfop),3)=='501','120201',IIF(ESQUERDA(cCfop,1)=='7','120101','110101'))  
Fim se

Fim  
se fim se fim  
  
se  
  
fim se

RestArea(aAreaNJR)  
RestArea(aAreaN9A)  
RestArea(aAreaSF4)  
RestArea(aAreaSA1)

aAdd( aRet, { cCultura , cOperacao } )  
Return aRet
