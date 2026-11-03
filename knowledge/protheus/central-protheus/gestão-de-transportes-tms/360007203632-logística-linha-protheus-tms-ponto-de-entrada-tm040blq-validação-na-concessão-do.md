---
article_id: 360007203632
category: Gestão de Transportes (TMS)
content_hash: 8c02858559ae2f9d6da9da3a161911ca516809b4fdf4094a165de269091082cc
fetched_at: '2026-06-28T22:45:29.633087+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM040BLQ Validação na Concessão
  do Desconto Máximo
type: support-article
updated_at: '2022-01-18T13:53:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007203632-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM040BLQ-Valida%C3%A7%C3%A3o-na-Concess%C3%A3o-do-Desconto-M%C3%A1ximo
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)*** Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como implementar o ponto de entrada **TM040BLQ** **Validação na Concessão do Desconto Máximo**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM040BLQ** está localizado no **TMSA040** **Cotação de Frete** e permite ao usuário efetuar validação na concessão do desconto máximo permitido. Lembrando que ao se utilizar esse ponto de entrada para efetuar as validações do desconto, as validações da rotina padrão serão desprezadas.  
  
**Programa Fonte**: TMSA040.PRW  
  
**Sintaxe**: TM040BLQ - Validação na Concessão do Desconto Máximo ( [ Nulo ] ) --> lRet  
**Parâmetros**:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Nome | Tipo | Descrição | Default | Obrigatório | Referência |
| Nulo | Nulo |  |  |  |  |

**Retorno:**  
lRet  
         (logico)  
         Se o Retorno estiver (.T.) permite conceder o desconto.  
  
**Exemplos**:  
#Include "Protheus.ch"  
User Function TM040BLQ()   
Local lRet := .F.  
Local cCodUser := RetCodUsr()  
If cCodUser == '000000'   
        lRet := .T.  
End If   
Return lRet  
  
**Variáveis**:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Tipo | Escopo | Pode Alterar | Descrição |
|  | Array of Record | Global | Não |  |
