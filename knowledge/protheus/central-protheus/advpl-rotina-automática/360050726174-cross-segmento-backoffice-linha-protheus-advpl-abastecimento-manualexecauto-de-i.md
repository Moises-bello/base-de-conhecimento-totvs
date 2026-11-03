---
article_id: 360050726174
category: ADVPL - Rotina Automática
content_hash: 69f9a4bbf5216e59ebb0ce5626dedb696eeb6cff24d478cd416d88ba1b637e2a
fetched_at: '2026-06-28T22:40:23.909106+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Abastecimento Manual:ExecAuto()
  de inclusão
type: support-article
updated_at: '2021-12-29T13:18:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050726174-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Abastecimento-Manual-ExecAuto-de-inclus%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:00 min  
  
Dúvida**Qual o exemplo de ExecAuto() MNTA655, para inclusão?  
  
**Ambiente**Protheus – ADVPL – A partir da versão P12  
  
**Solução**Segue exemplo, lembrando que o parâmetro **MV\_NGGERPR** tem que estar configurado com '**S**'

```
#Include 'Totvs.ch'   
  
User Function MNT655EXEC()  
  
    // Processo de Inclusão  
    Local aAbast := {}  
    //Abre empresa/filial/modulo/arquivos  
  
    RPCSetEnv('99','01')  
    // Itens obrigatórios para inclusão do abastecimento para posto interno  
  
    aAbast := { {'TQN_PLACA' , '        '            , Nil },;  
                {'TQN_FROTA' , 'TESTE-COMB      '    , Nil },;  
                {'TQN_CNPJ'  , '43672104000155'      , Nil },;  
                {'TQN_CODCOM', '002'                 , Nil },;  
                {'TQN_DTABAS', StoD( '20200707' )    , Nil },;  
                {'TQN_HRABAS', '15:05'               , Nil },;  
                {'TQN_TANQUE', '  '                  , Nil },;  
                {'TQN_BOMBA' , '   '                 , Nil },;  
                {'TQN_QUANT' , 10                    , Nil },;  
                {'TQN_VALUNI', 0                     , Nil },;  
                {'TQN_VALTOT', 100                   , Nil },;  
                {'TQN_HODOM' , 0                     , Nil },;  
                {'TQN_CODMOT', '000001'              , Nil },;  
                {'TQN_POSTO' , 'COLAB '              , Nil },;  
                {'TQN_LOJA'  , 'SA'                  , Nil },;  
                {'TQN_NOTFIS', '000000013'             , Nil }}   
  
    lMSHelpAuto := .T. // Não apresenta erro em tela  
    lMSErroAuto := .F. // Caso a variável torne-se .T. apos MsExecAuto, apresenta erro em tela       
  
    MSExecAuto( { | v, x, y | MNTA655( v, x, y ) }, , aAbast, 3 )  
  
    If lMsErroAuto  
        If !IsBlind()            
            ConOut( "Ocorreu um error")  
        Else  
            cError := MostraErro( GetSrvProfString("Startpath","") , ) // Armazena mensagem de erro na raiz.  
            ConOut( cError)  
        EndIf  
    ELSE  
        ConOut( "Inclusão com sucesso")  
    EndIf  
RETURN
```

**Saiba Mais**  
**[MNTA655 Abastecimento Manual - Rotina Automática (ExecAuto)](https://tdn.totvs.com/pages/releaseview.action?pageId=525822084)**
