---
article_id: 360007713691
category: Gestão de Transportes (TMS)
content_hash: cc808abc773550eb0f1d1fc686222b7eafc28ab8141cf1e0027340a9ada31161
fetched_at: '2026-06-28T22:45:32.312293+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM251OPE Customizações
  de Usuário
type: support-article
updated_at: '2023-02-28T14:27:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007713691-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM251OPE-Customiza%C3%A7%C3%B5es-de-Usu%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:25 min  
  
Dúvida**Como implementar o ponto de entrada **TM251OPE** **-** **Customizações de Usuário**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM251OPE** está localizado logo após a realização efetiva da **Quitação/Autorização** de **Pagamento do Contrato** junto a **Operadora de Frotas**. Tem a finalidade de executar customizações de usuário.  
  
**Programa** **Fonte**: TMSA251.PRW  
  
**Sintaxe**: TM251OPE - Customizações de Usuário ( [ cCodOpe ], [ cFilOri ], [ cViagem ], [ cContrat ], [ cCodVei ], [ oXML ], [ lQuitacao ] ) --> Nil  
  
**Parâmetros**:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | cCodOpe |  |  | Caracter |  |  | Codigo da Operadora de Frotas |  |  |  |  |  |  |  |  |  |  |
|  | cFilOri |  |  | Array of Record |  |  | Codigo da Filial de Origem |  |  |  |  |  |  |  |  |  |  |
|  | cViagem |  |  | Array of Record |  |  | Codigo da Viagem |  |  |  |  |  |  |  |  |  |  |
|  | cContrat |  |  | Array of Record |  |  | Numero do Contrato |  |  |  |  |  |  |  |  |  |  |
|  | cCodVei |  |  | Array of Record |  |  | Codigo do Veiculo |  |  |  |  |  |  |  |  |  |  |
|  | oXML |  |  | Array of Record |  |  | Objeto o XML de retorno enviado pela Operadora |  |  |  |  |  |  |  |  |  |  |
|  | lQuitacao |  |  | Array of Record |  |  | Se T - Indica o Processamento da Quitacao do Contrato.Se F - Indica o Processamento da Autorizacao do Pagamento |  |  |  |  |  |  |  |  |  |  |

**Retorno**:  
  

**Nil**

(nulo)

**Exemplos**:  
  
*User Function* **TM251OPE**()

*MsgAlert*('Ponto de Entrada **TM251OPE**')

*Return Nil*  
  
**Variáveis**:  
​

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Escopo |  |  | Pode Alterar |  |  | descrição |  |
|  |  |  |  | Array of Record |  |  | Global |  |  | Não |  |  |  |
