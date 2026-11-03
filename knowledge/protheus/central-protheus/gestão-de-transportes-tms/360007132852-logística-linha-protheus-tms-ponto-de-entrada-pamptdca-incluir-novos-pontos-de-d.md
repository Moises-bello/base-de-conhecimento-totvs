---
article_id: 360007132852
category: Gestão de Transportes (TMS)
content_hash: eaa9db31fcee6b1a0ac39aab63a567ef96baceebd4285d1a863f0fb8b3ff4ebb
fetched_at: '2026-06-28T22:45:29.574454+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada PAMPTDCA Incluir novos
  pontos de descarga
type: support-article
updated_at: '2022-06-21T11:21:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007132852-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-PAMPTDCA-Incluir-novos-pontos-de-descarga
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)  Tempo aproximado para leitura: 00:00:20 min  
  
Dúvida**Como implementar o ponto de entrada **PAMPTDCA** Incluir novos pontos de descarga?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **PAMPTDCA** foi disponibilizado para permitir a inclusão de novos pontos de descarga quando fizer Integração com a **Pamcard**.  
  
**Programa Fonte**: **TMSpamcard.prw**  
  
**Eventos de chamada do Ponto de Entrada**: PAMPTDCA()  
  
**Retorno**: Return (aPtoDca)  
  
**Exemplos**:  
  
#Include 'Protheus.ch'  
User Function PAMPTDCA()  
  
Local aPtoUsr := {}   
Local aPtoDca := {{ '', '' }}   
Local cFilOri :=PARAMIXB[1]   
Local cViagem :=PARAMIXB[2]  
  
If ValType(aPtoUsr) == "A"   
       Aadd(aPtoDca, { 'N09209', 'SP' } ) //--Código de origem + Grupo de região   
       MSGALERT("TESTE para incluir novos pontos de descarga")   
EndIf   
  
Return (aPtoDca)
