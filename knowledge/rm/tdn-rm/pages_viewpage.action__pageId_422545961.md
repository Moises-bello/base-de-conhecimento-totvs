---
content_hash: c2739b5a9573a3cce28e031db2242bd53b0a123c824e0db2d4f39443f41c9f82
fetched_at: '2026-06-29T00:09:22.085578+00:00'
page_id: '422545961'
product: rm
source: tdn-rm
title: Compensação de Tributos (Federais)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545961
version: 7
---

O sistema de Gestão Fiscal foi alterado de modo a proporcionar o controle de Compensações de Tributos Federais e geração das fichas correspondentes da DCTF.  
 Qualquer tributo administrado pela SRF passível de restituição poderá ser compensado com DÉBITOS PRÓPRIOS;  
 A compensação deverá ser comunicada previamente à SRF através de Declaração de Compensação feita na PER/DCOMP;  
 A responsabilidade pelo lançamento do valor a ser compensado é exclusiva do usuário, uma vez que a compensação pode ser indeferida pela SRF, devendo o contribuinte, nesses casos, pagar o valor do débito compensado indevidamente com juros e multa;

O valor do crédito será acrescido da Taxa SELIC a partir do mês subseqüente ao do pagamento que tenha sido efetuado (a partir de 31/12/1997), mais 1% (hum por cento) no mês da compensação (exceto quando a compensação ocorrer no mesmo mês que originou o crédito).   
 Deverá ser informado nos parâmetros (03.02.06 - Opções/Parâmetros/Gerais Tabelas/Apuração de Tributos/Pis/Compensação de Tributo) , o índice que será Utilizado para Cálculo das Compensações de Tributos.  
 O valor compensado deve corresponder à relação entre o valor original e os juros, assim como é calculado pela PER/DCOMP.

**Cadastro de Compensação**

Através deste cadastro será possível inserir os dados da PER/DCOMP, bem como associar a Guia que gerou direito a Crédito e as Guias que serão utilizadas para a Compensação.  
Com relação às informações do DARF que gerou o crédito, haverá duas formas de informá-lo:

* Por vinculação, caso o DARF tenha sido gerado no próprio Sistema de Gestão Fiscal OU
* Por digitação.

**Informações Apresentadas**

**Identificador da Compensação**

Identificador da Compensação, gerado de forma Auto-Incremental.

**Informações Fornecidas**

Os seguintes dados deverão ser informados na tela de compensação:  
**Tributo**: Informe o Tributo a ser utilizado para a compensação. Esse campo é de preenchimento obrigatório  
**Data de Transmissão**: Informe a Data de Transmissão do pedido de compensação. Esse campo somente deverá ser preenchido após a solicitação do crédito realizada através do cadastro do Crédito com a Data do Recibo da DCOMP gerado pelo programa da RFB.  
**Numero do Pedido**: Informe o Número do Pedido da compensação. Esse campo somente deverá ser preenchido após a solicitação do crédito realizada através do cadastro do Crédito com Número do Recibo da DCOMP gerado pelo programa da RFB. O mesmo somente está disponível para preenchimento após finalizar a compensação.  
**Tipo do Crédito**: Selecione o tipo de crédito da compensação. Esse campo é de preenchimento obrigatório.   
**Formalização de Pedido**: Selecione a formalização do pedido de crédito. Esse campo é de preenchimento obrigatório. As opções disponíveis são:

* DCOMP
* DCOMP com Direito Creditório Reconhecido em Processo
* Processo Administrativo

**Descrição do Pedido:** Informe a descrição do pedido de crédito.   
**Valor Original:** Informe o valor original do crédito.  
**Valor do Crédito:** Informe o valor do crédito na data de transmissão.  
**Identificador da Guia:** Informe a Guia a ser associada. Essa guia é correspondente a guia que originou o débito do pagamento indevido. Todos os campos abaixo serão preenchidos automaticamente e serão correspondentes a essa guia.  
***Observação*:**Caso não seja informado o Identificador da Guia, os campos referente aos Dados da Guia  deverão ser preenchidos manualmente.  
***Atenção!***Serão associadas somente as Guias de Crédito já baixadas.

**Informações a Serem Calculadas**

Taxa Selic Acumulada: Este campo deverá ser calculado com os Juros acumulados da SELIC, cuja moeda foi indicada no campo "Ìndice para Compensação de Tributos Federais" nos parâmetros do RM Liber, desde a **data do Pagamento Indevido ou a maior****(Data da baixa informada através do sistema RmFluxus)** até o mês anterior à **data de transmissão** do pedido mais 1 % (hum por cento), referente ao mês da compensação.   
***Observação*:**Quando a compensação ocorrer no mesmo mês que originou o crédito, não haverá o acréscimo de 1%.

**Valor Atualizado do Crédito**

**Cálculo:**Valor Atualizado do Crédito = Valor do Crédito + (Valor do Crédito x Taxa Selic Acumulada)/100

**Valor Compensado do Crédito Acumulado**

**Cálculo:**Valor Compensado do Crédito Acumulado = Soma (Valor Compensado na Guia)  
  
**Valor dos Juros sobre o Valor Compensado Acumulado**

**Cálculo:**Valor dos Juros sobre o Valor Compensado Acumulado = Soma (Valor dos Juros da Compensação na Guia)

**Saldo Residual do Crédito**

**Cálculo:**Saldo Residual do Crédito = Valor do Crédito - Valor Compensado

---

Como fazer

[Como fazer compensação de tributos federais](http://tdn.totvs.com/pages/viewpage.action?pageId=149882527)
