---
article_id: 360007450971
category: Gestão de Transportes (TMS)
content_hash: df67007ae14c46512e8823d4577573b4fe3a60579ec245d1296000c465804fa4
fetched_at: '2026-06-28T22:45:29.638565+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM040BUT Inclui botões
type: support-article
updated_at: '2022-01-18T18:03:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007450971-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM040BUT-Inclui-bot%C3%B5es
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)*** Tempo aproximado para leitura: **00:00:42 min  
  
Dúvida**Com o implementar o ponto de entrada **TM040BUT Inclui botões**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM040BUT** está localizado no **TMSA040** **Cotação de Frete** e permite ao usuário incluir botões na ***EnchoiceBar*** desta rotina.  
  
**Programa Fonte**: TMSA040.PRW  
  
**Sintaxe**: TM040BUT - Inclui Botões ( < nOpcx> ) --> aBotoesPe  
  
**Parâmetros**:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Nome | Tipo | Descrição | Default | Obrigatório | Referência |
| nOpcx | Array of Record |  |  | X |  |

**Retorno**:  
aBotoesPe  
               (vetor)  
               Array com os novos botões.  
  
**Exemplos**:  
User Function TM040BUT()  
Local aBotoesPe:={}  
Local nOpcx :=PARAMIXB[1]  
Aadd(aBotoesPE,{'PRECO',{|| TmsA040Leg() },'Mais um Botão'}) //Adicionado um botão na EnchoiceBar  
Return aBotoesPe
