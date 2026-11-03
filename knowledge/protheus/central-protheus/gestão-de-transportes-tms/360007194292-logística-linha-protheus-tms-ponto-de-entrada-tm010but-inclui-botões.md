---
article_id: 360007194292
category: Gestão de Transportes (TMS)
content_hash: d8221ffe1ff5d3a7fc10abaee139ba884e016a49584d16241432c8c7dad9116a
fetched_at: '2026-06-28T22:45:29.592871+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM010BUT Inclui Botões
type: support-article
updated_at: '2022-06-21T11:18:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007194292-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM010BUT-Inclui-Bot%C3%B5es
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:15 min  
  
Dúvida**Como implementar o ponto de entrada **TM010BUT** - **Inclui Botões**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM010BUT** está localizado no **TMSA010** **Tabela de Frete** e permite ao usuário adicionar botões na ***EnchoiceBar*** da rotina.  
  
**Programa Fonte**: TMSA010.PRW  
  
**Sintaxe**: TM010BUT - Inclui Botões ( [ Nill ] ) --> aBotoesPe  
  
**Parâmetros**:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Nome | Tipo | Descrição | Default | Obrigatório | Referência |
| Nill | Array of Record |  |  |  |  |

**Retorno:**  
aBotoesPe  
                (vetor)  
                Array com os novos botões a serem adicionados.  
  
**Exemplos:**  
  
User Function TM010BUT()   
Local aBotoesPe:={}   
Aadd(aBotoesPE,{'PRECO',{|| TmsA040Leg() },'Mais um Botão'}) //Adicionado um botão na EnchoiceBar   
Return aBotoesPe
