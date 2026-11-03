---
article_id: 360062438773
category: RH - Integração
content_hash: 6599eda3ee1369771fb488553c87273dd830dad687d29a02e9e838cba38dad88
fetched_at: '2026-06-28T22:43:44.961298+00:00'
product: protheus
section_id: 360003115611
source: central-protheus
title: RH - Linha Protheus - GPE - GPM19INTEG - Qual o ponto de Entrada para integração
  de Roteiros definidos pelo usuário
type: support-article
updated_at: '2025-09-11T12:10:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062438773-RH-Linha-Protheus-GPE-GPM19INTEG-Qual-o-ponto-de-Entrada-para-integra%C3%A7%C3%A3o-de-Roteiros-definidos-pelo-usu%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28431983392407)**Tempo aproximado para leitura:**00:02:00** min

**Dúvida**GPM19INTEG - Qual o ponto de Entrada para integração de Roteiros definidos pelo usuário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Solução**Ponto de entrada que permite integrar com a folha determinados roteiros de cálculos, definidos pelo usuário.Para que roteiros customizados possam ser integrados com a folha, foi disponibilizado o Ponto de Entrada **GPM19INTEG**, onde através deste, o desenvolvedor deverá transitar para a folha os dados necessários, como verbas e valores.

Deverá utilizar o Array aRotMark que contém os dados necessários sobre os roteiros escolhidos para integrar.

Lembrando que nada impede à criação de roteiros definidos manualmente, porém para a transição para a Folha, a responsabilidade se torna do desenvolvedor, em alimentar as tabelas necessárias, como no exemplo abaixo onde há a transição para a RGB.

Como exemplo foi criado uma tabela RZZ com os campos de: Matrícula, Verba e Valor.

Esses dados serão transpostos para a tabela de incidências RGB.  
  
**Programa Fonte:** GPEM019.PRW  
**Retorno:** .T. para permitir a integração.  
  
**Exemplos:**#Include '[Protheus.ch](http://protheus.ch/)'

User Function GPM19INTEG()

Local aAreaRGB := RGB->( GetArea("RGB") )  
Local cPd := ""  
Local nValor := 0  
Local cPerFol := aRotMark[1,3] // Periodo  
Local cSemFol := aRotMark[1,5] // Semana  
Local cProc := aRotMark[1,1] // Processo  
Local cRoteiro := aRotMark[1,2] // Roteiro  
Local cRGBSeek := ""  
Local nIndice := RetOrder( "RGB", "RGB\_FILIAL+RGB\_MAT+RGB\_PD+RGB\_PERIOD+RGB\_SEMANA+RGB\_SEQ" )

DbSelectArea("RZZ")  
RZZ->( DbSetOrder(1) )

While RZZ->( !Eof() )

DbSelectArea("RGB")  
RGB->( DbSetOrder( nIndice ) )  
If !( RGB->( DbSeek( xFilial("RGB") + RZZ->RZZ\_MAT + RZZ->RZZ\_PD + cPerFol + "01", .F. ) ) )  
RGB->( RecLock( "RGB" , .T. ) )  
RGB->RGB\_FILIAL := xFilial("RGB")  
RGB->RGB\_MAT := RZZ->RZZ\_MAT  
RGB->RGB\_CC := "000001"  
RGB->RGB\_PD := RZZ->RZZ\_PD  
RGB->RGB\_HORAS := 0  
RGB->RGB\_VALOR := RZZ->RZZ\_VALOR  
RGB->RGB\_PARCEL := 0  
RGB->RGB\_PROCES := cProc  
RGB->RGB\_PERIOD := cPerFol  
RGB->RGB\_ROTEIR := cRoteiro  
RGB->RGB\_SEMANA := "01"  
RGB->RGB\_ROTORI := cRoteiro  
RGB->( MsUnlock() )  
EndIf  
  
RGB->( DbCloseArea() )  
RZZ->( DbSkip() )  
EndDo

RZZ->( DbCloseArea() )

RestArea( aAreaRGB )  
Return(.T.)

**Saiba Mais:**<https://tdn.totvs.com/pages/releaseview.action?pageId=243007532>
