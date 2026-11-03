---
article_id: 360047688774
category: Financeiro - Baixas a Receber
content_hash: 1d5f46a62042d12dc6502a1be7dab10fa48fbb12cb37c7872be639eb1151cbc0
fetched_at: '2026-06-28T22:37:43.747677+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Pontos de entrada FINA070
type: support-article
updated_at: '2026-05-11T16:30:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047688774-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Pontos-de-entrada-FINA070
---

**Dúvida**  
Quais os pontos de entrada da rotina **FINA070** ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**  
Segue abaixo a relação dos pontos de entrada da rotina **FINA070**:

**F070ACONT** - Chamado antes da contabilização

**F070ACRE** - Execução antes da confirmação da Baixa a Receber  
<https://tdn.totvs.com/pages/viewpage.action?pageId=110432873>

**F070AltV** - Validação da data da baixa  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6070913>

**F070BAUT** - Valida *Execauto*  
<https://tdn.totvs.com/display/public/mp/F070BAUT+-+Valida+Execauto+--+109962>

**F070BROW** - Pré-validação de dados **baixa de títulos a receber**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6070914>

**F070BTOK** - Confirmação da baixa a receber  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6070915>

**F070BXABT** - Retorno do título para carteira

**F070BXLT** - Validação de Baixa  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6071684>

**F070BXPC** - Exibição automática da tela de baixas  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6071671>

**F070CANABT** - Retorno do título para carteira

**F070CANCEL** - Manipula as variáveis Cancelamento de Baixas  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6071474>

**F070CCAN** - Validações adicionais no cancelamento de **Baixas a Receber**, quando Cancelar  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6071588>

**F070CHDV** - Campo cancelamento por devolução de cheque irá aparecer selecionado ou não  
<https://tdn.totvs.com/display/public/mp/F070CHDV+-+Marca+campo+--+116302>

**F070CLOK** - Validação de linhas de grade  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6070916>

**F070CMC7** - Validações ou alterações das informações dos dados do cheque  
<https://tdn.totvs.com/display/PROT/DT_F070CMC7_Impressora_de_Cheque>

**F070CTB** - Somas Valores Desejados com valor do Título  
<https://tdn.totvs.com/pages/viewpage.action?pageId=113804788>

**F070DCDESC** - Alteração de valor de desconto no cancelamento da baixa a receber  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6071563>

**F070DCHQ** - Altera ou insere dados adicionais na inclusão do cheque  
<https://tdn.totvs.com/display/PROT/F070DCHQ>

**F070DCNB** - Desabilita campos juros, multa, desconto e outros  
<https://tdn.totvs.com/display/public/mp/F070DCNB+-+Desabilita+campos+juros%2C+multa%2C+desconto+e+outros+--+22940>

**F070DESC** - Validação de desconto  
<https://tdn.totvs.com/pages/viewpage.action?pageId=6071704>

**F070DSC** - Permite a digitação de valor de desconto  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6070920>

**F070DTCR** - Simular outra data base ou data crédito

**F070DTRE** - Permite a digitação do campo Data Recebimento  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6071326>

**F070EST** - Gravação complementares do cancelamento

**F070EST2** - Gravação complementares do cancelamento

**F070HISCAN** - Alteração do Cancelamento de Baixa a Receber  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6071607>

**F070IRBX** - Permite a manipulação do juros apos o valor liquido

**F070JRS** - Digitação de valor de juros  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6070922>

**F070JRVlR** - Alteração do valor de Juros na Baixa a Receber  
<https://tdn.totvs.com/pages/viewpage.action?pageId=6071608>

**F070KCO** - Valida código do banco  
<https://tdn.totvs.com/pages/viewpage.action?pageId=39125013>

**F070MNAT** - Rateio de título baixado entre múltiplas naturezas  
<https://tdn.totvs.com/pages/viewpage.action?pageId=111182103>

**F070MUL** - Digitação do valor de multa na baixa de CR  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6070923>

**F070OWN** - Montagem do filtro da baixa  
<https://tdn.totvs.com/display/public/mp/F070OWN+-+Montagem+do+filtro+da+baixa+--+11652>

**F070TCTR** - Controle do total de cheques informados com o total a ser baixado

**F070TPBA** - Validação do Campo **Mov. Bancário** (**ED\_MOVBCO**)  
<https://tdn.totvs.com/display/PROT/F070TPBA>

**F070TRAVA** - Trava/Destrava registros da **SA1**  
<https://tdn.totvs.com/display/PROT/F070TRAVA+-+trava+ou+destrava+os+registros+da+tabela+SA1>

**F070TREA** - Envio de valor personalizado na tag de processo da mensagem única *UpdateContractParcel*  
<https://tdn.totvs.com/pages/viewpage.action?pageId=381046561>

**F070TXPER** - Altera ou valida taxa de permanência  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6071603>

**F070VCHL** - Somente validar o total dos cheques no botão *OK*

**F070VDATA** - Validar os dados da baixa dos campos:Taxa contratada,Desconto,Multa,Taxa de permanência (juros)  
<https://tdn.totvs.com/display/public/mp/F070VDATA+-+Valida+dados+da+baixa+--+23157>

**F070VREC** - Valid do campo valor recebido  
<https://tdn.totvs.com/display/public/mp/F070VREC+-+Valid+do+campo+valor+recebido+--+11653>

**F070VSE5** - Validação de Gravação de campos na **SE5**, após baixa por lote.  
<https://tdn.totvs.com/display/PROT/F070VSE5>

**FA070BCO** - Validação adicional de banco  
<https://tdn.totvs.com/pages/viewpage.action?pageId=155582686>

**FA070BLQ** - Manipulação da correção monetária na baixa do contas a receber  
<https://tdn.totvs.com/display/PROT/FA070BLQ>

**FA070BTN** - Adicionar, alterar ou remover botões da tela de parâmetros de baixa do contas a receber  
<https://tdn.totvs.com/display/PROT/DT_FA070BTN_adic_remo_alt_botoes>

**FA070BXL** - Efetua baixa por lote  
<https://tdn.totvs.com/display/public/mp/FA070BXL+-+Efetua+baixa+por+lote+--+11873;jsessionid=B9319BB1327EBFD2975884545441A631>

**FA070CA2** - Cancela baixas  
<https://tdn.totvs.com/display/public/mp/FA070CA2+-+Cancela+baixas+--+11875>

**FA070CA3** - Verifica cancelamento  
<https://tdn.totvs.com/display/public/mp/FA070CA3+-+Verifica+cancelamento+--+11876>

**FA070CA4** - Permite cancelar baixa  
<https://tdn.totvs.com/display/public/mp/FA070CA4+-+Permite+cancelar+baixa+--+11877>

**FA070CAN** - Grava dados de cancelamento  
<https://tdn.totvs.com/display/public/mp/FA070CAN+-+Grava+dados+de+cancelamento+--+11878>

**FA070CHK** - Efetua baixas a receber  
<https://tdn.totvs.com/display/public/mp/FA070CHK+-+Efetua+baixa+a+receber+--+11879>

**FA070IMP -** Retorno os valores dos impostos IRRF, ISS, PIS, COFINS, CSLL, INSS  
<https://tdn.totvs.com/display/public/mp/Ponto+de+Entrada+FA070IMP>

**FA070MDB** - Valida motivo de baixa  
<https://tdn.totvs.com/display/public/mp/FA070MDB+-+Valida+motivo+da+baixa+--+11882>

**FA070POS** - Baixa títulos a receber  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6071134>

**FA070TIT** - Confirma baixa a receber  
<https://tdn.totvs.com/display/public/mp/FA070TIT+-+Confirma+baixa+a+receber+--+11884>

**SE5FI70E** - Cancelamento de baixa  
<https://tdn.totvs.com/pages/viewpage.action?pageId=389547437>

**FJURREC** - Ponto de Entrada: recalculo de juros a receber  
<https://tdn.totvs.com/display/public/PROT/FJURREC+-+Ponto+de+Entrada+recalculo+de+juros+a+recebe>

**FJURCST** - Cálculo de juros

<https://tdn.totvs.com/pages/releaseview.action?pageId=6071298>

**Saiba mais:**  
<https://tdn.totvs.com/pages/viewpage.action?pageId=389547437>
