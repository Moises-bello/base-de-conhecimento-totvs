---
article_id: 360007447251
category: Gestão de Transportes (TMS)
content_hash: 480a9ff8f1a559659e4726d69f4350dd478fd7c7b44892a94456ff84476c54b1
fetched_at: '2026-06-28T22:45:29.597022+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM011BUT Inclui Botões
type: support-article
updated_at: '2022-06-21T11:20:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007447251-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM011BUT-Inclui-Bot%C3%B5es
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)  Tempo aproximado para leitura: 00:00:15 min  
  
Dúvida**Como implementar o ponto de entrada **TM011BUT** Inclui Botões?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM011BUT** está localizado no **TMSA011** **Ajuste da Tabela de Frete**, permite ao usuário adicionar botões na ***EnchoiceBar*** da rotina.  
  
**Programa Fonte**:**TMSA011.PRW**  
  
**Sintaxe**: TM011BUT - Inclui Botões ( [ Nill ] ) --> aBotoesPe

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
  
User Function TM011BUT()   
  
Local aBotoesPe:={}   
  
Aadd(aBotoesPE,{'PRECO',{|| TmsA040Leg() },'Mais um Botão'}) //Adicionado um botão na EnchoiceBar   
  
Return aBotoesPe
