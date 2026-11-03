---
article_id: 360007506872
category: Gestão de Transportes (TMS)
content_hash: 08429b426945b17adea7392e57eadee3b2f9f59d14ab533a8dd419129813281f
fetched_at: '2026-06-28T22:45:32.320455+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM300BUT Adiciona Botões
  - Tabela de Seguro
type: support-article
updated_at: '2023-03-01T20:10:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007506872-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM300BUT-Adiciona-Bot%C3%B5es-Tabela-de-Seguro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:35 min  
  
Dúvida**Como implementar o ponto de entrada TM300BUT Adiciona Botões - Tabela de Seguro?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM300BUT** está localizado no fonte **TMSA300** (**Tabela** **de** **Seguro**) e permite ao usuário adicionar botões na ***EnchoiceBar*** da rotina.  
  
  
**Programa** **Fonte**: TMSA300.PRW  
  
**Sintaxe**: TM300BUT - Adiciona Botões - Tabela de Seguro ( < Nill> ) --> aBotoesPE  
  
**Parâmetros**:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | Nill |  |  | Array of Record |  |  |  |  |  |  |  |  | X |  |  |  |  |

**Retorno**:  
  
**aBotoesPE**

(vetor)* Aray com os novos botões.

**Exemplos**:  
  
User Function TM300BUT()

Local aBotoesPe:={}

Aadd(aBotoesPE,{'PRECO',{|| TmsA040Leg() },'Mais um Botão'}) //Adicionado um botão na EnchoiceBar

Return aBotoesPe
