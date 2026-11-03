---
article_id: 360007520772
category: Gestão de Transportes (TMS)
content_hash: d9a7cda6d13012406c3ec3c1bf315d4e21088a168abdf487630297d4f1bdc66e
fetched_at: '2026-06-28T22:45:32.367197+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM310TOK Processo de Fechamento
  da Viagem
type: support-article
updated_at: '2023-11-01T19:45:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007520772-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM310TOK-Processo-de-Fechamento-da-Viagem
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como implementar o ponto de entrada **TM310TOK -** **Processo de Fechamento da Viagem**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM310TOK** está localizado no fonte **TMSA310** - **Fechamento da Viagem** e é executado durante o processo de **Fechamento da Viagem**. Caso o retorno seja falso impede o fechamento da viagem inibindo inclusive a mensagem.  
  
**Programa** **Fonte**: **TMSA310.PRW**  
**Sintaxe**: TM310TOK - Processo de Fechamento da Viagem ( [ nOpcx ] ) --> lRet  
**Parâmetros**:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Nome | Tipo | Descrição | Default | Obrigatório | Referência |
| nOpcx | Array of Record |  |  |  |  |

**Retorno**:  
**lRet**     logico

* Caso o retorno seja (.F.) não permite fechar a viagem.

**Importante**No exemplo abaixo não permitimos fechar a viagem 000021, lembrando que a viagem está posicionada para validações.  
  
**Exemplos**:  
  
Local lRet := .T.

Local cViagem := DTQ->DTQ\_VIAGEM

Local nOpcx := PARAMIXB

Default nOpcx := ''

If cViagem == '000021'

lRet:= .F.

MsgAlert('Não é permitido fechar a viagem ' + DTQ->DTQ\_VIAGEM ,'Fechamento de Viagem')

End if

Return lRet
