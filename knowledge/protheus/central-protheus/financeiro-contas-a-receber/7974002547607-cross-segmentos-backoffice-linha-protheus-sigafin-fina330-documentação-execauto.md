---
article_id: 7974002547607
category: Financeiro - Contas a Receber
content_hash: 39d45f4ef7fe508c85eef27be578ca0f925f1d183a78a7106dd9bd5cf6049700
fetched_at: '2026-06-28T22:38:14.065078+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA330 - Documentação
  execauto
type: support-article
updated_at: '2022-08-17T22:14:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7974002547607-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA330-Documenta%C3%A7%C3%A3o-execauto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Qual a documentação para executar a rotina FINA330 via execauto?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA330 - Todas as versões

**Solução**

Para execução automática da compensação de contas a receber, é necessário o uso da função **MaIntBxCr()**.  
Por meio dessa função, é possível realizar a compensação automática entre dois títulos a receber (NF x **Adiantamento**).

### Parâmetros da rotina

| Posição | Parâmetro | Tipo | Descrição |
| --- | --- | --- | --- |

| 1 | nCaso | numeric | Código da operação a ser efetuada (numérico).  [1] **Baixa simples do financeiro**; [2] **Liquidação de** **títulos**; [3] **Compensação de títulos de mesma carteira** (**RA**/**NCC**). |
| 2 | aSE1 | array | Vetor com os *RECNOs* dos títulos a serem baixados (exemplo: **NF** ou **boleto**). |
| 3 | aBaixa | array | Vetor com os dados da baixa simples do financeiro.  [1] **Motivo da Baixa**; [2] **Valor Recebido**; [3] **Banco**; [4] **Agência**; [5] **Conta**; [6] **Data de Crédito**; [7] **Data da Baixa**. |
| 4 | aNCC\_RA | array | Vetor com os *RECNOs* dos títulos de créditos a serem compensados (exemplo: **RA** ou **NCC**) |
| 5 | aLiquidacao | array | Vetor  com os dados da liquidação do financeiro.  [1] **Prefixo**; [2] **Banco**; [3] **Agencia**; [4] **Conta**; [5] **Numero do Cheque**; [6] **Data Boa**; [7] **Valor**; [8] **Tipo**; [9] **Natureza**; [10] **Moeda**. |
| 6 | aParam | array | Vetor com os parâmetros da rotina  [1] **Contabiliza On-Line**; [2] **Aglutina Lançamentos** **Contábeis**; [3] **Digita lançamentos contábeis**; [4] **Juros** **para Comissão**; [5] **Desconto para Comissão**; [6] **Calcula Comissão**. |
| 7 | NIL | NIL | Parâmetro interno. |
| 8 | aEstorno | array | Vetor com o campo **E5\_DOCUMEN** referente à movimentação de compensação que se deseja estornar, podendo a sequência ser passada opcionalmente. Caso a sequência não seja informada, todas as compensação relativas aos documentos informados serão estornadas. Exemplo: {{{**cDocumen**}, **cSeq**}} ou {{**cDocumen**}} |
| 9 | NIL | NIL | Parâmetro interno. |
| 10 | NIL | NIL | Parâmetro interno. |
| 11 | nSaldoComp | numeric | Valor a compensar - Informe o valor que deseja compensar. Este valor deve ser menor ou igual ao saldo do título e maior que zero. Para compensação total, informar NIL. |
| 12 | aCpoUser | array | Vetor com os campos de usuário para gravação da liquidação. |
| 13 | aNCC\_RAvlr | array | Parâmetro interno. |
| 14 | nSomaCheq | numeric | Parâmetro interno. |
| 15 | nTaxaCM | numeric | Taxa para correção monetária. |
| 16 | aTxMoeda | array | Vetor com as **taxas das moedas** existentes.  [1] **Moeda**; [2] **Taxa da Moeda**; |
| 17 | lConsdAbat | logical | Variável logica para consideração dos abatimentos. |
| 18 | NIL | NIL | Parâmetro interno. |
| 19 | NIL | NIL | Parâmetro interno. |

Exemplo de utilização:

**Exemplo #01 - Rotina automática para compensação**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73 | `#INCLUDE``"PROTHEUS.CH"`  `#INCLUDE``"TBICONN.CH"`      `//-------------------------------------------------------------------`  `/*/ MaIntBxCr`  `Exemplo de compensação de títulos normais com adiantamentos - CR`    `@since 27/07/2021`  `@version 1.0`  `/*/`  `//-------------------------------------------------------------------`  `USER FUNCTION CmpAutCR()`    `Local lRetOK := .T.`  `Local aArea  := GetArea()`    `Local nTaxaCM :=``5.2322`  `Local aTxMoeda := {}`    `Local nSaldoComp:=``1000.00` `*nTaxaCM``// Valor a ser compensado (Caso seja parcial Pode ser parcial) - Compensar apenas R$ 50,00`    `Private nRecnoNDF`  `Private nRecnoE1`    `PREPARE ENVIRONMENT EMPRESA``"TI"` `FILIAL``"D MG 01 "` `MODULO``"FIN"` `TABLES``"SE2TI0"``,``"SE5TI0"``,``"SA6TI0"``,``"SEDTI0"`    `Conout(``"----Inicio da Rotina Automatica!------"``)`    `dbSelectArea(``"SE1"``)`  `dbSetOrder(``2``)``// E1_FILIAL, E1_CLIENTE, E1_LOJA, E1_PREFIXO, E1_NUM, E1_PARCELA, E1_TIPO, R_E_C_N_O_, D_E_L_E_T_`  `IF dbSeek(XFILIAL(``"SE1"``)+``"000000"``+``"00"``+``"331"``+``"RA0001   "``+``"  "``+``"RA "``)`  `nRecnoRA := RECNO()`  `IF dbSeek(XFILIAL(``"SE1"``)+``"000000"``+``"00"``+``"331"``+``"000001   "``+``"  "``+``"DP "``)`  `nRecnoE1 := RECNO()`    `PERGUNTE(``"FIN330"``,.F.)`  `lContabiliza    := (MV_PAR09 ==``1``)``// Contabiliza On Line ?`  `lDigita         := (MV_PAR07 ==``1``)``// Mostra Lanc Contab ?`  `lAglutina       := .F.`    `/*`  `==> Utilizar esse trecho se quiser simular o botão Taxas da tela inicial do FINA330`  `==> Verifique os parâmetros MV_CMP330 e MV_CMTXCON para tal.`  `nTaxaCM := RecMoeda(dDataBase,SE1->E1_MOEDA)`    `aAdd(aTxMoeda, {1, 1} )`  `aAdd(aTxMoeda, {2, nTaxaCM} )`  `*/`  `SE1->(dbSetOrder(``1``))``//E1_FILIAL+E1_PREFIXO+E1_NUM+E1_PARCELA+E1_TIPO+E1_FORNECE+E1_LOJA`    `//NF X RA`  `aRecRA := { nRecnoRA }`  `aRecSE1 := { nRecnoE1 }`    `/*`  `//RA X NF`  `aRecRA := { nRecnoE1 }`  `aRecSE1 := { nRecnoRA }`  `*/`    `If !MaIntBxCR(``3``, aRecSE1,,aRecRA,,{lContabiliza,lAglutina,lDigita,.F.,.F.,.F.},,,,,nSaldoComp,,,, nTaxaCM, aTxMoeda)`  `Help(``"XAFCMPAD"``,``1``,``"HELP"``,``"XAFCMPAD"``,``"Não foi possível a compensação"``+CRLF+``" do titulo de adiantamento"``,``1``,``0``)`  `lRet := .F.`  `ENDIF`  `ENDIF`  `ENDIF`    `RestArea(aArea)`    `RESET ENVIRONMENT`    `Return lRet` |

**Exemplo #02 - Rotina automática para compensação ou estorno**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98 | `#INCLUDE``"PROTHEUS.CH"`  `#include``"tbiconn.ch"`    `user function xCmpCR()`  `local aPerg as array`  `local aRet as array`  `local aEstorno as array`  `local aRecTit as array`  `local aRecCmp as array`  `local aRecEst as array`  `local aRecEst1 as array`  `local aTxMoeda as array`  `local cRecTit as character`  `local cRecCmp as character`  `local cJanela as character`  `local cCodCanc as character`  `local cValor as character`  `local cSeq as character`  `local lContabiliza as logical`  `local lAglutina as logical`  `local lDigita as logical`  `local lHelp as logical`  `local lConsdAbat as logical`  `local nSldComp as numeric`  `local nHdl as numeric`  `local nOperacao as numeric`  `local nTaxaCM as numeric`    `cJanela :=``"Compensação automática CR"`  `aPerg := {}`  `aRet := {}`  `aEstorno := {}`  `aRecTit := {}`  `aRecCmp := {}`  `aRecEst := {}`  `aRecEst1 := {}`  `aTxMoeda := {}`  `cSeq := cValor := cCodCanc := cRecTit := cRecCmp := replicate(``" "``,``50``)`  `nSldComp =``0`  `nHdl :=``0`  `nOperacao :=``0`  `nTaxaCM :=``0`  `lHelp := .F.`  `lConsdAbat := .F.`    `PREPARE ENVIRONMENT EMPRESA``"T1"` `FILIAL``"D MG 01 "` `MODULO``"FIN"`  `conOut(``"INICIO DA ROTINA AUTOMATICA"``)`    `PERGUNTE(``"AFI340"``,.F.)`  `lContabiliza := MV_PAR11 ==``1`  `lAglutina := MV_PAR08 ==``1`  `lDigita := MV_PAR09 ==``1`    `aAdd(aPerg,{``1``,``'RecNo título de partida'``, cRecTit,``"@"``, nil, nil, nil,``50``, .T.})`  `aAdd(aPerg,{``1``,``'RecNo título a compensar'``, cRecCmp,``"@"``, nil, nil, nil,``50``, .T.})`  `aAdd(aPerg,{``2``,``'Comp/Est?'``,``"1"``, {``"1=Compensação"``,``"2=Estorno"``},``100``, nil, .T.})`  `aAdd(aPerg,{``1``,``'Valor'``, cValor,``"@"``, nil, nil, nil,``50``, .F.})`  `aAdd(aPerg,{``1``,``'Sequencia Est.'``, cRecCmp,``"@"``, nil, nil, nil,``50``, .F.})`    `if` `paramBox(aPerg, cJanela, aRet)`  `aAdd(aRecTit, val(aRet[``1``]))`  `cSeq := AllTrim(aRet[``5``])`  `if` `aRet[``3``] =``"1"`  `aAdd(aRecCmp, val(aRet[``2``]))`  `else`  `aAdd(aRecEst, getDocumen(val(aRet[``2``])))`  `if` `cSeq =``""`  `aAdd(aEstorno, aRecEst)`  `else`  `aAdd(aEstorno, {aRecEst,cSeq})`  `endif`  `endif`  `if` `!Empty(AllTrim(aRet[``4``]))`  `nSldComp := val(aRet[``4``])`  `else`  `nSldComp := nil`  `endif`    `if` `MaIntBxCR(``3``, aRecTit, nil ,aRecCmp, nil,{lContabiliza,lAglutina,lDigita,.F.,.F.,.F.},nil,aEstorno,nil,nil,nSldComp,nil,nil,nil, nTaxaCM, aTxMoeda, lConsdAbat)`  `conOut(``"Processo concluido com exito."``)`  `else`  `conOut(``"Processo nao concluido."``)`  `endif`  `endif`    `conOut(``"FIM DA ROTINA AUTOMATICA"``)`  `RESET ENVIRONMENT`  `Return nil`    `static` `function getDocumen(nRecSe1 as numeric)`  `local cDocumen as character`  `default` `cDocumen :=``""`    `SE1->(DbGoTo(nRecSe1))`  `If SE1->(Recno()) == nRecSe1`  `cDocumen := SE1->E1_PREFIXO + SE1->E1_NUM + SE1->E1_PARCELA + SE1->E1_TIPO + SE1->E1_LOJA`  `EndIf`  `return` `cDocumen` |

**Saiba mais**  
[FIN0023\_CREC\_Compensacao\_receber\_execauto](https://tdn.totvs.com/display/public/PROT/FIN0023_CREC_Compensacao_receber_execauto)
