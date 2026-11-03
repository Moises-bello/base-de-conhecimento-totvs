---
article_id: 360047678634
category: Financeiro - Contas a Receber
content_hash: 84b3dbd5d7905abddd6d6880fe28c75701f5a2840e79e340cba90c7f25b0c778
fetched_at: '2026-06-28T22:38:14.141945+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Pontos de entrada FINA330
type: support-article
updated_at: '2026-03-24T20:27:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047678634-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Pontos-de-entrada-FINA330
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39269714344855)**Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**  
Quais são os pontos de entrada da Rotina **FINA330 ?**

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA330 - Todas as versões  
  
  
**Solução**  
Segue abaixo os pontos de entrada disponíveis na rotina **FINA330**:

* **FA330FLT -Filtra dados a serem exibidos**

O ponto de entrada **FA330FLT** será executado antes da montagem da *mBrowse* na tela de compensação de contas a receber e pode ser utilizado como filtro dos dados a serem exibidos.

Para maiores informações, consulte: [FA330FLT -Filtra dados a serem exibidos](https://tdn.totvs.com/display/public/mp/FA330FLT+-Filtra+dados+a+serem+exibidos+--+11977)

* **FA330MNU - Incluir botões na rotina**

Ponto de Entrada chamado antes da exibição do *Browse* para inclusão de novas funcionalidades no menu.

Para maiores  informações, consulte: [DT\_FA330MNU\_Incluir\_funcionalidades\_no\_menu](https://tdn.totvs.com/display/PROT/DT_FA330MNU_Incluir_funcionalidades_no_menu)

* **FA330FBRW - Filtro customizado**

Ponto de entrada para retornar uma expressão SQL para filtro no *mBrowse* sem que a opção de filtro do usuário seja desabilitado.

Para maiores informações, consulte: [FA330FBRW - Filtro customizado na compensação a receber](https://tdn.totvs.com/pages/releaseview.action?pageId=640905581)

* **F330DTFIN - Valida data**

Ponto de entrada para permitir ao cliente decidir se quer validar a data do parâmetro **MV\_DATAFIN** ou não.

Para maiores informações, consulte: [F330DTFIN - Valida data](http://tdn.totvs.com/display/public/mp/F330DTFIN+-+Valida+data+--+11748)

* **F330DESC - Desconto na Compensação CR**

Define se na compensação de títulos a receber é calculado o desconto financeiro. Para o cálculo do desconto é levado em consideração o percentual de desconto informado no campo **E1\_DESCFIN**. Esta operação de desconto em compensação é uma particularidade do Módulo **OMS**.

Para maiores informações, consulte: [F330DESC - Desconto na compensação contas a receber](https://tdn.totvs.com/pages/releaseview.action?pageId=639933364)

* **F330ATLIS - Manipulação de Array na tela de compensação**

O ponto de entrada **F330ATLIS** foi disponibilizado para manipulação do *array*a títulos antes da confirmação de compensação.

Para maiores informações, consulte: https://tdn.totvs.com/pages/releaseview.action?pageId=639930534

* **F330BOTON - Cria novo botão**

Ponto de Entrada que permite criar novos botões na tela de seleção dos títulos a receber a serem compensados.

Para maiores informações, consulte: [F330BOTON - Cria novo botão](http://tdn.totvs.com/pages/releaseview.action?pageId=6071526)

* **FA330CMP - Confirma títulos**

O ponto de entrada **FA330CMP** é utilizado após a confirmação dos títulos selecionados.

Para maiores informações, consulte: [FA330CMP - Confirma títulos](http://tdn.totvs.com/pages/releaseview.action?pageId=6071206)

* **FA330BX - Compensação de títulos a receber**

O ponto de entrada **FA330BX** está disponível para procedimentos internos do usuário, através dele é possível ter acesso ao dados dos títulos a receber que serão baixados.

Para maiores informações, consulte: [FA330BX - Baixa de títulos na compensação a receber](http://tdn.totvs.com/pages/releaseview.action?pageId=113803836)

* **F330SE5 - Manipula Movimentos bancários processados na compensação**

O ponto de entrada **F330SE5** manipula Movimentos Bancários Processados tendo como parâmetro o **Recno** dos registros **SE5** que foram utilizados na Compensação.

Para maiores informações, consulte: [F330ATLIS - Manipulação das informações antes da confirmação de compensação](https://tdn.totvs.com/pages/releaseview.action?pageId=639930534)

* **FA330ORD - Altera ordem de exibição**

Permite a mudança da ordem ao qual os os títulos serão exibidos na *markbrowse*. O Ponto de entrada deve retornar um valor numérico equivalente a ordem especificada no **SIX**.

Para maiores informações, consulte: [FA330ORD - Altera ordem de exibição](http://tdn.totvs.com/pages/releaseview.action?pageId=6071210)

* **FA330QRY - Manipula Query**

O ponto de entrada **FA330QRY** está na função **Fa330Tit()** que possibilita criar e manipular a *query.*

Para maiores informações, consulte: [FA330QRY - Manipulação da query da compensação de contas a receber](https://tdn.totvs.com/pages/releaseview.action?pageId=640906264)

* **F330RIO - Trata filtros de títulos em adiantamento**

O ponto de entrada **F330RIO** trata o filtro de títulos de adiantamento a serem considerados ou não no *array* dos adiantamentos que devem ser compensados. O retorno é logico

Para maiores informações, consulte: [F330RIO - Trata filtros de títulos em adiantamento](http://tdn.totvs.com/pages/releaseview.action?pageId=6071014)

* **FI330ALT**

Ponto de entrada antes da compensação dos títulos, que permite a edição do *array* que contém as informações sobre os títulos que serão compensados.

Para maiores informações, consulte: [DT\_FI330ALT\_Altera\_array\_titulos](https://tdn.totvs.com/display/PROT/DT_FI330ALT_Altera_array_titulos)

* **FI330EST - Manipulação de parâmetros na rotina de Estorno CR.**

O ponto de entrada **FI330EST** manipula os parâmetros usados para filtros de títulos na rotina de **Estorno** e **Exclusão**, na **Compensação de títulos a receber**.

Para maiores informações, consulte: [FI330EST - Manipulação de parâmetros na rotina de Estorno CR.](http://tdn.totvs.com/pages/releaseview.action?pageId=6071627)

* **F330FLTC - Dispensa cancelamento**

O ponto de entrada **F330FLTC** será utilizado para dispensar do cancelamento.

Para maiores informações, consulte: [F330FLTC - Dispensa cancelamento](http://tdn.totvs.com/display/public/mp/F330FLTC+-+Dispensa+cancelamento+--+11749)

* **F330EXCOMP - Valida exclusão/estorno da compensação**

O ponto de entrada **F330EXCOMP** efetua validações adicionais na **exclusão**/**estorno da compensação de Contas a receber**. Este ponto de entrada identifica através do terceiro parâmetro em qual operação está sendo realizada (5=Estorno e 4=Exclusão).

Para maiores informações, consulte: [F330EXCOMP - Valida exclusãoestorno da compensação](http://tdn.totvs.com/pages/releaseview.action?pageId=6071473)

* **F330AE5E -** Alteração do histórico na **SE5** no momento do estorno**.**
* **F330VEEX -** Gravação de dados exclusão/estorno

Ponto de entrada para gravação de dados ao **Excluir** e **Estornar** a **compensação de títulos a Receber**.

Para maiores informações, consulte: [F330VEEX- Gravação de dados em exclusão/estorno de compensação de títulos a receber](https://tdn.totvs.com/pages/releaseview.action?pageId=639934018)

* **FA330EAC - Exclui compensação a receber**

O ponto de entrada **FA330EAC** é  utilizado na exclusão de **compensação de contas a receber**, antes da contabilização.

Para maiores informações, consulte: [FA330EAC - Exclui compensação a receber](http://tdn.totvs.com/pages/releaseview.action?pageId=6071207)

* **FA330EXC - Cancela faturas a receber**

O ponto de entrada **FA330EXC** é utilizado no cancelamento de**Faturas a receber**.

Para maiores informações, consulte: [FA330EXC - Cancela faturas a receber](http://tdn.totvs.com/display/public/mp/FA330EXC+-+Cancela+faturas+a+receber+--+11976)

* **FA330VLD - Customiza validação**

O ponto de entrada **FA330VLD** tem como finalidade possibilitar customização de uma validação na confirmação dos títulos a compensar. Este ponto de entrada não passa nenhum parâmetro e deve ter retorno logico (.T. ou .F.) e será ativado ao confirmar no botão OK.

Para maiores informações, consulte: [Fa330Vld - Customiza validação](http://tdn.totvs.com/pages/releaseview.action?pageId=6071213)

* **F330VALID - Possibilita novas validações de campos no FINA330**

O ponto de entrada **F300VALID** possibilita novas validações de campos na função **Tudo Ok** (**Fa330TudOk**) da rotina Compensação do contas a receber (**FINA330**).

Este ponto de entrada é executado após clicar em *Ok*, ao escolher o título a ser compensado.

Para maiores informações, consulte: [F300VALID - Validação adicional compensação de contas a receber](https://tdn.totvs.com/pages/releaseview.action?pageId=641461324)

* **FA330LIB - Habilita/desabilita botões**

O ponto de entrada **FA330LIB** recebe um *array* que permite habilitar ou desabilitar botões da tela de Compensação de Títulos.

Para maiores informações, consulte: [FA330LIB - Habilitadesabilita botões](http://tdn.totvs.com/pages/releaseview.action?pageId=6071555)

* FA330SE1 Grava dados

O ponto de entrada FA330SE1 é utilizado na gravação complementar do SE1 na compensação.

[FA330SE1 Grava dados](https://tdn.totvs.com/display/public/mp/FA330SE1+Grava+dados++--+11980)
