---
article_id: 360007451431
category: Gestão de Transportes (TMS)
content_hash: 1e27b48941ac060f4939b97a54bdb4215ff76cbd8b7a5359e076ee84660261b0
fetched_at: '2026-06-28T22:45:29.645366+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM040CFA Visualização de
  campos customizados na tabela DF1
type: support-article
updated_at: '2022-01-18T17:59:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007451431-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM040CFA-Visualiza%C3%A7%C3%A3o-de-campos-customizados-na-tabela-DF1
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)*** Tempo aproximado para leitura: **00:00:48 min  
  
Dúvida**Como implementar o ponto de entrada **TM040CFA** **Visualização de campos customizados na tabela DF1**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM040CFA** está localizado no **TMSA040****Cotação de Frete** e permite o usuário visualizar o conteúdo dos campos customizados da tabela **DF1****Itens do Agendamento**, na tabela **DT4****Cotação de Frete** quando a função **Cotação** da rotina de agendamento for utilizado.  
  
**Programa Fonte**: TMSA040.PRW  
  
**Sintaxe**: TM040CFA - Visualização de campos customizados na tabela DF1 ( [ ] )  
  
**Parâmetros**:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Nome | Tipo | Descrição | Default | Obrigatório | Referência |
|  | Array of Record |  |  |  |  |

**Retorno:**  
()  
  
**Exemplos**:  
#Include 'Protheus.ch'  
User Function TM040CFA()  
//-- O campo customizado da tabela DT4 recebe o conteúdo do campo customizado da tabela DF1 //-- carregado no ponto de entrada TMF05CFA  
M->DT4\_TESTE := \_cCampo  
Return  
  
**Variáveis**:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Tipo | Escopo | Pode Alterar | Descrição |
|  | Array of Record | Global | Não |  |
