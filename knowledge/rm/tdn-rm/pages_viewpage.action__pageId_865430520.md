---
content_hash: a3ab50cb76062a927f84b2708adf3d3cbc837e2899911cbbd25c963c957437cd
fetched_at: '2026-06-29T00:11:56.433785+00:00'
page_id: '865430520'
product: rm
source: tdn-rm
title: Relatórios - Ficha Financeira Sintética
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=865430520
version: 4
---

O relatório de ***Ficha Financeira Sintética*** apresenta as informações financeiras resumidas da venda selecionada.

Este relatório está disponível para instalação  para instalação a partir da opção [TOTVS Compartilhamento](https://tdn.totvs.com/display/LRM/TOTVS+Compartilhamento), na barra [Central de Recursos](https://tdn.totvs.com/display/LRM/Habilitando+painel+da+central+de+recursos), na lateral direita da tela do RM.

Para disponibilizá-lo para o TCGI, pesquise por TINREL0067, com o tipo relatório do produto Gestão Imobiliária, conforme imagem abaixo e siga as instruções desta [página](https://tdn.totvs.com/display/LRM/TOTVS+Compartilhamento):

Uma vez que este relatório está instalado, para gerá-lo, acesse o cadastro de vendas, selecione a venda desejada, vá em processos, relatórios e ficha financeira:

Ao acessar esta opção selecione o relatório *TINREL0067*, defina a **Data Base**, que é a data da competência\* em que serão buscadas as informações na base de dados e selecione também, as opções desejadas, conforme descrito abaixo:

* **Imprimir Resíduo:** Imprime a somatória de todos os valores de resíduo, quando há este componente no plano de financiamento da venda;
* **Considerar Multa e Juros:** Imprime os valores de multa e juros, calculados no módulo financeiro;
* **Considerar Deságio:** Ao marcar esta opção, caso o plano de financiamento da venda seja no tipo PRICE, o sistema irá calcular os valores atualizado da venda em relação à data base informada;
* **Posição Atual da Base:** Ao marcar esta opção, o sistema irá apresentar os valores da venda na competência da data de execução, considerando as opções citadas acima. Marcando esta opção, o campo Data Base será desabilitado:

Competência!

Ao filtrar a Data Base para geração da ficha Financeira, o resultado sempre será o valor da competência do mês/ano filtrado no relatório, ou seja, o retrato dos logs da(s) parcela(s) para o último dia do mês solicitado.

A ficha financeira **não**trabalha com valores pro-rata (por dia) e **não** executa o reajuste para o mês solicitado,

Este relatório apresenta as seguintes informações:

* **Cabeçalho:**
  + **Empreendimento:** Código e nome do empreendimento da venda selecionada;
  + **Unidade:** Código e descrição da unidade, bloco ou quadra ao qual o imóvel da venda pertence;
  + **Subunidade:** Código e descrição da subunidade, ou apartamento ou lote, do imóvel que é objeto deste contrato de venda;
  + **Cliente:** Código e nome de cliente que é o comprador principal deste contrato de venda;
  + **CNPJ/CPF:** CNPJ ou CPF do comprador principal associado a esta venda;
  + **Telefone:** Telefone associado ao cliente desta venda;
  + **Numero da Venda:** Número da venda selecionada;
  + **Data da Venda:** Data de assinatura do contrato desta venda informada no campo *data venda/aluguel*, do cadastro de vendas;
  + **Situação:** Situação de cadastro da venda selecionada (bloqueada, distratada, efetivada, em preparação, proposta ou quitada), na competência informada;
  + **Data Base:** É a data base utilizada para o buscar nas tabelas de log, os valores relativos à venda;
  + **Títulos a Receber:** Detalha os valores receber da venda:
    - **Valor da Venda:** É o valor do imóvel do contrato;
    - **Valor Original Atualizado:** É o valor original da venda, sem considerar os cálculos o módulo financeiro, atualizado até o último reajuste aplicado nesta competência. Este valor não é calculado pelo sistema, ele é obtido através do valor gravado nas tabelas de log, na competência informada;
    - **Valor da Venda Atualizada:** É o valor da venda, considerando os cálculos o módulo financeiro (juros, multa, etc.), na competência informada, gravado nas tabelas de log. Os valores do financeiro são calculados em relação à data base da competência;
    - **Saldo devedor:** É todo o saldo devedor da venda na data base/competência informada.
  + **Títulos a Pagar:** Detalha os valores a Pagar da venda (geralmente utilizado em casos de distrato):
    - **Valor a Pagar Atualizado:** É a soma dos valores de todas as parcelas ativas (que não estejam canceladas) a pagar, em relação à data base/competência informada;
    - **Saldo Devedor:** É o saldo devedor (valor em aberto) das parcelas a pagar, em relação à data base/competência informada.
* **Detalhamento:**
  + **Total de Subunidades:** É a soma das subunidades associadas à venda. O TCGI não permite mais que uma subunidade por contrato de venda;
  + **Valor da Venda:** Idem mesmo item descrito no cabeçalho;
  + **Valor Original Atualizado:** Idem mesmo item descrito no cabeçalho;
  + **Valor da Venda Atualizada:** Idem mesmo item descrito no cabeçalho;
  + **Saldo Devedor:** Idem mesmo item descrito no cabeçalho;
* **Totalizador:**
  + **Total de Subunidades:** Idem mesmo item descrito no cabeçalho;
  + **Valor da Venda:** Idem mesmo item descrito no cabeçalho;
  + **Valor Original Atualizado:** Idem mesmo item descrito no cabeçalho;
  + **Valor da Venda Atualizada:** Idem mesmo item descrito no cabeçalho;
  + **Saldo Devedor:** Idem mesmo item descrito no cabeçalho;
