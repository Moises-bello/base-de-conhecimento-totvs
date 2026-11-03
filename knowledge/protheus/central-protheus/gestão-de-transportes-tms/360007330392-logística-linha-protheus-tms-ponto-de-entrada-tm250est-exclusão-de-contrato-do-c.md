---
article_id: 360007330392
category: Gestão de Transportes (TMS)
content_hash: 811c3cee212c6f334ee17c4f38273c23c468d6bdc9fd349d2e2ec26928929aed
fetched_at: '2026-06-28T22:45:32.218796+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM250EST Exclusão de Contrato
  do Carreteiro
type: support-article
updated_at: '2022-11-29T20:12:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007330392-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM250EST-Exclus%C3%A3o-de-Contrato-do-Carreteiro
---

**Dúvida**Como implementar o ponto de entrada **TM250EST** Exclusão de Contrato do Carreteiro?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM250EST** está localizado no fonte **TMSA250** - Contrato de Carreteiro,e é executado após a exclusão do **Contrato do Carreteiro**.  
  
**Programa** **Fonte**: TMSA250.PRW  
  
**Sintaxe**: TM250EST - Exclusão de Contrato do Carreteiro ( [ cContrat ], [ lRet ] ) --> Nil  
  
**Parâmetros**:

* **cContrat**
  + **Tipo**: Array of Record
  + **Descrição**: Número do Contrato excluído.
* **lRet**
  + **Tipo**: Array of Record;
  + **Descrição**: Verifica se ocorreu algum erro durante a exclusão.

**Retorno**:  

* **Nil** - Não Tem

**Exemplo**:

```
User Function TM250Est()  
  
Local cContrat := ParamIXB[1]  
Local lRet := ParamIXB[2]  
  
If lRet  
    MsgAlert( 'O Contrato : ' + cContrat + ' foi excluido com sucesso ...', 'ATENCAO' )  
Else  
    MsgAlert( 'Ocorreu algum erro durante a exclusao' )  
End if  
  
Return Nil
```
