---
article_id: 360007428311
category: Gestão de Transportes (TMS)
content_hash: 0df8aa0b035fffae0b1a39cb1bd51df655a67263cf0c56aa5db716cb4971ba2f
fetched_at: '2026-06-28T22:45:29.588505+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada T250PER Geração por Período
type: support-article
updated_at: '2022-06-20T18:59:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007428311-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-T250PER-Gera%C3%A7%C3%A3o-por-Per%C3%ADodo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)  Tempo aproximado para leitura: 00:00:25 min  
  
Dúvida**Como implementar o ponto de entrada **T250PER** Geração por Período?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada  **T250PER** está localizado no programa **TMSA250** Contrato de Carreteiro e dentro do *loop* em caso de geração por período, após a exclusão da tabela **DTY**.

**Programa Fonte**: **TMSA250**  
  
**Sintaxe**: T250PER - Geração por Período ( [ **DTY\_FILORI** ] [ **DTY\_VIAGEM** ] [ **DTY\_NUMCTC** ] )  
  
**Retorno**:  
()  
  
**Exemplos**:   
  
User Function T250PER()   
  
Local FilOri := PARAMIXB[1]  
Local Viagem := PARAMIXB[2]  
Local NumCtc := PARAMIXB[3]  
  
MsgAlert( 'Filial de origem:' + FilOri +, 'ATENCAO' )  
MsgAlert( 'Viagem:' + Viagem +, 'ATENCAO' )  
MsgAlert( 'Numero de Contrato:' + NumCtc +, 'ATENCAO' )  
  
Return Nil  
  
**Parâmetros**:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Nome | Tipo | Descrição | Default | Obrigatório | Referência |
| DTY\_FILORI | Array of Record | Filial de Origem do contrato |  |  |  |
| DTY\_VIAGEM | Array of Record | Número da Viagem |  |  |  |
| DTY\_NUMCTC | Array of Record | Número do Contrato |  |  |  |
