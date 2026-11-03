---
article_id: 22899052026263
category: Financeiro - Movimentação Bancária
content_hash: b3e462b0f10bf0eb0ff561a148887ca3c2c70edb7051c44868ef466308586993
fetched_at: '2026-06-28T22:38:19.492879+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA100 - Pontos de
  entrada
type: support-article
updated_at: '2025-01-08T20:58:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22899052026263-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA100-Pontos-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22899072755863) Tempo aproximado para leitura: **00****:08:00 min** **Dúvida** **Quais os pontos de entrada da rotina FINA100 ?**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas versões  
  
**Solução**

**F100BROW**   
O ponto de entrada será executado antes do *browse* da **movimentação bancaria.**

Documentação: <https://tdn.totvs.com/pages/releaseview.action?pageId=6070950>

**FA100PAG**   
O ponto de entrada será utilizado após gravação dos dados e da contabilização de **contas a pagar** na **movimentação bancaria.**

Documentação: <http://tdn.totvs.com.br/display/public/mp/FA100PAG+-+Grava+dados+--+11930>

**FA100REC**   
O ponto de entrada será utilizado após a gravação dos dados e da contabilização de **contas a receber** na **movimentação bancária.**

Documentação: <https://tdn.totvs.com.br/display/public/mp/FA100REC+-+Grava+dados+--+11931>

**FINATROC**

executado após a gravação de todos os dados da movimentação a receber e da contabilização. Utilizado somente pelo ambiente **SIGALOJA.**

Documentação: [FINATROC - Gravação de dados da movimentação a receber -- 12069](https://tdn.totvs.com/pages/viewpage.action?pageId=6071292)

**FA100VLD**   
permite ao usuário criar validações quanto ao acesso para **exclusão e cancelamento de movimento bancário.**

Documentação: <https://tdn.totvs.com/pages/releaseview.action?pageId=6071360>

**FA100CA2**   
executado após a confirmação da **Exclusão da Movimentação Bancária**, antes de efetuar a **exclusão e a contabilização.**

Documentação: [FA100CA2 - Cancela movimentação bancária -- 11924](https://tdn.totvs.com/pages/releaseview.action?pageId=6071159)

**FA100CAN**   
O ponto de entrada será utilizado após a exclusão da **movimentação bancária** e antes da contabilização.

Documentação: [FA100CAN - Cancela movimento bancário -- 11925](https://tdn.totvs.com/pages/releaseview.action?pageId=6071160)

**FA100Get**   
permite ao cliente preencher automaticamente os dados da tela de **transferência bancária**.

Documentação: [FA100GET - Preenchimento da tela de Transferência Bancária -- 109531](https://tdn.totvs.com/pages/releaseview.action?pageId=6071576)

**FA100TRF**   
executado antes da **transferência** e retornara **.T.** para gravar a **transferência** ou **.F.** em caso contrário.

Documentação: [FA100TRF - Grava transferência](https://tdn.totvs.com/pages/releaseview.action?pageId=571005838)

**F100DOC**   
utilizado para alterar o numero do cheque no momento da **transferência entre bancos e agencias.**

Documentação: <https://tdn.totvs.com.br/pages/releaseview.action?pageId=6070951>

**A100BL01**   
executado após a gravação dos dados da **transferência bancaria.**

Documentação: [A100BL01 - Gravação de dados -- 11548](https://tdn.totvs.com/pages/releaseview.action?pageId=6070830)

**FA100DOC**   
será utilizado para manipular a variável cDocTran. Retorno: valor que deverá conter em cDocTran. Parâmetros: **cBcoOrig, cAgenOrig, cCtaOrig, cTipoTran**

Documentação: [FA100DOC - Manipula variável -- 11926](FA100DOC%20-%20Manipula%20vari%C3%A1vel%20--%2011926)

**A100TR01**   
utilizado na gravação de **transferência do movimento bancário.**

Documentação: [A100TR01 - Transferencia de movimento bancario](http://tdn.totvs.com.br/display/public/mp/A100TR01+-+Transferencia+de+movimento+bancario+--+11549)

**A100TRA**   
O ponto de entrada A100TRA complementa o ponto de entrada **A100TR01**. Esse ponto de entrada recebe um array de parâmetros com o seguinte conteúdo: **lEstorno, cBcoOrig, cBcoDest, cAgenOrig, cAgenDest, cCtaOrig, cCtaDest, cNaturOri, cNaturDes, cDocTran,cHist100.**

Documentação: [A100TRA - Movimentação bancária -- 11552](https://tdn.totvs.com/pages/releaseview.action?pageId=6070834)

**A100TR02**   
utilizado durante a gravação dos dados de **transferência bancaria**

Documentação: [A100TR02 - Gravação de dados de transferencia bancária -- 11550](https://tdn.totvs.com/pages/releaseview.action?pageId=6070832)

**A100TRB**   
O ponto de entrada **A100TRB** complementa o ponto de entrada **A100TR02.**  
Esse ponto de entrada recebe um array de parâmetros com o seguinte conteúdo: **lEstorno, cBcoOrig, cBcoDest, cAgenOrig, cAgenDest, cCtaOrig, cCtaDest, cNaturOri, cNaturDes, cDocTran, cHist100.**

Documentação: [A100TRB - Gravação de transferência -- 11553](https://tdn.totvs.com/pages/releaseview.action?pageId=6070835)

**A100TR03**   
executado após gravação dos dados da **transferência bancaria.** Após gravar o **SE5** de ambos **bancos** **Origem** / **Destino**, após a contabilização.

Documentação: [A100TR03 - Gravação de dados de transferencia bancaria -- 11551](https://tdn.totvs.com/pages/releaseview.action?pageId=6070833)

**A100TRC**   
O ponto de entrada **A100TRC** complementa o ponto de entrada **A100TR03**.  
Esse ponto de entrada recebe um array de parâmetros com o seguinte conteúdo: **lEstorno, cBcoOrig, cBcoDest, cAgenOrig, cAgenDest, cCtaOrig, cCtaDest, cNaturOri, cNaturDes, cDocTran, cHist100.**

Documentação: [A100TRC - Gravação da transferência -- 11554](https://tdn.totvs.com/pages/releaseview.action?pageId=6070836)

**F100TOK**   
valida os dados da **movimentação bancária**.

Documentação: [F100TOK - Validar dados da movimentação bancária -- 11688](https://tdn.totvs.com/pages/releaseview.action?pageId=6070954)

**FA100ROT**   
Permite a inclusão de botões customizados na *EnchoiceBar* da rotina **Movimento Bancário**.

Documentação: [FA100ROT - Inclusão de botões customizados na EnchoiceBar -- 30104](https://tdn.totvs.com/pages/releaseview.action?pageId=6071399)

**FA100OKP**   
utilizado para bloquear a inclusão de **movimentos a pagar** na rotina **Movimentos Bancários.** Se o retorno for verdadeiro, o movimento será realizado normalmente, caso contrario não haverá inclusão do movimento. Retorno lógico.

Documentação: [FA100OKP - Bloqueia inclusão de movimentos -- 11928](https://tdn.totvs.com/pages/releaseview.action?pageId=6071163)

**FA100OKR**   
utilizado para bloquear a inclusão de movimentos a receber na rotina **Movimentos bancários**. Caso o retorno seja verdadeiro o movimento é feito normalmente, caso contrario não se fará a inclusão do movimento. Retorno lógico.

Documentação: [FA100OKR - Bloqueia inclusão de movimentos -- 11929](https://tdn.totvs.com/pages/releaseview.action?pageId=6071164)

**A85CHPDT**   
permite que o usuário possa fazer seu próprio tratamento para selecionar os cheques de terceiros que poderão ser utilizados no tipo de pagamento informado na opção pagamento diferenciado.

Documentação: [A85CHPDT - Seleção de cheques de terceiros -- 11564](https://tdn.totvs.com/pages/releaseview.action?pageId=6070845)

**F100FBRW**   
O ponto de entrada será executado antes do *browse* da movimentação bancaria.

Documentação: [F100FBRW - Permite filtrar as movimentações bancárias](https://tdn.totvs.com/pages/releaseview.action?pageId=653139088)

**FA100NAT**   
Ponto de entrada que permite não validar o CST na rotina **FINA100**.

Documentação: [FA100NAT Não valida CST de Credito](https://tdn.totvs.com/display/public/PROT/DT_FA100NAT_NAO_VALIDA_CST_FINA100)

**Saiba mais:**

[Movimentos Bancários - FINA100 - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=501480542)

[Pontos de Entrada - Financeiro - P12](https://tdn.totvs.com/display/public/PROT/Pontos+de+Entrada+-+Financeiro+-+P12)
