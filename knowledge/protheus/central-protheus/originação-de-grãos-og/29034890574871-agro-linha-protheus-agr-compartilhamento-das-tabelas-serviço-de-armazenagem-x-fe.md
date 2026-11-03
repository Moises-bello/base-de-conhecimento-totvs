---
article_id: 29034890574871
category: Originação de Grãos (OG)
content_hash: 97c38801ef856346244dd52e979c163b6d286efa2b70ea1f1862b64d4a3f6edf
fetched_at: '2026-06-28T22:45:37.639259+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Compartilhamento das tabelas - Serviço de Armazenagem
  x Fechamento Serviços
type: support-article
updated_at: '2025-05-05T19:23:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29034890574871-Agro-Linha-Protheus-AGR-Compartilhamento-das-tabelas-Servi%C3%A7o-de-Armazenagem-x-Fechamento-Servi%C3%A7os
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29034890549527) Tempo aproximado para leitura: **00:01:40 min****Dúvida**  
Como é realizado um **Compartilhamento das tabelas - Serviço de Armazenagem x Fechamento Serviços**?   
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Para o **Serviço de Armazenagem**, ao confirmar o **acerto** dará origem ao**Fechamento do Serviço**, ou seja aos documentos fiscais de cobrança ou de saída do depósito em caso de retenção.   
Ao realizar este fechamento é gerado registro da cobrança do serviço relacionando a nota de serviço ao documento fiscal  ou a geração do documento de saída do depósito.  
Para os casos de retenção é gerado um **romaneio de retenção**.

Orientamos que utiliza a tabela NKS (fechamento Serviço de Armazenagem) com mesmo compartilhamento da tabela NKG (Acerto dos serviços Armazenagem) para que ao gerar o romaneio seja possível identificar o registro de origem através do documento fiscal e romaneio gerado.

|  |  |
| --- | --- |
| **NKG - Serviço Armazenagem** | **NKS - Fechamento Serviço** |
| Exclusivo | Exclusivo |

## **Exemplo:**

|  |
| --- |
| //Exemplo de Função de Acerto para ajustar a filial NKS conforme a filial da tabela NKG.  #INCLUDE "PROTHEUS.CH"    USER FUNCTION FAjustaNKS  Local nPos       := 0 Local aNKS       := {} lOCAL nI         := 0 Local cQuery     := "" Local cAliasQry  := GetNextAlias()      cQuery := " SELECT NKG\_FILIAL, NKG\_FECSER "     cQuery += " FROM " + RetSqlName('NKG') + " NKG "     cQuery += " WHERE NKG.D\_E\_L\_E\_T\_ = '' "     cQuery += " AND NKG\_FECSER <> ' ' "     cQuery := ChangeQuery( cQuery )      dbUseArea( .T., "TOPCONN", TCGENQRY(,,cQuery), cAliasQry, .F., .T.)     dbSelectArea(cAliasQry)     While !(cAliasQry)->( Eof() )             nPos  a  := aScan( aNKS, { |x| AllTrim( x[1] ) == AllTrim((cAliasQry)->NKG\_FECSER) } )         If nPos == 0             aAdd( aNKS, { (cAliasQry)->NKG\_FECSER, (cAliasQry)->NKG\_FILIAL} )                           EndIf         (cAliasQry)->(DbSkip())     EndDO      If  Len(aNKS) > 0         For nI := 1 to Len(aNKS)                       dbSelectArea("NKS")             NKS->(dbSetOrder(1))             if NKS->(DBSeek(PADR("",TamSX3("NKS\_FILIAL")[1])+aNKS[nI,1]))                           if  RecLock('NKS',.f.)                           NKS->NKS\_filiaL := aNKS[nI,2]                     NKS->(MsUnLock())                 ENDIF             ENDIF             Next nI             EndIF return |
