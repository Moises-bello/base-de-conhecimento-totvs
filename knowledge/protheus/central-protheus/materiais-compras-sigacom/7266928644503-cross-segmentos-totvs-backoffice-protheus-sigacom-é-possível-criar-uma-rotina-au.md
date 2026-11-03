---
article_id: 7266928644503
category: Materiais - Compras (SIGACOM)
content_hash: 2659f9641b0a2856cfd614499ed40e71315c40883c602dc5eca5be33c8d1e0ce
fetched_at: '2026-06-28T22:41:17.527147+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - É possível criar uma
  rotina automática para o cadastro de Produto x Fornecedor - MATA061 ?
type: support-article
updated_at: '2022-11-17T03:22:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7266928644503-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-%C3%89-poss%C3%ADvel-criar-uma-rotina-autom%C3%A1tica-para-o-cadastro-de-Produto-x-Fornecedor-MATA061
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00**:20:00 min****Dúvida**Existe um meio de criar uma automatização da rotina MATA061 - Produto x Fornecedor  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Compras - Todas as versões  
  
**Solução**Para casos onde necessita de realizar inclusão/alteração/exclusão de registros da MATA061 em grande escala, possuímos o exemplo de rotina automática abaixo:

**Exemplo de inclusão:**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48 | `#Include``"Protheus.ch"`  `#Include``"RwMake.ch"`  `#Include``"TbiConn.ch"`    `User Function EXEC061()`    `Local nOpc :=``3`  `Local oModel := Nil`  `Local cProd061 :=``"0002"`  `Local cForn1 :=``"001"`  `Local cLoja1 :=``"01"`  `Local cForn2 :=``"002"`  `Local cLoja2 :=``"01"`    `PREPARE ENVIRONMENT EMPRESA``"32"` `FILIAL``"6597"` `MODULO``"COM"`    `oModel := FWLoadModel(``'MATA061'``)`    `oModel:SetOperation(nOpc)`  `oModel:Activate()`    `//Cabeçalho`  `oModel:SetValue(``'MdFieldSA5'``,``'A5_PRODUTO'``,cProd061)`  `oModel:SetValue(``'MdFieldSA5'``,``'A5_NOMPROD'``,``'PRODUTO 061 CT001'``)`    `//Grid`  `oModel:SetValue(``'MdGridSA5'``,``'A5_FORNECE'``,cForn1)`  `oModel:SetValue(``'MdGridSA5'``,``'A5_LOJA'` `,cLoja1)`  `//oModel:SetValue('MdGridSA5','A5_NOMEFOR', 'FOR. P/ ROTINA MATA061 - CT001')`    `//Nova linha na Grid`  `oModel:GetModel(``"MdGridSA5"``):AddLine()`    `oModel:SetValue(``'MdGridSA5'``,``'A5_FORNECE'``,cForn2)`  `oModel:SetValue(``'MdGridSA5'``,``'A5_LOJA'` `,cLoja2)`  `//oModel:SetValue('MdGridSA5','A5_NOMEFOR', 'FOR. P/ ROTINA MATA061 - CT001')`    `If oModel:VldData()`  `oModel:CommitData()`  `Endif`    `oModel:DeActivate()`    `oModel:Destroy()`    `RESET ENVIRONMENT`    `Return` |

**Exemplo de alteração:**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50 | `#Include``"Protheus.ch"`  `#Include``"RwMake.ch"`  `#Include``"TbiConn.ch"`    `User Function EXEC061()`    `Local nOpc :=``4`  `Local oModel := Nil`  `Local oGridMod := Nil`  `Local cProd061 :=``"0002"`  `Local cForn1 :=``"001"`  `Local cLoja1 :=``"01"`  `Local cForn2 :=``"002"`  `Local cLoja2 :=``"01"`  `Local lFind  := .F.`    `PREPARE ENVIRONMENT EMPRESA``"32"` `FILIAL``"6597"` `MODULO``"COM"`    `//Posicionar na SA5 no registro a ser alterado`  `DbSelectArea(``"SA5"``)`  `SA5->(DbSetOrder(``1``))`  `If SA5->(DbSeek(xFilial(``"SA5"``) + cForn2 + cLoja2 + cProd061))`    `oModel      := FWLoadModel(``'MATA061'``)`  `oGridMod    := oModel:GetModel(``"MdGridSA5"``)`    `oModel:SetOperation(nOpc)`  `oModel:Activate()`    `lFind := oGridMod:SeekLine({{``"A5_FORNECE"``,cForn2},{``"A5_LOJA"``,cLoja2},{``"A5_PRODUTO"``,cProd061}})`    `If lFind`  `oModel:SetValue(``'MdGridSA5'``,``'A5_FORNECE'``,cForn2)`  `oModel:SetValue(``'MdGridSA5'``,``'A5_LOJA'` `,cLoja2)`  `oModel:SetValue(``'MdGridSA5'``,``'A5_NOMEFOR'``,``'FOR. ALTERADO'``)`  `oModel:SetValue("MdGridSA5``','``A5_CODPRF``','``TESPRF')`  `Endif`    `If oModel:VldData()`  `oModel:CommitData()`  `Endif`    `oModel:DeActivate()`    `oModel:Destroy()`  `Endif`    `RESET ENVIRONMENT`    `Return` |

**Exemplo de alteração e exclusão de linha:**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98 | `#INCLUDE``'RWMAKE.CH'`  `#INCLUDE``'TBICONN.CH'`  `#INCLUDE``'PROTHEUS.CH'`  `#INCLUDE``'FWMVCDEF.CH'`    `User Function MyMata061()`    `Local nLenProd  :=``0`        `//-- Controle de tamanho de campo de produto`  `Local lOk       := .T.``//-- Controle de validação e commit`  `Local aErro     := {}``//-- Recebe msg de erro de processamento`  `Local oModel061 := NIL``//-- Modelo de Dados Mata061`  `Local oModelGrid:= NIL``//-- Modelo de Dados Grid`  `Local cProd     :=``"PR-001"` `//-- Produto a ser alterado`  `Local cForn     :=``""`       `//-- Fornecedor posiciondo`  `Local cLoja     :=``""`       `//-- Loja do Fornecedor posicionado`  `Local cForn01   :=``"000002"` `//-- Fornecedor a ser alterado`  `Local cLoja01   :=``"01"`     `//-- Loja do Fornecedor a ser alterado`  `Local cForn02   :=``"000005"` `//-- Fornecedor a ser excluido`  `Local cLoja02   :=``"01"`     `//-- Loja do Fornecedor a ser excluido`  `Local nX        :=``0`      `//-- Inicializa o ambiente`  `PREPARE ENVIRONMENT EMPRESA``"01"` `FILIAL``"01"` `MODULO``"COM"`    `nLenProd := TamSX3(``"A5_PRODUTO"``)[``1``]``//-- Obtem tamanho do campo A5_PRODUTO`  `DbSelectArea(``"SA5"``)`  `SA5->(DbSetOrder(``2``))``//-- A5_FILIAL+A5_PRODUTO+A5_FORNECE+A5_LOJA`    `// Posiciona na amarração`  `If SA5->(DbSeek(xFilial(``"SA5"``) + Padr(cProd, nLenProd) + cForn01 + cLoja01))`      `//-- Carrega o modelo de dados e seleciona a operação de aprovação (UPDATE)`  `oModel061 := FWLoadModel(``'MATA061'``)`  `oModel061:SetOperation( MODEL_OPERATION_UPDATE )``// Alteração`  `oModel061:Activate()`    `oModelGrid := oModel061:GetModel(``'MdGridSA5'``)`    `// Percorre a Grid para posicionar os itens a alterar e excluir`  `For nX :=``1` `to oModelGrid:Length()`  `oModelGrid:GoLine(nX)`  `If !oModelGrid:Isdeleted()``//Verifica se a linha está deletada`  `cForn := oModelGrid:GetValue(``'A5_FORNECE'``)`  `cLoja := oModelGrid:GetValue(``'A5_LOJA'``)`    `// Verifica se é o Fornecedor a alterar`  `If cForn+cLoja == cForn01+cLoja01`  `oModelGrid:SetValue(``'A5_CODPRF'``,``'Teste alteração'``)``// Altera campo`  `Endif`    `// Verifica se é o Fornecedor a excluir`  `If cForn+cLoja == cForn02+cLoja02`  `oModelGrid:DeleteLine()``// Deleta linha do Fornecedor`  `Endif`  `EndIf`  `Next nX`    `//-- Valida o formulário`  `lOk := oModel061:VldData()`    `If lOk`  `//-- Se validou, grava o formulário`  `lOk := oModel061:CommitData()`  `EndIf`    `//-- Avalia erros`  `If !lOk`  `//-- Busca o Erro do Modelo de Dados`  `aErro := oModel061:GetErrorMessage()`    `//-- Monta o Texto que será mostrado na tela`  `AutoGrLog(``"Id do formulário de origem:"` `+``' ['` `+ AllToChar(aErro[``01``]) +``']'``)`  `AutoGrLog(``"Id do campo de origem: "`     `+``' ['` `+ AllToChar(aErro[``02``]) +``']'``)`  `AutoGrLog(``"Id do formulário de erro: "`  `+``' ['` `+ AllToChar(aErro[``03``]) +``']'``)`  `AutoGrLog(``"Id do campo de erro: "`       `+``' ['` `+ AllToChar(aErro[``04``]) +``']'``)`  `AutoGrLog(``"Id do erro: "`                `+``' ['` `+ AllToChar(aErro[``05``]) +``']'``)`  `AutoGrLog(``"Mensagem do erro: "`          `+``' ['` `+ AllToChar(aErro[``06``]) +``']'``)`  `AutoGrLog(``"Mensagem da solução:"`        `+``' ['` `+ AllToChar(aErro[``07``]) +``']'``)`  `AutoGrLog(``"Valor atribuído: "`           `+``' ['` `+ AllToChar(aErro[``08``]) +``']'``)`  `AutoGrLog(``"Valor anterior: "`            `+``' ['` `+ AllToChar(aErro[``09``]) +``']'``)`    `//-- Mostra a mensagem de Erro`  `MostraErro()`  `EndIf`    `//-- Desativa o modelo de dados`  `oModel061:DeActivate()`    `Else`  `MsgInfo(``"Documento não encontrado!"``,``"MyExec061"``)`  `EndIf`    `//-- Finaliza o ambiente`  `RESET ENVIRONMENT`    `Return Nil` |

***Saiba Mais:***

[PCOM01001 - Amarração Produto x Fornecedor (Rotina Automática MATA061 - EXECAUTO)](https://tdn.totvs.com/pages/releaseview.action?pageId=463823268)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
