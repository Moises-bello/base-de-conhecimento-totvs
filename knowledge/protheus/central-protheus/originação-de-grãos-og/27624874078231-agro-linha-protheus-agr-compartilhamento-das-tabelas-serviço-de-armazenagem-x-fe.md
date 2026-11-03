---
article_id: 27624874078231
category: Originação de Grãos (OG)
content_hash: 84d3dad63a8e0215a1efdf0d587f73c36f283da9d156b8f97d250ceef6c52daa
fetched_at: '2026-06-28T22:45:37.665397+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Compartilhamento das tabelas - Serviço de Armazenagem
  x Fechamento Serviços
type: support-article
updated_at: '2025-05-05T20:05:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27624874078231-Agro-Linha-Protheus-AGR-Compartilhamento-das-tabelas-Servi%C3%A7o-de-Armazenagem-x-Fechamento-Servi%C3%A7os
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27624874050071) Tempo aproximado para leitura: **00:00:45 min** **Dúvida**Para que serve **Compartilhamento das tabelas - Serviço de Armazenagem x Fechamento Serviços**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12 **Solução  
Compartilhamento das tabelas - Serviço de Armazenagem x Fechamento Serviços**:Para o **Serviço de Armazenagem**, ao confirmar a origem **certa** ao **Fechamento do Serviço**, ou seja aos documentos fiscais de cobrança ou de saída do depósito em caso de retenção.   
Ao realizar este fechamento é gerado registro de cobrança de serviço relacionado à nota de serviço ao documento fiscal ou à geração do documento de saída do depósito.  
Para os casos de retenção é gerado um **romaneio de retenção** .  

Orientamos que utilizamos a tabela **NKS -** **fechamento Serviço de Armazenagem** com o mesmo compartilhamento da tabela **NKG - Acerto dos serviços Armazenagem** para que ao gerar o romaneio seja possível identificar o registro de origem através do documento fiscal e romaneio gerado.

|  |  |
| --- | --- |
| **NKG - Serviço de Armazenagem** | **NKS - Fechamento Serviço** |
| Exclusivo | Exclusivo |

**Exemplo:**

|  |
| --- |
| //Exemplo de Função de Acerto para ajustar a filial NKS conforme a filial da tabela NKG.  #INCLUIR "PROTHEUS.CH"    FAJUSTANKS DE FUNÇÕES DO USUÁRIO  Local nPos := 0 Local aNKS := {} lOCAL nI := 0 Local cQuery := "" Local cAliasQry := GetNextAlias ​​() cQuery := " SELECIONE NKG\_FILIAL, NKG\_FECSER " cQuery += " DE " + RetSqlName ( 'NKG' ) + " NKG " cQuery += " ONDE NKG.D\_E\_L\_E\_T\_ = '' " cQuery += " E NKG\_FECSER <> ' ' " cQuery := ChangeQuery ( cQuery ) dbUseArea ( .T. , "TOPCONN" , TCGENQRY ( ,, cQuery ) , cAliasQry , .F. , .T. ) dbSelectArea ( cAliasQry ) Enquanto !( cAliasQry ) -> ( Eof () ) nPos a := aScan ( aNKS , { | x | AllTrim ( x [ 1 ] ) == AllTrim (( cAliasQry ) -> NKG\_FECSER ) } ) Se nPos == 0 aAdd ( aNKS , { ( cAliasQry ) -> NKG\_FECSER , ( cAliasQry ) -> NKG\_FILIAL } )                   EndIf         ( cAliasQry ) -> ( DbSkip ()) EndDO Se Len ( aNKS ) > 0 Para nI := 1 para Len ( aNKS )           dbSelectArea ( "NKS" ) NKS -> ( dbSetOrder ( 1 )) se NKS -> ( DBSeek ( PADR ( "" ,TamSX3 ( "NKS\_FILIAL" )[ 1 ]) + aNKS [nI , 1 ]))           if RecLock ( 'NKS' , .f. )       NKS -> NKS\_filiaL := aNKS [ nI , 2 ] NKS -> ( MsUnLock ()) ENDIF ENDIF Próximo nI EndIF retornar |
