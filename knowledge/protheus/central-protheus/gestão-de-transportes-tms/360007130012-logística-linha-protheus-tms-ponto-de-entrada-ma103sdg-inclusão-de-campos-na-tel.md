---
article_id: 360007130012
category: Gestão de Transportes (TMS)
content_hash: d9738960d42afb43b85aae91fb163189919fa153f15508832ebbc8ea5a67527d
fetched_at: '2026-06-28T22:45:29.555430+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada MA103SDG  Inclusão de Campos
  na Tela de Rateio
type: support-article
updated_at: '2022-06-21T11:26:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007130012-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-MA103SDG-Inclus%C3%A3o-de-Campos-na-Tela-de-Rateio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)  Tempo aproximado para leitura: 00:00:30 min  
  
Dúvida**Como implementar o ponto de entrada **MA103SDG** - Inclusão de Campos na Tela de Rateio?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada  **MA103SDG** está localizado na função **A103RATVEI**(), com finalidade de incluir novos campos na tela de Rateios por **Veículo**/**Viagem**.  
  
**Programa fonte**: **MATA103.PRW**  
  
**Sintaxe**: MA103SDG - Inclusão de Campos na Tela de Rateio ( ) --> aCposSDG  
  
**Retorno**  
aCposSDG  
  
       ()  
       Array contendo os novos campos a serem adicionados na tela de Rateios por Veículo/Viagem.  
  
**Exemplos**  
  
User Function MA103SDG()  
  
Local aCposSDG := {} //-- Novos campos que serão adicionados  
Local cCposSDG := ParamIXB //-- Campos que já fazem parte da tela padrão.  
  
AAdd(aCposSDG,"DG\_DESCRI")  
AAdd(aCposSDG,"DG\_DESVEI")   
AAdd(aCposSDG,"DG\_CONTA")  
  
Return aCposSDG  
  
**Variáveis**:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Tipo | Escopo | Pode Alterar | Descrição |
| cCposSDG | Caracter | Local | Não |  |
