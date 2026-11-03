---
article_id: 360007317992
category: Gestão de Transportes (TMS)
content_hash: d92c60cfe8c424109cf70361cfafd2002ae06adb52b8a714eb67d8f7352065a8
fetched_at: '2026-06-28T22:45:32.182738+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM250BUT Adiciona Botões
  na Tela de Visualização de Contrato Carreteiro
type: support-article
updated_at: '2022-11-30T17:54:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007317992-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM250BUT-Adiciona-Bot%C3%B5es-na-Tela-de-Visualiza%C3%A7%C3%A3o-de-Contrato-Carreteiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:40 min**

**Dúvida**Como implementar o ponto de entrada TM250BUT - Adiciona Botões na Tela de Visualização de Contrato Carreteiro?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM250BUT** permite adicionar botões na tela de **Visualização de Contrato Carreteiro**.

**Programa** **Fonte**: TMSA250.PRW  
  
**Sintaxe**: TM250BUT - Adiciona Botões na Tela de Visualização de Contrato Carreteiro. ( < nOpc> ) --> aRet  
  
**Parâmetros**:

* Nome: nOpc
  + Tipo: Array of Record

**Retorno**:

**aRet - Vetor -** Contém quais os botões serão exibidos em tela além do padrão.

**Exemplos**:

```
User Function TM250BUT()  
   
Local aRet := {}  
Local nOpcx := ParamIXB[1]  
  
If nOpcx == 2 //-- Visualizar   
        Aadd(aRet,{'PMSDOC',{||U_Função a Ser Chamada ('DTQ',M->DTQ_VIAGEM,3)},'Desc. Botão','Desc. Botão'})   
End If  
  
Return(aRet)
```
